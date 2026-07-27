import json

with open('scratch/yt_meta.json', 'r', encoding='utf-8') as f:
    meta = json.load(f)

print('TITLE:', meta['title'])
print('DURATION:', meta['duration'])
print('\nCHAPTERS:')
chapters = meta.get('chapters') or []
if not chapters:
    print('No chapters found in metadata.')
else:
    for i, ch in enumerate(chapters):
        st = int(ch['start_time'])
        et = int(ch['end_time'])
        h = st // 3600
        m = (st % 3600) // 60
        s = st % 60
        title = ch.get('title')
        print(f'{i+1:02d}. [{st}s - {et}s] ({h:02d}:{m:02d}:{s:02d}) {title}')
