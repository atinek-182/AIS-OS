import os
import subprocess
import shutil

target_dir = r"D:\SecurityOs"
junction_path = r"d:\AI-OS\SecurityOs"
repo_url = "https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git"

print(f"Target Directory: {target_dir}")
print(f"Junction Path: {junction_path}")

# Step 1: Ensure D:\SecurityOs exists and clone repo if needed
if not os.path.exists(target_dir):
    os.makedirs(target_dir, exist_ok=True)

if not os.path.exists(os.path.join(target_dir, ".git")):
    print("Cloning repository into D:\\SecurityOs...")
    res = subprocess.run(["git", "clone", repo_url, target_dir], capture_output=True, text=True)
    print("Git Clone stdout:", res.stdout)
    print("Git Clone stderr:", res.stderr)
    print("Git Clone returncode:", res.returncode)
else:
    print("Repository already cloned in D:\\SecurityOs.")

# Step 2: Create Junction Link d:\AI-OS\SecurityOs -> D:\SecurityOs
if not os.path.exists(junction_path):
    print("Creating junction link...")
    res_j = subprocess.run(["cmd", "/c", "mklink", "/J", junction_path, target_dir], capture_output=True, text=True)
    print("MKLINK stdout:", res_j.stdout)
    print("MKLINK stderr:", res_j.stderr)

# Step 3: Verify structure
if os.path.exists(junction_path):
    items = os.listdir(junction_path)
    print(f"[OK] Junction link verified! Found {len(items)} top-level items in SecurityOs.")
