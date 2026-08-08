import os
import sys
import json
import subprocess
import shutil

# Force UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

root_dir = r"d:\AI-OS"
health_log_dir = os.path.join(root_dir, "audits", "health-logs")
os.makedirs(health_log_dir, exist_ok=True)
health_log_file = os.path.join(health_log_dir, "gws-health.json")

# Credentials paths
cred_personal = r"C:\Users\HP\.config\gws\credentials_personal.json"
cred_brand = r"C:\Users\HP\.config\gws\credentials_brand.json"
gws_cli_js = r"C:\Users\HP\AppData\Roaming\npm\node_modules\@googleworkspace\cli\run.js"

def check_file(path, label):
    exists = os.path.exists(path)
    print(f"[{'OK' if exists else 'WARNING'}] {label} -> {path}")
    return exists

def run_gws_check(cred_file, context_name):
    print(f"\n--- Checking GWS OAuth Health ({context_name}) ---")
    if not os.path.exists(cred_file):
        print(f"[ERROR] Credential file missing: {cred_file}")
        return {"status": "MISSING_CREDENTIAL", "context": context_name, "error": "File not found"}

    env = os.environ.copy()
    env["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = cred_file
    
    # Resolve Node execution per Rule 1.2 & Rule 1.20
    node_bin = shutil.which("node") or "node"
    cmd = [node_bin, gws_cli_js, "auth", "status"] if os.path.exists(gws_cli_js) else ["gws", "auth", "status"]

    try:
        res = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            timeout=10,
            encoding="utf-8",
            errors="replace"
        )
        output = res.stdout + res.stderr
        
        if "invalid_grant" in output.lower():
            print(f"[RECOVERABLE ERROR] GWS Refresh Token Expired for {context_name}!")
            print("Action Required: Execute `node run.js auth login` to re-authenticate.")
            return {"status": "EXPIRED_TOKEN", "context": context_name, "reauth_cmd": "node run.js auth login"}
            
        elif "accessnotconfigured" in output.lower():
            print(f"[API ERROR] GCP Service API not enabled for {context_name}!")
            print("Action Required: Enable API at https://console.developers.google.com/apis/")
            return {"status": "API_NOT_ENABLED", "context": context_name, "url": "https://console.developers.google.com/apis/"}
            
        elif res.returncode == 0 or "authenticated" in output.lower() or "logged in" in output.lower():
            print(f"[OK] GWS OAuth Status Healthy for {context_name}")
            return {"status": "HEALTHY", "context": context_name}
        else:
            print(f"[INFO] GWS Check Output ({context_name}): {output.strip()[:200]}")
            return {"status": "ACTIVE_CHECKED", "context": context_name, "details": output.strip()[:200]}
            
    except Exception as e:
        print(f"[ERROR] Subprocess error during GWS health check: {e}")
        return {"status": "CHECK_FAILED", "context": context_name, "error": str(e)}

def main():
    print("==================================================")
    print(" ZORIXEL AIOS: PRE-FLIGHT GWS OAUTH HEALTH GUARD ")
    print("==================================================")
    
    c1 = check_file(cred_personal, "Personal GWS Credentials")
    c2 = check_file(cred_brand, "Brand GWS Credentials")
    
    r1 = run_gws_check(cred_personal, "Personal Account") if c1 else {"status": "NO_FILE"}
    r2 = run_gws_check(cred_brand, "Brand Account") if c2 else {"status": "NO_FILE"}
    
    health_data = {
        "timestamp": os.popen("date /t").read().strip() if os.name == 'nt' else "2026-08-07",
        "personal": r1,
        "brand": r2,
        "overall_status": "HEALTHY" if r1.get("status") in ["HEALTHY", "ACTIVE_CHECKED"] and r2.get("status") in ["HEALTHY", "ACTIVE_CHECKED"] else "ATTENTION_REQUIRED"
    }
    
    with open(health_log_file, "w", encoding="utf-8") as f:
        json.dump(health_data, f, indent=2)
        
    print(f"\n[OK] Health report saved to: {health_log_file}")
    print("==================================================")

if __name__ == "__main__":
    main()
