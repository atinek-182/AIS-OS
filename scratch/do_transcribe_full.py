import os
import sys

# Ensure site-packages and ffmpeg PATH are loaded
user_site = os.path.expanduser(r"~\AppData\Roaming\Python\Python314\site-packages")
user_scripts = os.path.expanduser(r"~\AppData\Roaming\Python\Python314\Scripts")
if user_site not in sys.path:
    sys.path.insert(0, user_site)

import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)
os.environ["PATH"] = ffmpeg_dir + os.path.pathsep + user_scripts + os.path.pathsep + os.environ.get("PATH", "")

# Ensure a copy named ffmpeg.exe exists in ffmpeg_dir
ffmpeg_target = os.path.join(ffmpeg_dir, "ffmpeg.exe")
if not os.path.exists(ffmpeg_target) and os.path.exists(ffmpeg_exe):
    import shutil
    try:
        shutil.copyfile(ffmpeg_exe, ffmpeg_target)
        print("Copied ffmpeg.exe to", ffmpeg_target)
    except Exception as e:
        print("Copy ffmpeg warning:", e)

import whisper

video_path = r"C:\Users\HP\Videos\2026-08-06 13-09-14.mp4"
print(f"Transcribing video: {video_path}")
print("Loading Whisper model ('base')...")

model = whisper.load_model("base")
print("Model loaded successfully. Starting transcription...")

result = model.transcribe(video_path, verbose=False)

transcript_text = result.get("text", "").strip()
language = result.get("language", "unknown")

print(f"\nLanguage detected: {language}\n")
print("="*60)
print("FULL TRANSCRIPT:")
print("="*60)
print(transcript_text)
print("="*60)

# Save text
output_txt = r"d:\AI-OS\scratch\transcript.txt"
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(f"Language: {language}\n\n" + transcript_text)

# Save timestamped segments
output_ts = r"d:\AI-OS\scratch\transcript_timestamps.txt"
with open(output_ts, "w", encoding="utf-8") as f:
    f.write(f"Language: {language}\n\n")
    for seg in result.get("segments", []):
        start = seg['start']
        end = seg['end']
        text = seg['text'].strip()
        f.write(f"[{start:06.2f}s -> {end:06.2f}s] {text}\n")

print(f"\nSaved transcript to: {output_txt}")
print(f"Saved timestamps to: {output_ts}")
