# -*- coding: utf-8 -*-
import os
import json
from youtube_transcript_api import YouTubeTranscriptApi
from pypdf import PdfReader

out_dir = r"D:\ZORIXEL-BRAND-OS\research"
yt_dir = os.path.join(out_dir, "youtube-transcripts")
os.makedirs(yt_dir, exist_ok=True)

# 1. Ingest YouTube Videos
new_videos = [
    {
        "id": "s2KTYJOU7Yw",
        "url": "https://youtu.be/s2KTYJOU7Yw",
        "skills": ["pd-1-person-business", "pd-ikigai-pro"]
    },
    {
        "id": "p0Fw_xGIWpE",
        "url": "https://youtu.be/p0Fw_xGIWpE",
        "skills": ["pd-1-person-business", "pd-ikigai-pro"]
    }
]

api = YouTubeTranscriptApi()
for v in new_videos:
    vid = v['id']
    url = v['url']
    print(f"Fetching transcript for {vid}...")
    try:
        fetched = api.fetch(vid)
        raw_text = " ".join([item.text for item in fetched])
        
        txt_path = os.path.join(yt_dir, f"{vid}_transcript.txt")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(raw_text)
            
        md_path = os.path.join(yt_dir, f"{vid}_summary.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"""# YouTube Video Ingestion: {vid}

- **Video ID**: {vid}
- **URL**: [{url}]({url})
- **Transcript Length**: {len(raw_text)} characters / ~{len(raw_text.split())} words

---

## Raw Transcript
{raw_text}
""")
        print(f"  [SUCCESS] {vid}: Extracted ~{len(raw_text.split())} words")
    except Exception as e:
        print(f"  [ERROR] {vid}: {e}")

# 2. Ingest PDF Playbook
pdf_path = os.path.join(out_dir, "The-First-Client-Playbook.pdf")
pdf_md_path = os.path.join(out_dir, "the-first-client-playbook.md")

if os.path.exists(pdf_path):
    print(f"Parsing PDF playbook at {pdf_path}...")
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    extracted_text = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        extracted_text.append(f"### Page {i+1}\n{text}\n")
    
    full_pdf_text = "\n".join(extracted_text)
    with open(pdf_md_path, 'w', encoding='utf-8') as f:
        f.write(f"""# Ingested PDF Playbook: The First Client Playbook

- **Source File**: `The-First-Client-Playbook.pdf`
- **Total Pages**: {num_pages}
- **Extracted Text Length**: {len(full_pdf_text)} characters / ~{len(full_pdf_text.split())} words

---

## Extracted Contents
{full_pdf_text}
""")
    print(f"  [SUCCESS] PDF Playbook extracted: {num_pages} pages, ~{len(full_pdf_text.split())} words saved to {pdf_md_path}")
else:
    print(f"  [ERROR] PDF file not found at {pdf_path}")

print("Ingestion complete.")
