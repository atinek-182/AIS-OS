# -*- coding: utf-8 -*-
import os
import json
import yt_dlp

videos = [
    {"url": "https://youtu.be/8LL5Z9Lz0-4", "id": "8LL5Z9Lz0-4", "skills": ["pd-1-person-business"]},
    {"url": "https://youtu.be/gRcBu8LyfGo", "id": "gRcBu8LyfGo", "skills": ["pd-ikigai-pro"]},
    {"url": "https://youtu.be/DuOolRhG2UY", "id": "DuOolRhG2UY", "skills": ["pd-1-person-business"]},
    {"url": "https://youtu.be/4lbl9MtKUF8", "id": "4lbl9MtKUF8", "skills": ["pd-ikigai-pro", "pd-personal-brand-positioning"]},
    {"url": "https://youtu.be/qy_MIMtT_d8", "id": "qy_MIMtT_d8", "skills": ["pd-1-person-business"]}
]

out_dir = r"D:\ZORIXEL-BRAND-OS\research\youtube-transcripts"
os.makedirs(out_dir, exist_ok=True)

ydl_opts = {
    'skip_download': True,
    'writeautosub': True,
    'subtitleslangs': ['en', 'en-orig', 'en-US'],
    'subtitlesformat': 'vtt/json3/srv1',
    'quiet': True,
    'no_warnings': True,
}

print("Starting extraction for 5 YouTube videos...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for item in videos:
        url = item['url']
        vid = item['id']
        skills = item['skills']
        print(f"Processing {vid}...")
        try:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Title')
            channel = info.get('uploader', 'Unknown Channel')
            description = info.get('description', '')
            duration = info.get('duration', 0)
            view_count = info.get('view_count', 0)
            
            # Save raw metadata JSON
            meta_path = os.path.join(out_dir, f"{vid}_metadata.json")
            with open(meta_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'id': vid,
                    'title': title,
                    'channel': channel,
                    'description': description,
                    'duration': duration,
                    'view_count': view_count,
                    'skills': skills
                }, f, indent=2, ensure_ascii=False)
                
            print(f"  [OK] Metadata extracted for {title}")
        except Exception as e:
            print(f"  [ERROR] {vid}: {e}")

print("Extraction script completed.")
