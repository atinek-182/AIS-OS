import subprocess

print("Launching gws auth login...")
subprocess.run(["gws", "auth", "login"], shell=True)
