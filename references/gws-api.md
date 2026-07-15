# Google Workspace CLI (GWS) Integration Guide

This guide details the integration details, environment credentials, CLI syntax, and scripting templates for the Google Workspace CLI (`gws`) used inside your AIOS.

---

## 🔒 1. Environment & Authentication Profile Flow

The `gws` CLI determines which account to hit based on the path supplied in the `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` environment variable. These credential paths are loaded from your workspace `.env` file:

- **Personal Profile Environment:**
  `$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE = $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_PERSONAL`
  Points to: `C:\Users\HP\.config\gws\credentials_personal.json`

- **Brand/ZORIXEL Profile Environment:**
  `$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE = $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_BRAND`
  Points to: `C:\Users\HP\.config\gws\credentials_brand.json`

---

## 💻 2. Common CLI Commands Reference

Ensure you set the profile environment variable in the same line of command execution:

### Calendar Operations (GCal)
- **List calendar events:**
  ```powershell
  $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"; gws calendar events --days 1
  ```
- **Add calendar event:**
  ```powershell
  $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"; gws calendar add --title "Zorixel Content Prep" --start "2026-07-15T10:00:00" --duration "2h"
  ```

### Gmail Operations (Emails & Drafts)
- **List unread emails:**
  ```powershell
  $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"; gws gmail list --unread
  ```
- **Create draft email (Base64-encoded body support):**
  ```powershell
  $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_brand.json"; gws gmail draft create --to "collaborator@example.com" --subject "Zorixel Partnership Proposal" --body "hey! just wanted to share..."
  ```

---

## 🐍 3. Programmatic Python Execution Template

Below is a Python function you can call from your custom workflow scripts to invoke the `gws` CLI with the correct environmental credentials loaded from `.env`:

```python
import os
import subprocess
from dotenv import load_dotenv

# Load workspace env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

def run_gws_command(profile: str, args: list) -> str:
    """
    Executes a gws CLI command under the selected credentials profile.
    profile: 'personal' or 'brand'
    args: list of command line arguments (e.g. ['calendar', 'events', '--days', '1'])
    """
    # Select credential file path from environment variables
    env_var = "GOOGLE_WORKSPACE_CLI_CREDENTIALS_PERSONAL" if profile == "personal" else "GOOGLE_WORKSPACE_CLI_CREDENTIALS_BRAND"
    cred_file = os.getenv(env_var)
    
    if not cred_file or not os.path.exists(cred_file):
        raise FileNotFoundError(f"Credential file not found for profile {profile}: {cred_file}")
    
    # Clone current environment and inject credentials file variable
    custom_env = os.environ.copy()
    custom_env["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = cred_file
    
    # Execute the gws command
    command = ["gws"] + args
    result = subprocess.run(command, env=custom_env, capture_output=True, text=True, check=True)
    return result.stdout.strip()

# Example: Get calendar events under personal profile
# events = run_gws_command('personal', ['calendar', 'events', '--days', '1'])
# print(events)
```
