# -*- coding: utf-8 -*-
import os
import json
from youtube_transcript_api import YouTubeTranscriptApi

videos = [
    {
        "id": "8LL5Z9Lz0-4",
        "title": "How I'd Start a $10K/Month Claude AI Side Hustle That Pays More Than a 9-5",
        "url": "https://youtu.be/8LL5Z9Lz0-4",
        "skills": ["pd-1-person-business"]
    },
    {
        "id": "gRcBu8LyfGo",
        "title": "How I'd Start a 1-Person Business With Claude AI in 30 Days",
        "url": "https://youtu.be/gRcBu8LyfGo",
        "skills": ["pd-ikigai-pro"]
    },
    {
        "id": "DuOolRhG2UY",
        "title": "How I'd Start a $10K/Month One-Person Business With Claude (Masterclass)",
        "url": "https://youtu.be/DuOolRhG2UY",
        "skills": ["pd-1-person-business"]
    },
    {
        "id": "4lbl9MtKUF8",
        "title": "How I'd Use Claude AI to Build a Premium Personal Brand (1-Person Business)",
        "url": "https://youtu.be/4lbl9MtKUF8",
        "skills": ["pd-ikigai-pro", "pd-personal-brand-positioning"]
    },
    {
        "id": "qy_MIMtT_d8",
        "title": "If you have a Job, Start a 1-Person Business with Claude AI ASAP",
        "url": "https://youtu.be/qy_MIMtT_d8",
        "skills": ["pd-1-person-business"]
    }
]

out_dir = r"D:\ZORIXEL-BRAND-OS\research\youtube-transcripts"
os.makedirs(out_dir, exist_ok=True)

for v in videos:
    vid = v['id']
    title = v['title']
    url = v['url']
    skills = v['skills']
    print(f"Fetching transcript for {vid}: {title}...")
    
    try:
        # Fetch transcript entries
        api = YouTubeTranscriptApi()
        fetched = api.fetch(vid)
        
        # Format text
        raw_text = " ".join([item.text for item in fetched])
        
        # Save transcript txt file
        txt_path = os.path.join(out_dir, f"{vid}_transcript.txt")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(raw_text)
            
        # Save structured markdown document
        md_path = os.path.join(out_dir, f"{vid}_summary.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"""# YouTube Video Ingestion: {title}

- **Video ID**: {vid}
- **URL**: [{url}]({url})
- **Associated Skill(s)**: {', '.join([f'`{s}`' for s in skills])}
- **Transcript Length**: {len(raw_text)} characters / ~{len(raw_text.split())} words

---

## Raw Transcript
{raw_text}
""")
        print(f"  [SUCCESS] {vid}: Saved transcript (~{len(raw_text.split())} words)")
    except Exception as e:
        print(f"  [ERROR] {vid}: {e}")

print("All transcript extraction completed.")
