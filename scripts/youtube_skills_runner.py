#!/usr/bin/env python3
"""
YouTube Skills Runner - Multi-Source YouTube Video Transcript, Search & Channel Engine for AIOS
Primary Backend: Local yt-dlp (Free, Unlimited, Zero API Key)
Fallback Backend: TranscriptAPI.com (Cloud Proxy, API Key: TRANSCRIPT_API_KEY)
"""

import sys
import os
import json
import subprocess
import urllib.request
import urllib.parse
import argparse
from typing import Dict, Any, Optional

# Ensure UTF-8 stdio configuration on Windows OS
sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def fetch_transcript_ytdlp(video_url: str) -> Dict[str, Any]:
    """Fetch transcript using local yt-dlp binary."""
    try:
        cmd = [
            sys.executable, "-m", "yt_dlp",
            "--write-sub",
            "--write-auto-sub",
            "--sub-lang", "en,zh-Hans,es",
            "--skip-download",
            "--dump-json",
            video_url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            return {"status": "error", "source": "yt-dlp", "message": result.stderr.strip()}

        data = json.loads(result.stdout)
        title = data.get("title", "")
        uploader = data.get("uploader", "")
        duration = data.get("duration", 0)
        description = data.get("description", "")
        subtitles = data.get("subtitles", {})
        auto_subtitles = data.get("automatic_captions", {})

        return {
            "status": "success",
            "source": "yt-dlp",
            "title": title,
            "channel": uploader,
            "duration": duration,
            "description": description[:1000] if description else "",
            "subtitles_available": list(subtitles.keys()),
            "auto_subtitles_available": list(auto_subtitles.keys()),
            "raw_info": {
                "id": data.get("id"),
                "webpage_url": data.get("webpage_url")
            }
        }
    except Exception as e:
        return {"status": "error", "source": "yt-dlp", "message": str(e)}


def fetch_transcript_api(video_url: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """Fetch transcript using TranscriptAPI.com (Fallback)."""
    key = api_key or os.environ.get("TRANSCRIPT_API_KEY")
    if not key:
        return {"status": "error", "source": "transcriptapi", "message": "TRANSCRIPT_API_KEY environment variable not set."}

    try:
        encoded_url = urllib.parse.quote(video_url)
        endpoint = f"https://transcriptapi.com/api/v2/youtube/transcript?video_url={encoded_url}&format=text&include_timestamp=true&send_metadata=true"
        req = urllib.request.Request(
            endpoint,
            headers={
                "Authorization": f"Bearer {key}",
                "User-Agent": "ZORIXEL-AIOS/1.0"
            }
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {
                "status": "success",
                "source": "transcriptapi",
                "data": data
            }
    except Exception as e:
        return {"status": "error", "source": "transcriptapi", "message": str(e)}


def get_transcript(video_url: str, mode: str = "auto", api_key: Optional[str] = None) -> Dict[str, Any]:
    """Get video transcript with ordered fallback logic."""
    if mode in ["auto", "ytdlp"]:
        res = fetch_transcript_ytdlp(video_url)
        if res.get("status") == "success":
            return res
        if mode == "ytdlp":
            return res

    # Fallback to TranscriptAPI
    return fetch_transcript_api(video_url, api_key)


def search_youtube_ytdlp(query: str, max_results: int = 5) -> Dict[str, Any]:
    """Search YouTube videos using yt-dlp search query."""
    try:
        cmd = [
            sys.executable, "-m", "yt_dlp",
            f"ytsearch{max_results}:{query}",
            "--dump-json",
            "--flat-playlist"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            return {"status": "error", "message": result.stderr.strip()}

        videos = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                item = json.loads(line)
                videos.append({
                    "title": item.get("title"),
                    "url": item.get("url") or f"https://www.youtube.com/watch?v={item.get('id')}",
                    "id": item.get("id"),
                    "uploader": item.get("uploader")
                })
            except Exception:
                pass

        return {
            "status": "success",
            "query": query,
            "count": len(videos),
            "videos": videos
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_playlist_ytdlp(playlist_url: str) -> Dict[str, Any]:
    """Extract playlist contents using yt-dlp."""
    try:
        cmd = [
            sys.executable, "-m", "yt_dlp",
            "--flat-playlist",
            "--dump-json",
            playlist_url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            return {"status": "error", "message": result.stderr.strip()}

        items = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                item = json.loads(line)
                items.append({
                    "title": item.get("title"),
                    "url": item.get("url") or f"https://www.youtube.com/watch?v={item.get('id')}",
                    "id": item.get("id")
                })
            except Exception:
                pass

        return {
            "status": "success",
            "playlist_url": playlist_url,
            "count": len(items),
            "videos": items
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def main():
    parser = argparse.ArgumentParser(description="ZORIXEL AIOS YouTube Skills Runner")
    subparsers = parser.add_subparsers(dest="action", help="Action to execute")

    # Transcript action
    t_parser = subparsers.add_parser("transcript", help="Fetch transcript for a video URL or ID")
    t_parser.add_argument("--url", required=True, help="YouTube video URL or 11-char ID")
    t_parser.add_argument("--mode", choices=["auto", "ytdlp", "api"], default="auto", help="Fetch backend mode")
    t_parser.add_argument("--api-key", help="Optional TranscriptAPI key override")

    # Search action
    s_parser = subparsers.add_parser("search", help="Search YouTube for videos")
    s_parser.add_argument("--query", required=True, help="Search query string")
    s_parser.add_argument("--max-results", type=int, default=5, help="Max results to return")

    # Playlist action
    p_parser = subparsers.add_parser("playlist", help="Extract videos from a playlist URL")
    p_parser.add_argument("--url", required=True, help="YouTube playlist URL")

    args = parser.parse_args()

    if args.action == "transcript":
        res = get_transcript(args.url, mode=args.mode, api_key=args.api_key)
        print(json.dumps(res, indent=2))
    elif args.action == "search":
        res = search_youtube_ytdlp(args.query, max_results=args.max_results)
        print(json.dumps(res, indent=2))
    elif args.action == "playlist":
        res = get_playlist_ytdlp(args.url)
        print(json.dumps(res, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
