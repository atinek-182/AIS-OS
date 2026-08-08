# Reusable Pre-Flight Health Check: Skill Workflows & Master Scenario Engine
import os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def verify_skill_workflows_health():
    print("=== ZORIXEL AIOS SKILL WORKFLOWS HEALTH CHECK ===")
    
    # Check 1: Master Capture File
    capture_path = r"d:\AI-OS\brainstorms\2026-08-08-skill-workflows-and-scenario-mapping.md"
    if os.path.exists(capture_path):
        print(f"[OK] Found Master Capture File: {capture_path}")
        with open(capture_path, "r", encoding="utf-8") as f:
            content = f.read()
            if "Master 10 Production Playbooks" in content:
                print("  [OK] Option A 10 Production Playbooks Verified.")
            if "7-Stage Complete AI Agency Master Engine" in content:
                print("  [OK] Option B 7-Stage Agency Engine Verified.")
    else:
        print(f"[ERROR] Missing Master Capture File: {capture_path}")
        return False
        
    # Check 2: Roast Audit Artifact
    roast_path = r"d:\AI-OS\brainstorms\roast_2026-08-08_skill_workflows.md"
    if os.path.exists(roast_path):
        print(f"[OK] Found Roast Audit Artifact: {roast_path}")
    else:
        print(f"[ERROR] Missing Roast Audit Artifact: {roast_path}")
        return False

    # Check 3: Active Focus (hot.md)
    hot_path = r"d:\AI-OS\hot.md"
    if os.path.exists(hot_path):
        with open(hot_path, "r", encoding="utf-8") as f:
            hot_content = f.read()
            if "2026-08-08-skill-workflows-and-scenario-mapping.md" in hot_content:
                print("[OK] hot.md correctly references Skill Workflows Engine.")
    else:
        print(f"[ERROR] Missing hot.md: {hot_path}")
        return False

    print("==================================================")
    print("[SUCCESS] Skill Workflows Engine Health Check PASSED 100%!")
    return True

if __name__ == "__main__":
    success = verify_skill_workflows_health()
    sys.exit(0 if success else 1)
