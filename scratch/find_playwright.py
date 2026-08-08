import os

root_dir = r"d:\AI-OS"

print("Searching for node_modules containing playwright...")
for current_root, dirs, files in os.walk(root_dir):
    if "node_modules" in dirs:
        nm_path = os.path.join(current_root, "node_modules")
        pw_path = os.path.join(nm_path, "playwright")
        if os.path.exists(pw_path):
            print(f"[FOUND] Playwright node_modules at: {nm_path}")
