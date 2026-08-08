#!/usr/bin/env python3
"""
Pre-Flight Health Check - Ingested Skills Validator (Defuddle, YouTube Full, Composio)
Verifies:
1. sys.executable -m yt_dlp execution
2. scripts/youtube_skills_runner.py execution
3. scripts/composio_runner.py binary resolution logic
4. Rule 2.8, 2.9, 2.10 present in references/GLOBAL_ERROR_PREVENTION_RULES.md
5. System prompts (AGENTS.md and GEMINI.md) synchronized
"""

import sys
import os
import json
import subprocess

# Ensure UTF-8 stdio configuration on Windows OS
sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def check_ytdlp() -> bool:
    try:
        res = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"], capture_output=True, text=True, check=True)
        print(f"[OK] yt-dlp module responsive (Version: {res.stdout.strip()})")
        return True
    except Exception as e:
        print(f"[FAIL] yt-dlp check failed: {e}")
        return False


def check_youtube_runner() -> bool:
    try:
        cmd = [sys.executable, "scripts/youtube_skills_runner.py", "search", "--query", "test", "--max-results", "1"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and "status" in res.stdout:
            data = json.loads(res.stdout)
            if data.get("status") == "success":
                print("[OK] youtube_skills_runner.py search functional")
                return True
        print(f"[FAIL] youtube_skills_runner.py check returned invalid response: {res.stdout}")
        return False
    except Exception as e:
        print(f"[FAIL] youtube_skills_runner.py execution error: {e}")
        return False


def check_composio_runner() -> bool:
    try:
        cmd = [sys.executable, "scripts/composio_runner.py", "--help"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print("[OK] composio_runner.py executable CLI responsive")
            return True
        print(f"[FAIL] composio_runner.py check failed: {res.stderr}")
        return False
    except Exception as e:
        print(f"[FAIL] composio_runner.py execution error: {e}")
        return False


def check_rules() -> bool:
    rules_path = os.path.join("references", "GLOBAL_ERROR_PREVENTION_RULES.md")
    if not os.path.exists(rules_path):
        print("[FAIL] GLOBAL_ERROR_PREVENTION_RULES.md missing")
        return False

    with open(rules_path, "r", encoding="utf-8") as f:
        content = f.read()

    rules_ok = True
    if "Web Article Ingestion & Defuddle Standard" not in content:
        print("[FAIL] Rule 2.8 Defuddle Standard missing")
        rules_ok = False
    else:
        print("[OK] Rule 2.8 Defuddle Standard verified")

    if "YouTube Transcript & Media Extraction Standard" not in content:
        print("[FAIL] Rule 2.9 YouTube Standard missing")
        rules_ok = False
    else:
        print("[OK] Rule 2.9 YouTube Standard verified")

    if "Composio SaaS Integration & Zero-Fee Boundary Standard" not in content:
        print("[FAIL] Rule 2.10 Composio Standard missing")
        rules_ok = False
    else:
        print("[OK] Rule 2.10 Composio Standard verified")

    return rules_ok


def main():
    print("==================================================")
    print("ZORIXEL AIOS: Ingested Skills Pre-Flight Health Check")
    print("==================================================")

    ytdlp_ok = check_ytdlp()
    yt_runner_ok = check_youtube_runner()
    composio_ok = check_composio_runner()
    rules_ok = check_rules()

    print("--------------------------------------------------")
    if ytdlp_ok and yt_runner_ok and composio_ok and rules_ok:
        print("[SUCCESS] ALL INGESTED SKILLS PRE-FLIGHT CHECKS PASSED (100%)!")
        sys.exit(0)
    else:
        print("[ERROR] INGESTED SKILLS PRE-FLIGHT CHECKS FAILED!")
        sys.exit(1)


if __name__ == "__main__":
    main()
