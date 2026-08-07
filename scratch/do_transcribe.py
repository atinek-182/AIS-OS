import os
import sys

# Add user site-packages to sys.path
user_site = os.path.expanduser(r"~\AppData\Roaming\Python\Python314\site-packages")
if user_site not in sys.path:
    sys.path.insert(0, user_site)

import imageio_ffmpeg
import whisper

# Ensure ffmpeg binary from imageio_ffmpeg is available in PATH for whisper
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)
os.environ["PATH"] = ffmpeg_dir + os.path.pathsep + os.environ.get("PATH", "")

# Create alias or symlink if needed so whisper finds 'ffmpeg'
target_ffmpeg = os.path.join(ffmpeg_dir, "ffmpeg.exe")
if not os.path.exists(target_ffmpeg) and os.path.exists(ffmpeg_exe):
    import shutil
    try:
        shutil.copyfile(ffmpeg_exe, target_ffmpeg)
    except Exception as e:
        print("Copy ffmpeg warning:", e)

video_path = r"C:\Users\HP\Videos\2026-08-06 13-09-14.mp4"
print(f"Transcribing video: {video_path}")
print("Loading Whisper model...")

model = whisper.load_model("base")
print("Model loaded. Running transcription...")

result = model.transcribe(video_path, verbose=True)

transcript_text = result.get("text", "")
print("\n" + "="*50)
print("TRANSCRIPTION RESULTS:")
print("="*50 + "\n")
print(transcript_text)

output_txt = r"d:\AI-OS\scratch\transcript.txt"
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(transcript_text)

print(f"\nTranscript saved to {output_txt}")

# Save detailed segments with timestamps
output_segments = r"d:\AI-OS\scratch\transcript_timestamps.txt"
with open(output_segments, "w", encoding="utf-8") as f:
    for seg in result.get("segments", []):
        start = seg['start']
        end = seg['end']
        text = seg['text']
        line = f"[{start:.2f}s -> {end:.2f}s] {text}\n"
        f.write(line)

print(f"Timestamped transcript saved to {output_segments}")
