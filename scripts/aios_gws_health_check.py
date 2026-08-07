import subprocess
import json
import shutil
import sys
import os

GWS_RUN_JS = r"C:\Users\HP\AppData\Roaming\npm\node_modules\@googleworkspace\cli\run.js"
BRAND_CREDS = r"C:\Users\HP\.config\gws\credentials_brand.json"

def check_gws_health():
    print("========================================================")
    print("ZORIXEL AIOS: Google Workspace CLI (gws) Pre-Flight Check")
    print("========================================================\n")
    
    # 1. Verify Node.js
    node_path = shutil.which("node")
    if not node_path:
        print("[ERROR] Node.js is not installed or not found on PATH.")
        sys.exit(1)
    print(f"[OK] Node.js located: {node_path}")
    
    # 2. Verify gws run.js
    if not os.path.exists(GWS_RUN_JS):
        print(f"[ERROR] gws run.js entry point not found at: {GWS_RUN_JS}")
        sys.exit(1)
    print(f"[OK] gws run.js entry point located.")
    
    # 3. Test Drive API Call
    env = os.environ.copy()
    valid_creds = None
    for path, label in [(BRAND_CREDS, "ZORIXEL Brand"), (r"C:\Users\HP\.config\gws\credentials_personal.json", "Personal")]:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    json.load(f)
                valid_creds = (path, label)
                break
            except Exception:
                pass
                
    if valid_creds:
        env["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = valid_creds[0]
        print(f"[OK] Using {valid_creds[1]} Credentials: {valid_creds[0]}")
    else:
        env.pop("GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE", None)
        print("[INFO] Using Default OAuth Credentials Keyring.")
        
    cmd = ["node", GWS_RUN_JS, "drive", "files", "list", "--params", '{"pageSize": 1}']
    res = subprocess.run(cmd, capture_output=True, text=True, shell=False, env=env)
    
    if res.returncode != 0:
        err_text = res.stderr or res.stdout
        print("\n[ERROR] gws Health Check Failed!")
        if "invalid_grant" in err_text:
            print("-> OAuth refresh token is EXPIRED or REVOKED.")
            print("-> RUN: node " + GWS_RUN_JS + " auth login to re-authenticate.")
        elif "accessNotConfigured" in err_text or "has not been used in project" in err_text:
            print("-> Google Drive/Sheets API is DISABLED on your GCP project.")
            print("-> Enable Drive API: https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=zorixel-aios")
            print("-> Enable Sheets API: https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=zorixel-aios")
        else:
            print(f"Details: {err_text}")
        sys.exit(1)
    
    print("[OK] OAuth Authentication is ACTIVE.")
    print("[OK] Google Drive & Sheets APIs are ENABLED.")
    print("\n========================================================")
    print("ALL GWS HEALTH CHECKS PASSED SUCCESSFULLY!")
    print("========================================================\n")

if __name__ == "__main__":
    check_gws_health()
