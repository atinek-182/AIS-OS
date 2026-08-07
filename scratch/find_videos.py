import os
import glob
from datetime import datetime

search_dirs = [
    r"C:\Users\HP\Videos",
    r"C:\Users\HP\Downloads",
    r"C:\Users\HP\Desktop",
    r"C:\Users\HP\Documents",
    r"d:\AI-OS",
    r"C:\Users\HP\.gemini",
]

extensions = ['*.mp4', '*.webm', '*.mov', '*.mkv', '*.avi', '*.m4a', '*.wav', '*.mp3', '*.webp']

found = []

for sdir in search_dirs:
    if not os.path.exists(sdir):
        continue
    for ext in extensions:
        # Search top 3 levels deep
        for root, dirs, files in os.walk(sdir):
            # prevent walking too deep into node_modules or .git
            if 'node_modules' in root or '.git' in root or 'venv' in root or '.venv' in root:
                continue
            depth = root.count(os.sep) - sdir.count(os.sep)
            if depth > 4:
                continue
            for file in files:
                if any(file.lower().endswith(ext.replace('*', '')) for ext in extensions):
                    full_path = os.path.join(root, file)
                    try:
                        mtime = os.path.getmtime(full_path)
                        size = os.path.getsize(full_path)
                        found.append((mtime, size, full_path))
                    except Exception:
                        pass

found.sort(key=lambda x: x[0], reverse=True)

print("FOUND FILES:")
for mtime, size, path in found[:25]:
    dt = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    size_mb = size / (1024 * 1024)
    print(f"[{dt}] ({size_mb:.2f} MB) {path}")
