# -*- coding: utf-8 -*-
import os
import json
import re
import yt_dlp

video_ids = ["8LL5Z9Lz0-4", "gRcBu8LyfGo", "DuOolRhG2UY", "4lbl9MtKUF8", "qy_MIMtT_d8"]
out_dir = r"D:\ZORIXEL-BRAND-OS\research\youtube-transcripts"

ydl_opts = {
    'skip_download': True,
    'writeautosub': True,
    'subtitleslangs': ['en'],
    'subtitlesformat': 'vtt',
    'outtmpl': os.path.join(out_dir, '%(id)s.%(ext)s'),
    'quiet': True,
    'no_warnings': True,
}

print("Fetching subtitles for 5 videos...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid in video_ids:
        url = f"https://youtu.be/{vid}"
        print(f"Downloading sub for {vid}...")
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Sub error for {vid}: {e}")

# Process downloaded VTT files into clean text
def clean_vtt(vtt_path):
    if not os.path.exists(vtt_path):
        return ""
    with open(vtt_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    clean_lines = []
    seen = set()
    for line in lines:
        line = line.strip()
        if not line or '-->' in line or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
            continue
        # Remove HTML tags like <c>, </c>, <00:00:00.000>
        line = re.sub(r'<[^>]+>', '', line).strip()
        if line and line not in seen:
            seen.add(line)
            clean_lines.append(line)
    return " ".join(clean_lines)

for vid in video_ids:
    vtt_file = os.path.join(out_dir, f"{vid}.en.vtt")
    clean_txt = clean_vtt(vtt_file)
    if clean_txt:
        txt_path = os.path.join(out_dir, f"{vid}_transcript.txt")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(clean_txt)
        print(f"Saved clean transcript for {vid} ({len(clean_txt)} chars)")
    else:
        print(f"No VTT found for {vid}")

print("Transcript processing completed.")
