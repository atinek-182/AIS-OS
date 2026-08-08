import os
import subprocess

root_dir = r"d:\AI-OS"

def check_secrets_hygiene():
    print("=== STEP 2: SECRETS HYGIENE & VIBESEC AUDIT ===")
    modified_files = [
        os.path.join(root_dir, "GEMINI.md"),
        os.path.join(root_dir, "AGENTS.md"),
        os.path.join(root_dir, "context", "00_MASTER_INDEX.md"),
        os.path.join(root_dir, "scripts", "aios_deep_search.py"),
        os.path.join(root_dir, "scripts", "aios_bootup_context.py"),
        os.path.join(root_dir, "scripts", "aios_gws_health_check.py"),
        os.path.join(root_dir, "scripts", "aios_memory_compact.py"),
        os.path.join(root_dir, "scripts", "verify_design_milestone.py"),
    ]
    
    secret_patterns = ["AIzaSy", "sk-proj-", "secret_", "ntn_"]
    exposed = []
    
    for fpath in modified_files:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for sp in secret_patterns:
                if sp in content:
                    exposed.append((fpath, sp))
                    
    if exposed:
        print(f"[WARNING] Potential secrets found: {exposed}")
    else:
        print("[OK] Secrets Hygiene Clean! Zero hardcoded API keys found in modified files.")

def main():
    check_secrets_hygiene()

if __name__ == "__main__":
    main()
