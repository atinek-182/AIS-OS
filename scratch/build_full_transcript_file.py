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

timestamp_pattern = re.compile(r'(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> (\d{2}):(\d{2}):(\d{2})\.(\d{3})')

entries = []
current_start = 0
current_end = 0

for i, line in enumerate(lines):
    match = timestamp_pattern.search(line)
    if match:
        h1, m1, s1, _ = map(int, match.groups()[:4])
        current_start = h1 * 3600 + m1 * 60 + s1
    elif line.strip() and not line.startswith('WEBVTT') and not line.startswith('Kind:') and not line.startswith('Language:'):
        cleaned = clean_vtt_line(line)
        if cleaned and (not entries or entries[-1][1] != cleaned):
            entries.append((current_start, cleaned))

output_file = r'd:\AI-OS\references\six-file-context-methodology\FULL_TRANSCRIPT.md'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('# Full Video Transcript: How Senior Engineers Actually Build With AI in 2026\n\n')
    f.write('**Video Title**: How Senior Engineers Actually Build With AI in 2026 | Build a Full Stack Systems Architecture App\n')
    f.write('**Uploader**: JavaScript Mastery (Adrian Hajdin)\n')
    f.write('**Duration**: 3 hours 58 minutes 17 seconds (14,297 seconds)\n\n')
    f.write('---\n\n')
    
    current_ch_index = -1
    
    for t, txt in entries:
        # Check if chapter changed
        ch_title = "Intro"
        ch_obj = None
        for idx, ch in enumerate(chapters):
            if ch['start_time'] <= t <= ch['end_time']:
                ch_title = ch.get('title')
                ch_obj = ch
                if idx != current_ch_index:
                    current_ch_index = idx
                    h = int(ch['start_time']) // 3600
                    m = (int(ch['start_time']) % 3600) // 60
                    s = int(ch['start_time']) % 60
                    f.write(f'\n\n## Chapter {idx+1:02d}: {ch_title} ({h:02d}:{m:02d}:{s:02d})\n\n')
                break
        
        h_t = t // 3600
        m_t = (t % 3600) // 60
        s_t = t % 60
        f.write(f'[{h_t:02d}:{m_t:02d}:{s_t:02d}] {txt}\n')

print(f"Full transcript written to {output_file}")
