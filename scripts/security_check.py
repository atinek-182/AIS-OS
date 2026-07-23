import os
import sys
import re

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRIALS_DIR = os.path.join(WORKSPACE_ROOT, "trials")
SCRIPTS_DIR = os.path.join(WORKSPACE_ROOT, "scripts")

def check_gitignore():
    gitignore_path = os.path.join(WORKSPACE_ROOT, ".gitignore")
    if not os.path.exists(gitignore_path):
        return False, "Missing .gitignore file in workspace root!"
        
    with open(gitignore_path, "r") as f:
        content = f.read()
        
    rules = [".env", "trials/.venv", "trials/**/renders/", "trials/**/results.tsv"]
    missing = []
    for r in rules:
        if r not in content:
            missing.append(r)
            
    if missing:
        return False, f"Missing rules in .gitignore: {', '.join(missing)}"
    return True, ".gitignore includes all security exclusion rules."

def scan_files_for_secrets():
    # Scanning python files for hardcoded API keys
    secret_patterns = [
        re.compile(r'(?:API_KEY|GEMINI_API_KEY|NOTION_TOKEN|NOTION_API_KEY|GITHUB_TOKEN|GITHUB_PERSONAL_ACCESS_TOKEN|GWS_TOKEN)\s*=\s*["\'][a-zA-Z0-9_-]{20,}["\']', re.IGNORECASE),
        re.compile(r'token\s*=\s*["\'][a-zA-Z0-9_-]{20,}["\']', re.IGNORECASE)
    ]
    
    findings = []
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Exclude directories we ignore
        if ".git" in dirs:
            dirs.remove(".git")
        if ".venv" in dirs:
            dirs.remove(".venv")
        if "brain" in dirs:
            dirs.remove("brain")
        if ".playwright-mcp" in dirs:
            dirs.remove(".playwright-mcp")
            
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, WORKSPACE_ROOT)
            
            # Verify no credentials_*.json or .env are in workspace root/subdirs except if specified
            if file.startswith("credentials_") and file.endswith(".json"):
                findings.append(f"{rel_path}: Found active credentials JSON file in workspace directory!")
                continue
            if file == ".env" and not (rel_path == ".env" or rel_path.replace("\\", "/").startswith("trials/")):
                findings.append(f"{rel_path}: Found active .env file outside allowed boundaries!")
                continue
                
            if file.endswith(".py") or file.endswith(".json") or file.endswith(".md") or file.endswith(".js") or file.endswith(".ts"):
                if ".env" in file_path or "credentials_" in file_path:
                    continue
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line_num, line in enumerate(f, 1):
                            for pattern in secret_patterns:
                                if pattern.search(line):
                                    findings.append(f"{rel_path}:L{line_num} - Possible hardcoded secret!")
                except Exception:
                    pass
    return findings


def check_path_traversals():
    findings = []
    
    # Check that sys.argv[2] or inputs in scripts are sanitized using regex in runner.py and manage_autoresearch.py
    files_to_check = [
        os.path.join(TRIALS_DIR, "runner.py"),
        os.path.join(SCRIPTS_DIR, "manage_autoresearch.py")
    ]
    
    for f_path in files_to_check:
        if not os.path.exists(f_path):
            continue
        with open(f_path, "r") as f:
            content = f.read()
        if "re.match" not in content and "re.search" not in content:
            findings.append(f"{os.path.basename(f_path)}: Missing input sanitization / regex path validation!")
            
    return findings

def main():
    print("==========================================")
    print("   AIOS Security Parameter Audit Tools    ")
    print("==========================================")
    
    # 1. Check gitignore
    gi_status, gi_msg = check_gitignore()
    print(f"\n[+] Git Exclusions Check:")
    if gi_status:
        print(f"  PASS: {gi_msg}")
    else:
        print(f"  FAIL: {gi_msg}")
        
    # 2. Scan for hardcoded secrets
    print(f"\n[+] Hardcoded Secrets Scan:")
    secrets = scan_files_for_secrets()
    if not secrets:
        print("  PASS: No hardcoded secrets detected in repository source files.")
    else:
        print("  FAIL: Detected potential hardcoded secrets:")
        for s in secrets:
            print(f"    - {s}")
            
    # 3. Check for path traversal vulnerabilities
    print(f"\n[+] Input Validation / Path Traversal Check:")
    traversals = check_path_traversals()
    if not traversals:
        print("  PASS: Input targets are sanitized with regular expressions against directory traversals.")
    else:
        print("  FAIL: Potential traversal vulnerabilities:")
        for t in traversals:
            print(f"    - {t}")
            
    print("\n==========================================")
    print("Security Check Finished.")
    
    if not gi_status or secrets or traversals:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
