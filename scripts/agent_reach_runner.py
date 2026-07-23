# -*- coding: utf-8 -*-
"""Agent Reach AIOS Runner & Diagnostic Helper

Invokes agent-reach CLI or native module checks from local AIOS environment.
"""

import os
import shutil
import subprocess
import sys

# Ensure user Python scripts & GitHub CLI directories are in PATH for executable resolution
PATHS_TO_ADD = [
    os.path.expanduser(r"~\AppData\Roaming\Python\Python314\Scripts"),
    r"C:\Program Files\GitHub CLI",
]

for p in PATHS_TO_ADD:
    if os.path.exists(p) and p not in os.environ.get("PATH", ""):
        os.environ["PATH"] = p + os.path.pathsep + os.environ.get("PATH", "")

def run_doctor():
    """Execute health check across all registered channels."""
    env = os.environ.copy()
    # Unset stale GITHUB_TOKEN so gh CLI uses authenticated keyring account (atinek-182)
    env.pop("GITHUB_TOKEN", None)
    env.pop("GH_TOKEN", None)

    agent_reach_bin = shutil.which("agent-reach")
    if not agent_reach_bin:
        fallback = os.path.expanduser(r"~\AppData\Roaming\Python\Python314\Scripts\agent-reach.exe")
        if os.path.exists(fallback):
            agent_reach_bin = fallback

    if agent_reach_bin:
        subprocess.run([agent_reach_bin, "doctor"], check=False, env=env)
        return

    try:
        from agent_reach.config import Config
        from agent_reach.doctor import check_all, format_report

        config = Config()
        results = check_all(config)
        report = format_report(results)
        print(report)
    except Exception as e:
        print(f"Agent Reach Status Error: {e}")
        print("To install Agent Reach CLI globally, run:")
        print("  pip install https://github.com/Panniantong/agent-reach/archive/main.zip")
        print("  agent-reach install --env=auto")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "doctor"
    if cmd == "doctor":
        run_doctor()
    else:
        print(f"Unknown command: {cmd}. Usage: python agent_reach_runner.py doctor")
