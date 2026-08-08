#!/usr/bin/env python3
"""
Resemble Detect CLI Runner for ZORIXEL AIOS
Provides direct interaction with Resemble AI v2 API for deepfake detection,
audio source tracing, and media intelligence.
"""

import sys
import os
import json
import time
import argparse
import urllib.request
import urllib.parse
import urllib.error

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_URL = "https://app.resemble.ai/api/v2"


def get_auth_header():
    api_key = os.environ.get("RESEMBLE_API_KEY", "").strip()
    if not api_key:
        print("[ERROR] RESEMBLE_API_KEY environment variable is not set.", file=sys.stderr)
        print("Please export or set RESEMBLE_API_KEY before running detection commands.", file=sys.stderr)
        sys.exit(1)
    return {"Authorization": f"Bearer {api_key}"}


def make_request(url, method="GET", headers=None, data=None):
    req_headers = get_auth_header()
    if headers:
        req_headers.update(headers)

    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            return json.loads(res_body), response.status
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        try:
            err_json = json.loads(error_body)
        except Exception:
            err_json = {"raw": error_body}
        print(f"[ERROR] HTTP {e.code}: {json.dumps(err_json, indent=2)}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def upload_secure_file(file_path):
    """Upload large or private file via secure_uploads endpoint using multipart/form-data."""
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    url = f"{BASE_URL}/secure_uploads"
    boundary = "----WebKitFormBoundaryAIOSResembleDetect"
    filename = os.path.basename(file_path)

    with open(file_path, "rb") as f:
        file_bytes = f.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n"
    ).encode("utf-8") + file_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    res, status = make_request(url, method="POST", headers=headers, data=body)
    return res.get("item", {}).get("media_token") or res.get("media_token")


def submit_detect(url=None, file_path=None, media_token=None, options=None):
    options = options or {}
    api_url = f"{BASE_URL}/detect"
    headers = {}

    if options.get("prefer_wait"):
        headers["Prefer"] = "wait"

    if file_path and not media_token:
        # Check size: if > 150MB, use secure upload
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > 150:
            print(f"[INFO] File size ({file_size_mb:.1f} MB) > 150 MB. Utilizing secure_uploads token...", file=sys.stderr)
            media_token = upload_secure_file(file_path)
            file_path = None
        else:
            # Multipart upload directly to /detect
            boundary = "----WebKitFormBoundaryAIOSResembleDetect"
            filename = os.path.basename(file_path)

            with open(file_path, "rb") as f:
                file_bytes = f.read()

            parts = [
                f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\nContent-Type: application/octet-stream\r\n\r\n".encode("utf-8"),
                file_bytes,
                b"\r\n"
            ]

            for key in ["intelligence", "visualize", "audio_source_tracing", "use_reverse_search", "zero_retention_mode"]:
                if options.get(key):
                    parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{key}\"\r\n\r\ntrue\r\n".encode("utf-8"))

            if options.get("frame_length"):
                parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"frame_length\"\r\n\r\n{options['frame_length']}\r\n".encode("utf-8"))

            parts.append(f"--{boundary}--\r\n".encode("utf-8"))
            body = b"".join(parts)
            headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
            res, status = make_request(api_url, method="POST", headers=headers, data=body)
            return res

    # JSON payload mode
    payload = {}
    if url:
        payload["url"] = url
    elif media_token:
        payload["media_token"] = media_token
    else:
        print("[ERROR] Must provide a media URL, local file path, or media token.", file=sys.stderr)
        sys.exit(1)

    for k in ["intelligence", "visualize", "audio_source_tracing", "use_reverse_search", "zero_retention_mode"]:
        if options.get(k):
            payload[k] = True

    if options.get("frame_length"):
        payload["frame_length"] = int(options["frame_length"])

    headers["Content-Type"] = "application/json"
    data_bytes = json.dumps(payload).encode("utf-8")
    res, status = make_request(api_url, method="POST", headers=headers, data=data_bytes)
    return res


def get_detect(uuid):
    url = f"{BASE_URL}/detect/{uuid}"
    res, status = make_request(url, method="GET")
    return res


def poll_detect(uuid, max_retries=10):
    delays = [2, 2, 5, 5, 10, 10, 10, 10, 10, 10]
    for i in range(max_retries):
        res = get_detect(uuid)
        item = res.get("item", {})
        status_val = item.get("status")
        print(f"[POLL] Attempt {i+1}: Status = {status_val}", file=sys.stderr)
        if status_val in ["completed", "failed"]:
            return res
        delay = delays[i] if i < len(delays) else 10
        time.sleep(delay)
    return get_detect(uuid)


