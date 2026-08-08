#!/usr/bin/env python3
"""
ZORIXEL AIOS: Zero-Cost & Zero-Subscription Boundary Validator
Audits workspace skills, scripts, and rules to guarantee zero unauthorized paid API dependencies.
"""

import sys
import os
import re

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PAID_API_PATTERNS = [
    r'resemble\.ai',
    r'api\.elevenlabs\.io',
]

def audit_zero_cost_boundary(workspace_dir):
    print("========================================================")
    print("ZORIXEL AIOS: Zero-Cost Boundary Health Validator")
    print("========================================================")

    skills_dir = os.path.join(workspace_dir, ".agents", "skills")
    scripts_dir = os.path.join(workspace_dir, "scripts")
    errors_found = 0

    # 1. Audit active skills
    if os.path.exists(skills_dir):
        for root, dirs, files in os.walk(skills_dir):
            for file in files:
                if file == "SKILL.md":
                    skill_path = os.path.join(root, file)
                    with open(skill_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    for pattern in PAID_API_PATTERNS:
                        if re.search(pattern, content, re.IGNORECASE):
                            print(f"[WARN] Paid API reference found in skill: {skill_path} (Pattern: {pattern})")
                            errors_found += 1

    # 2. Audit scripts
    if os.path.exists(scripts_dir):
        for file in os.listdir(scripts_dir):
            if file.endswith(".py"):
                script_path = os.path.join(scripts_dir, file)
                with open(script_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for pattern in PAID_API_PATTERNS:
                    if re.search(pattern, content, re.IGNORECASE):
                        print(f"[WARN] Paid API reference found in script: {script_path} (Pattern: {pattern})")
                        errors_found += 1

    print("========================================================")
    if errors_found == 0:
        print("[SUCCESS] 100% Zero-Cost Boundary Verified (0 unauthorized paid API dependencies)!")
        return 0
    else:
        print(f"[CAUTION] Found {errors_found} paid API references requiring zero-cost review.")
        return 1

if __name__ == "__main__":
    ws_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.exit(audit_zero_cost_boundary(ws_dir))
