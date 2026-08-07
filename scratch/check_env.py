import os
import shutil

keys = [k for k in os.environ if any(term in k.upper() for term in ['KEY', 'TOKEN', 'API', 'GEMINI', 'OPENAI', 'GROQ', 'WHISPER', 'DEEPGRAM', 'ASSEMBLY'])]
print("Relevant Env Vars:", keys)

for k in keys:
    val = os.environ[k]
    # mask sensitive parts
    masked = val[:6] + "..." + val[-4:] if len(val) > 10 else "***"
    print(f"  {k} = {masked}")

# Check PATH entries for ffmpeg
path_dirs = os.environ.get("PATH", "").split(os.path.pathsep)
for p in path_dirs:
    if os.path.exists(p):
        for f in os.listdir(p):
            if "ffmpeg" in f.lower() or "whisper" in f.lower():
                print(f"Found in PATH ({p}): {f}")
