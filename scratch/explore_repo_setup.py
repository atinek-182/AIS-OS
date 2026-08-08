import os
import json
import subprocess

def check_file(path):
    return os.path.exists(path)

results = {
    "git_config_exists": check_file(".git/config"),
    "agents_md": check_file("AGENTS.md"),
    "claude_md": check_file("CLAUDE.md"),
    "context_md": check_file("CONTEXT.md"),
    "context_map_md": check_file("CONTEXT-MAP.md"),
    "docs_adr": check_file("docs/adr"),
    "docs_agents": check_file("docs/agents"),
    "scratch_dir": check_file(".scratch"),
    "triage_installed": check_file(".agents/skills/triage") or check_file("C:/Users/HP/.gemini/config/skills/triage"),
    "monorepo_pnpm": check_file("pnpm-workspace.yaml"),
    "monorepo_pkg": False,
}

if check_file("package.json"):
    try:
        with open("package.json", "r", encoding="utf-8") as f:
            pkg = json.load(f)
            if "workspaces" in pkg:
                results["monorepo_pkg"] = True
    except Exception as e:
        results["package_json_err"] = str(e)

# git remote
try:
    remote = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, cwd="d:/AI-OS")
    results["git_remote"] = remote.stdout.strip()
except Exception as e:
    results["git_remote_err"] = str(e)

print(json.dumps(results, indent=2))
