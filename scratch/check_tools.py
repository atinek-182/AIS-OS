import shutil
import sys
import subprocess

print("Python version:", sys.version)

tools = ["ffmpeg", "ffprobe", "whisper", "yt-dlp", "node"]
for t in tools:
    path = shutil.which(t)
    print(f"Tool {t}: {path}")

# Check python packages
packages = ["whisper", "faster_whisper", "speech_recognition", "google.generativeai", "openai", "groq", "pydub", "moviepy", "torch"]
for pkg in packages:
    try:
        __import__(pkg)
        print(f"Package {pkg}: INSTALLED")
    except ImportError:
        print(f"Package {pkg}: NOT installed")
