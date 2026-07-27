import json
import re

with open('scratch/yt_meta.json', 'r', encoding='utf-8') as f:
    meta = json.load(f)

chapters = meta.get('chapters') or []

def clean_vtt_line(text):
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

with open('scratch/yt_captions.en.vtt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

blocks = []
current_time = 0
buffer = []

timestamp_pattern = re.compile(r'(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> (\d{2}):(\d{2}):(\d{2})\.(\d{3})')

for line in lines:
    match = timestamp_pattern.search(line)
    if match:
        h, m, s, _ = map(int, match.groups()[:4])
        current_time = h * 3600 + m * 60 + s
    elif line.strip() and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:'):
        cleaned = clean_vtt_line(line)
        if cleaned and (not buffer or buffer[-1] != cleaned):
            buffer.append((current_time, cleaned))

# Deduplicate consecutive lines
deduped = []
for t, txt in buffer:
    if not deduped or deduped[-1][1] != txt:
        deduped.append((t, txt))

# Map deduped transcript to chapters
chapter_transcript = {ch['title']: [] for ch in chapters}
if not chapters:
    chapter_transcript['Full Video'] = deduped
else:
    for t, txt in deduped:
        # find matching chapter
        matched_title = chapters[0]['title']
        for ch in chapters:
            if ch['start_time'] <= t <= ch['end_time']:
                matched_title = ch['title']
                break
        chapter_transcript[matched_title].append(txt)

# Save structured transcript
with open('scratch/structured_transcript.json', 'w', encoding='utf-8') as f:
    json.dump({title: " ".join(lines) for title, lines in chapter_transcript.items()}, f, indent=2, ensure_ascii=False)

print('Structured transcript created successfully!')
for ch_title, lines in chapter_transcript.items():
    word_count = len(" ".join(lines).split())
    print(f'- {ch_title}: {word_count} words')
