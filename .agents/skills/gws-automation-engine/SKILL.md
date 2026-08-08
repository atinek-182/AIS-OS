---
title: Google Workspace CLI Automation Engine (`/gws-automation-engine`)
domain: skill
summary: This skill manages Google Workspace CLI (`gws`) subprocess operations on Windows OS across Google Drive, Google Sheets,
  Gmail, and Google Calendar. It eliminates Windows batch file resolution errors (`WinError 2`), prevents `cmd.exe` stringified
  JSON
critical_directives:
- NEVER** invoke `gws` through `cmd.exe` or set `shell=True` in Python subprocess calls on Windows OS.
- 'ALWAYS** invoke Node directly targeting the explicit `run.js` entry point:'
- 'Always pass python dictionaries serialized with `json.dumps(payload)` directly in the argument array with `shell=False`:'
- Always set `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` in process environment before subprocess execution.
section_outline:
- Google Workspace CLI Automation Engine (`/gws-automation-engine`)
- Overview & Tri-Mode Execution
- Core Rules & Windows Execution Safeguards
- 🐍 Standard Python Subprocess Execution Boilerplate
- 🧪 Pre-Flight Environment Verification Protocol
read_triggers:
- When working on skill in .agents/skills/gws-automation-engine/SKILL.md
- When reading context for Google Workspace CLI Automation Engine (`/gws-automation-engine`)
tags:
- skill
- SKILL
updated: '2026-08-08'
name: gws-automation-engine
description: Executes Google Workspace CLI (gws) operations for Drive, Sheets, Gmail, and Calendar on Windows OS. Prevents
  cmd.exe quote mangling, manages OAuth refresh tokens, and intercepts GCP API enablement HTTP 403 blocks. Validates environment
  via scripts/aios_gws_health_check.py.
argument-hint: '[resource] [action] [params]'
---

# Google Workspace CLI Automation Engine (`/gws-automation-engine`)

## Overview & Tri-Mode Execution

This skill manages Google Workspace CLI (`gws`) subprocess operations on Windows OS across Google Drive, Google Sheets, Gmail, and Google Calendar. It eliminates Windows batch file resolution errors (`WinError 2`), prevents `cmd.exe` stringified JSON payload quote stripping, handles OAuth refresh token expirations (`invalid_grant`), and automatically intercepts GCP API enablement blocks (`HTTP 403`).

Invokable via:
- **Slash Command**: `/gws-automation-engine`
- **Dynamic Intent**: Triggered when provisioning Google Sheets, creating Drive folders, sending automated emails, or managing GCP Workspace credentials.
- **Programmatic Inter-Skill Calling**: Invoked by `/new-client`, `/zero-paywall-client-os`, `/interactive-operator-guide-generator`, or `/daily-plan-day`.

---

## Core Rules & Windows Execution Safeguards

1. **Direct Node Entry Point Routing (Zero `cmd.exe` / `shell=False`)**:
   - **NEVER** invoke `gws` through `cmd.exe` or set `shell=True` in Python subprocess calls on Windows OS.
   - Npm CLI binaries on Windows are `.cmd` batch wrappers (`gws.cmd`), which cause `WinError 2` when passed to `subprocess.run(["gws", ...], shell=False)`.
   - **ALWAYS** invoke Node directly targeting the explicit `run.js` entry point:
     ```python
     GWS_RUN_JS = r"C:\Users\HP\AppData\Roaming\npm\node_modules\@googleworkspace\cli\run.js"
     ```

2. **JSON Payload Argument Passing**:
   - Passing stringified JSON containing double quotes through `shell=True` causes `cmd.exe` to strip quotes, producing `EOF while parsing a string` errors.
   - Always pass python dictionaries serialized with `json.dumps(payload)` directly in the argument array with `shell=False`:
     ```python
     cmd = ["node", GWS_RUN_JS, "sheets", "spreadsheets", "create", "--json", json.dumps(payload)]
     subprocess.run(cmd, capture_output=True, text=True, shell=False)
     ```

3. **Account Credential Switching**:
   - ZORIXEL Brand Account: `C:\Users\HP\.config\gws\credentials_brand.json`
   - Personal Account: `C:\Users\HP\.config\gws\credentials_personal.json`
   - Always set `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` in process environment before subprocess execution.

4. **OAuth Error Interception (`invalid_grant`)**:
   - If response contains `invalid_grant` or `token expired`, trigger `node run.js auth login` and prompt the operator to complete browser authentication.

5. **GCP API Enablement Interception (`HTTP 403`)**:
   - If response contains `accessNotConfigured` or `has not been used in project`, extract the activation link and present direct GCP console enable URLs to the operator.

---

## 🐍 Standard Python Subprocess Execution Boilerplate

```python
import subprocess
import json
import os
import sys

GWS_RUN_JS = r"C:\Users\HP\AppData\Roaming\npm\node_modules\@googleworkspace\cli\run.js"
BRAND_CREDS = r"C:\Users\HP\.config\gws\credentials_brand.json"

def call_gws(service_args, json_payload=None, creds_path=BRAND_CREDS):
    env = os.environ.copy()
    env["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = creds_path
    
    cmd = ["node", GWS_RUN_JS] + service_args
    if json_payload:
        cmd.extend(["--json", json.dumps(json_payload)])
        
    res = subprocess.run(cmd, capture_output=True, text=True, shell=False, env=env)
    
    if res.returncode != 0:
        err_msg = res.stderr or res.stdout
        if "invalid_grant" in err_msg:
            print("[OAUTH EXPIRED] Run: python scripts/aios_gws_health_check.py")
        elif "accessNotConfigured" in err_msg:
            print(f"[GCP API DISABLED] Enable API at console link in error:\n{err_msg}")
        raise RuntimeError(f"GWS CLI Execution Failed: {err_msg}")
        
    return json.loads(res.stdout) if res.stdout.strip() else {}
```

---

## 🧪 Pre-Flight Environment Verification Protocol

Before running complex Google Workspace automations:
1. Execute `python scripts/aios_gws_health_check.py` using `run_command`.
2. Ensure Node.js binary, `run.js` entry point, OAuth refresh tokens, and Drive/Sheets GCP APIs return `[OK]`.

---

## Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

