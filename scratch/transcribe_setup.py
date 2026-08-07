import subprocess
import sys

def install_and_run():
    print("Installing imageio-ffmpeg and openai-whisper...")
    subprocess.run([sys.executable, "-m", "pip", "install", "imageio-ffmpeg", "openai-whisper"], check=True)
    print("Installation complete.")

if __name__ == "__main__":
    install_and_run()