def submit_intelligence(url=None, media_token=None, media_type=None):
    api_url = f"{BASE_URL}/intelligence"
    payload = {}
    if url:
        payload["url"] = url
    elif media_token:
        payload["media_token"] = media_token
    if media_type:
        payload["media_type"] = media_type

    headers = {"Content-Type": "application/json"}
    res, status = make_request(api_url, method="POST", headers=headers, data=json.dumps(payload).encode("utf-8"))
    return res


def ask_detect_intelligence(detect_uuid, question):
    api_url = f"{BASE_URL}/detects/{detect_uuid}/intelligence"
    payload = {"query": question}
    headers = {"Content-Type": "application/json"}
    res, status = make_request(api_url, method="POST", headers=headers, data=json.dumps(payload).encode("utf-8"))
    question_uuid = res.get("item", {}).get("uuid") or res.get("uuid")

    if not question_uuid:
        return res

    # Poll question result
    poll_url = f"{BASE_URL}/detects/{detect_uuid}/intelligence/{question_uuid}"
    delays = [2, 2, 5, 5, 10]
    for i, delay in enumerate(delays):
        q_res, status = make_request(poll_url, method="GET")
        q_status = q_res.get("item", {}).get("status") or q_res.get("status")
        if q_status in ["completed", "failed"]:
            return q_res
        time.sleep(delay)
    return q_res


def main():
    parser = argparse.ArgumentParser(description="Resemble Detect CLI Runner")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Detect subcommand
    detect_parser = subparsers.add_parser("detect", help="Submit deepfake detection job")
    detect_parser.add_argument("--url", help="Public HTTPS URL of media")
    detect_parser.add_argument("--file", help="Local file path (<150MB direct, >150MB secure upload)")
    detect_parser.add_argument("--media-token", help="Secure upload token")
    detect_parser.add_argument("--visualize", action="store_true", help="Generate heatmap/treeview visualizations")
    detect_parser.add_argument("--intelligence", action="store_true", help="Run media intelligence analysis")
    detect_parser.add_argument("--audio-source-tracing", action="store_true", help="Identify voice synthesis platform")
    detect_parser.add_argument("--reverse-search", action="store_true", help="Enable reverse image search for known fakes")
    detect_parser.add_argument("--zero-retention", action="store_true", help="Auto-delete media after analysis")
    detect_parser.add_argument("--prefer-wait", action="store_true", help="Synchronous waiting mode")
    detect_parser.add_argument("--poll", action="store_true", help="Poll automatically until completion")

    # Poll subcommand
    poll_parser = subparsers.add_parser("poll", help="Poll existing detection job")
    poll_parser.add_argument("uuid", help="Detection job UUID")

    # Intelligence subcommand
    intel_parser = subparsers.add_parser("intelligence", help="Run media intelligence analysis")
    intel_parser.add_argument("--url", help="Public HTTPS URL of media")
    intel_parser.add_argument("--media-token", help="Secure upload token")
    intel_parser.add_argument("--media-type", choices=["audio", "video", "image"], help="Media type override")

    # Detect Intelligence Q&A subcommand
    ask_parser = subparsers.add_parser("ask", help="Ask natural language question about a completed detection")
    ask_parser.add_argument("uuid", help="Completed detection UUID")
    ask_parser.add_argument("question", help="Natural language question string")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "detect":
        options = {
            "visualize": args.visualize,
            "intelligence": args.intelligence,
            "audio_source_tracing": args.audio_source_tracing,
            "use_reverse_search": args.reverse_search,
            "zero_retention_mode": args.zero_retention,
            "prefer_wait": args.prefer_wait,
        }
        res = submit_detect(url=args.url, file_path=args.file, media_token=args.media_token, options=options)
        
        uuid = res.get("item", {}).get("uuid") or res.get("uuid")
        if args.poll and uuid and not args.prefer_wait:
            res = poll_detect(uuid)

        print(json.dumps(res, indent=2))

    elif args.command == "poll":
        res = poll_detect(args.uuid)
        print(json.dumps(res, indent=2))

    elif args.command == "intelligence":
        res = submit_intelligence(url=args.url, media_token=args.media_token, media_type=args.media_type)
        print(json.dumps(res, indent=2))

    elif args.command == "ask":
        res = ask_detect_intelligence(args.uuid, args.question)
        print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
