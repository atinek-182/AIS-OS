#!/usr/bin/env python
import os
import sys
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def test_health():
    print("=== SecurityOs Health & Pre-Flight Check ===")
    
    # 1. Verify SecurityOs directory & skills
    security_os_dir = r"d:\AI-OS\SecurityOs"
    skills_dir = os.path.join(security_os_dir, "skills")
    
    if not os.path.exists(security_os_dir):
        print("[FAIL] SecurityOs directory missing at", security_os_dir)
        sys.exit(1)
    else:
        print("[OK] SecurityOs directory exists.")
        
    if not os.path.exists(skills_dir):
        print("[FAIL] SecurityOs skills directory missing at", skills_dir)
        sys.exit(1)
    else:
        skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
        print(f"[OK] Found {len(skills)} cybersecurity skills in SecurityOs.")
        
    # 2. Test CLI search
    runner_script = r"d:\AI-OS\scripts\security_os_runner.py"
    res = subprocess.run([sys.executable, runner_script, "search", "prompt injection"], capture_output=True, text=True)
    if res.returncode == 0 and "Matches:" in res.stdout:
        print("[OK] SecurityOs CLI search functional.")
    else:
        print("[FAIL] SecurityOs CLI search failed:", res.stderr)
        sys.exit(1)

    # 3. Test Export
    res_exp = subprocess.run([sys.executable, runner_script, "export", "--target", "antigravity"], capture_output=True, text=True)
    if res_exp.returncode == 0 and "[SUCCESS]" in res_exp.stdout:
        print("[OK] SecurityOs Multi-Agent Exporter functional.")
    else:
        print("[FAIL] SecurityOs Exporter failed:", res_exp.stderr)
        sys.exit(1)
        
    print("\n[SUCCESS] SecurityOs is 100% HEALTHY and READY!")

if __name__ == "__main__":
    test_health()
