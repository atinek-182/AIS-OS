---
title: 'Notion to Google Sheets Live Sync: Complete Step-by-Step Setup Guide'
domain: audit
summary: '**Target Operator:** Atinek Maurya **System:** Notion Master Database -> Google Apps Script -> Google Sheets Live
  Sync'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- 'Notion to Google Sheets Live Sync: Complete Step-by-Step Setup Guide'
- '📌 STEP 1: GET YOUR NOTION INTEGRATION TOKEN (1 MINUTE)'
- '🔗 STEP 2: CONNECT THE INTEGRATION TO YOUR NOTION DATABASE (CRITICAL!)'
- '🆔 STEP 3: GET YOUR NOTION DATABASE ID (30 SECONDS)'
- '📊 STEP 4: PASTE & RUN THE SCRIPT IN GOOGLE SHEETS (2 MINUTES)'
read_triggers:
- When working on audit in clients/001-vashishthya-research-edu/01-pre-outreach-audit/03-pitch-and-loom-guides/NOTION_TO_GSHEETS_INTEGRATION_STEP_BY_STEP.md
- 'When reading context for Notion to Google Sheets Live Sync: Complete Step-by-Step Setup Guide'
tags:
- audit
- NOTION_TO_GSHEETS_INTEGRATION_STEP_BY_STEP
updated: '2026-08-08'
---

# Notion to Google Sheets Live Sync: Complete Step-by-Step Setup Guide

**Target Operator:** Atinek Maurya  
**System:** Notion Master Database -> Google Apps Script -> Google Sheets Live Sync  
**Setup Time:** 5 Minutes (100% Free Cloud Sync, Zero External Accounts Required)  
**Notion API Version:** Notion 2026 Developer Portal Standard (`ntn_...` / `secret_...`)

---

## 📌 STEP 1: GET YOUR NOTION INTEGRATION TOKEN (1 MINUTE)

1. Open your browser and go to: [https://app.notion.com/developers/connections](https://app.notion.com/developers/connections)  
   *(If you go to `notion.so/my-integrations`, Notion will automatically redirect you here).*
2. Click **+ New integration** (or **Create new integration**).
3. Fill in the details:
   - **Name:** `Vashishthya Google Sheet Sync`
   - **Associated workspace:** Select your active workspace.
   - **Type:** Internal Integration
   - **Capabilities:** Ensure **Read content**, **Update content**, and **Insert content** are checked.
4. Click **Save** (or **Submit**).
5. Under the **Secrets** / **Configuration** section, click **Show** and then click **Copy**.
   - *Token Format Note:* Newer Notion tokens start with `ntn_...` (older tokens start with `secret_...`). Either format works perfectly!
   - *Save this token safely — you will paste it into Google Apps Script in Step 4.*

---

## 🔗 STEP 2: CONNECT THE INTEGRATION TO YOUR NOTION DATABASE (CRITICAL!)

*If you skip this step, Notion will block Google Sheets from reading your database.*

1. Open your Notion database page (`Vashishthya Master Client Desk`).
2. Click the **`...`** (three dots) icon in the **top-right corner** of the Notion page.
3. Scroll down and click **Add connections** (or **Connections**).
4. Search for: **`Vashishthya Google Sheet Sync`**.
5. Click it and select **Confirm**.  
   *Result:* Your Notion database is now authorized to send data to Google Apps Script!

---

## 🆔 STEP 3: GET YOUR NOTION DATABASE ID (30 SECONDS)

1. Open your Notion database page in your web browser.
2. Look at your browser URL bar:
   `https://www.notion.so/workspace/a1b2c3d4e5f67890123456789abcdef0?v=...`
3. Copy the **32-character string** between the last slash `/` and `?v=`.
   *(Example Database ID: `a1b2c3d4e5f67890123456789abcdef0`)*

---

## 📊 STEP 4: PASTE & RUN THE SCRIPT IN GOOGLE SHEETS (2 MINUTES)

1. Go to `drive.google.com` and open your Google Sheet: **`-Vashishthya-01Master-OS`**.
2. Rename the first sheet tab to: **`Scholars Intake`**.
3. Click **Extensions** (Top menu bar) -> Select **Apps Script**.
4. Erase any default code in `Code.gs` and paste the entire code from [GoogleAppsScript_NotionSync.gs](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/02-notion-and-automation-specs/GoogleAppsScript_NotionSync.gs).
5. At lines 18–19 of the script, paste your secret token and database ID:
   ```javascript
   NOTION_API_KEY: 'ntn_YOUR_COPIED_TOKEN_HERE',
   NOTION_DATABASE_ID: 'YOUR_32_CHARACTER_DATABASE_ID_HERE',
   ```
6. Click **Save** (disk icon or `Ctrl + S`).
7. Click **Run** (`runMasterSync` function selected).
8. **Permissions Approval:** Click **Review permissions** -> Select your Google account -> Click **Advanced** -> Click **Go to Project (unsafe)** -> Click **Allow**.

---

## ⚡ STEP 5: SET 24/7 AUTOMATIC CLOUD SYNC TRIGGER (30 SECONDS)

1. Inside the Google Apps Script editor, click the **Clock Icon (Triggers)** on the left sidebar menu.
2. Click **+ Add Trigger** (bottom right).
3. Set fields:
   - **Function to run:** `runMasterSync`
   - **Event source:** `Time-driven`
   - **Type of time based trigger:** `Hour timer` -> `Every hour` (or `Every 15 minutes`)
4. Click **Save**.

*Your Notion Master Database and Google Sheet CRM are now 100% connected and auto-syncing 24/7 in the cloud for free!*
