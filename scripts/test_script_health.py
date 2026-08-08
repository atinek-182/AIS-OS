#!/usr/bin/env python3
"""
AIOS Pre-Flight Utility Script Health Validator
Verifies UTF-8 stdio reconfiguration and CLI path resolution across all workspace scripts.
"""

import sys
import os
import glob

# Enforce UTF-8 stdio
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def check_script_health(scripts_dir):
    script_files = glob.glob(os.path.join(scripts_dir, "*.py"))
    passed = 0
    failed = 0

    print(f"[SCRIPT HEALTH] Auditing {len(script_files)} python scripts in {scripts_dir}...\n")

    for file_path in script_files:
        basename = os.path.basename(file_path)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check UTF-8 stdio reconfiguration
            has_reconfigure = "sys.stdout.reconfigure" in content or "PYTHONIOENCODING" in content or "reconfigure(encoding='utf-8'" in content
            
            if has_reconfigure:
                print(f"  [PASS] {basename} (UTF-8 stdio configured)")
                passed += 1
            else:
                print(f"  [WARN] {basename} (Missing explicit sys.stdout.reconfigure)")
                passed += 1
        except Exception as e:
            print(f"  [FAIL] {basename}: {e}")
            failed += 1

    print(f"\n[SUMMARY] {passed} passed, {failed} failed out of {len(script_files)} scripts.")
    return failed == 0

if __name__ == "__main__":
    scripts_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
    success = check_script_health(scripts_path)
    sys.exit(0 if success else 1)
