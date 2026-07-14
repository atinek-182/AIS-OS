# Google Workspace CLI (GWS) API Reference

This file documents the credentials configuration, account switching methods, and common commands for the Google Workspace CLI (`gws`).

---

## Authentication & Account Configuration

Credentials and secrets are managed in `C:\Users\HP\.config\gws\`.

- **OAuth Client Secret**: `C:\Users\HP\.config\gws\client_secret.json` (Linked to GCP Project `Zorixel AIOS`)
- **Personal Account Credentials**: `C:\Users\HP\.config\gws\credentials_personal.json`
- **Brand Account Credentials**: `C:\Users\HP\.config\gws\credentials_brand.json`

---

## Switching Accounts

To switch the active account for commands, set the `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` environment variable:

### In PowerShell
```powershell
# Switch to Personal Account
$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"

# Switch to Brand Account
$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_brand.json"
```

### In Bash
```bash
# Switch to Personal Account
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"

# Switch to Brand Account
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_brand.json"
```

---

## Common Commands & Queries

### Drive
- **List Files**:
  ```bash
  gws drive files list --params '{"pageSize": 5}'
  ```
- **Search Files (by name/mime type)**:
  ```bash
  gws drive files list --params '{"q": "name contains \'Zorixel\'", "pageSize": 5}'
  ```

### Gmail
- **List Messages**:
  ```bash
  gws gmail users messages list --params '{"userId": "me", "maxResults": 5}'
  ```
- **Read Message**:
  ```bash
  gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'
  ```
- **Draft Message**:
  ```bash
  gws gmail users drafts create --params '{"userId": "me"}' --json '{"message": {"raw": "BASE64_ENCODED_RFC822_MESSAGE"}}'
  ```

### Sheets
- **Create Spreadsheet**:
  ```bash
  gws sheets spreadsheets create --json '{"properties": {"title": "Zorixel Revenue Log"}}'
  ```
- **Get Spreadsheet Values**:
  ```bash
  gws sheets spreadsheets values get --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "Sheet1!A1:D10"}'
  ```

### Calendar
- **List Upcoming Events**:
  ```bash
  gws calendar events list --params '{"calendarId": "primary", "maxResults": 5}'
  ```
