import shutil
import subprocess

print("winget path:", shutil.which("winget"))
print("pip path:", shutil.which("pip"))

# test running winget --version
try:
    res = subprocess.run(["winget", "--version"], capture_output=True, text=True, timeout=5)
    print("winget version:", res.stdout.strip())
except Exception as e:
    print("winget error:", e)

# test running pip list
try:
    res = subprocess.run(["pip", "list"], capture_output=True, text=True, timeout=5)
    print("pip packages count:", len(res.stdout.splitlines()))
    for line in res.stdout.splitlines():
        if any(pkg in line.lower() for pkg in ['torch', 'whisper', 'ffmpeg', 'speech', 'audio', 'moviepy', 'pydub', 'openai']):
            print("  -", line)
except Exception as e:
    print("pip error:", e)
