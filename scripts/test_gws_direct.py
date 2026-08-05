import subprocess
import json
import shutil
import sys

def main():
    gws_path = shutil.which("gws")
    print(f"Resolved gws path: {gws_path}")
    
    payload = {"properties": {"title": "Vashishthya-01Master-OS"}}
    payload_str = json.dumps(payload)
    
    res = subprocess.run([gws_path, "sheets", "spreadsheets", "create", "--json", payload_str], capture_output=True, text=True, shell=False)
    
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    print("Return code:", res.returncode)

if __name__ == "__main__":
    main()
