---
title: Vashishthya Notion OS & Google Workspace Setup SOP (1-Page Guide)
domain: audit
summary: '**Client:** Vashishthya Research Education Foundation **System:** Operational Notion OS + 100% Free Google Workspace
  Sync Engine'
critical_directives:
- Adding a New Column:** Add any new column in Notion or Google Sheets. The system uses **Dynamic Column Mapping**, so exi
section_outline:
- Vashishthya Notion OS & Google Workspace Setup SOP (1-Page Guide)
- '📌 STEP 1: Duplicate Notion Master OS Template (2 Minutes)'
- '📊 STEP 2: Create Master Google Drive Workspace Folder (2 Minutes)'
- '⚡ STEP 3: Connect Google Apps Script (3 Minutes — 100% Free Cloud Sync)'
- 🎯 How Staff & Founders Work Daily
read_triggers:
- When working on audit in clients/001-vashishthya-research-edu/01-pre-outreach-audit/03-pitch-and-loom-guides/VASHISTHYA_NOTION_GSHEETS_SETUP_GUIDE.md
- When reading context for Vashishthya Notion OS & Google Workspace Setup SOP (1-Page Guide)
tags:
- audit
- VASHISTHYA_NOTION_GSHEETS_SETUP_GUIDE
updated: '2026-08-08'
---

# Vashishthya Notion OS & Google Workspace Setup SOP (1-Page Guide)

**Client:** Vashishthya Research Education Foundation  
**System:** Operational Notion OS + 100% Free Google Workspace Sync Engine  
**Setup Time:** 10 to 15 Minutes (Zero Code, Zero Monthly Bills)

---

## 📌 STEP 1: Duplicate Notion Master OS Template (2 Minutes)

1. Open the shareable template link provided during your Zoom onboarding:  
   `[Vashishthya Master Client Desk Template]`
2. Click **Duplicate** in the top right corner.
3. Sign into your free Notion account (`parsjp17@gmail.com`).
4. **Mobile Shortcut Setup:**
   - Open the Notion Mobile App on your Android/iOS phone.
   - Open the **Call Intake Desk** view.
   - Tap `...` (Top Right) -> Select **Add to Home Screen**.  
   *Result:* Dr. Prashant Singh can now log calls in <30 seconds with 1 tap on his phone.

---

## 📊 STEP 2: Create Master Google Drive Workspace Folder (2 Minutes)

1. Go to `drive.google.com` using `parsjp17@gmail.com`.
2. Create a new folder named: **`VASHISTHYA OPERATIONAL HUB`**.
3. Inside this folder, create a new Google Sheet named: **`01-Vashishthya-Master-OS`**.
4. Rename the default sheet tab to: **`Scholars Intake`**.

---

## ⚡ STEP 3: Connect Google Apps Script (3 Minutes — 100% Free Cloud Sync)

1. In your `01-Vashishthya-Master-OS` Google Sheet, click **Extensions** -> **Apps Script**.
2. Erase any default code and paste the code from [GoogleAppsScript_NotionSync.gs](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/GoogleAppsScript_NotionSync.gs).
3. Paste your Notion Integration Token and Database ID into lines 18–19:
   - `NOTION_API_KEY`: `'secret_...'`
   - `NOTION_DATABASE_ID`: `'...'`
4. Click **Save** -> Click **Run** (`runMasterSync`).
5. **Set 24/7 Cloud Trigger:**
   - Click the Clock icon (Triggers) on the left menu.
   - Click **Add Trigger** -> Select `runMasterSync` -> Select **Time-driven** -> **Every hour**.  
   *Result:* Google Cloud now syncs Notion rows automatically 24/7 for FREE.

---

## 🎯 How Staff & Founders Work Daily

| User Role | View Used | Primary Action |
|---|---|---|
| **Dr. Prashant Singh / Dr. Pooja Singh** | Phone Home Screen -> Notion Call Intake | Enter Scholar Name, Select Services, Type Total Fee & Advance, Assign Staff. |
| **Academic Staff Leads** | Desktop Notion -> My Work Queue | Check off 5 steps as work completes. Progress bar auto-calculates `0%` -> `100%`. |
| **Accounting & Audit** | Google Sheet -> `Financial Ledger` Tab | View auto-calculated Total Contracted Revenue, Advance Collected, and Outstanding Balance. |

---

## 💡 How to Add New Services or Columns in the Future Without Breaking Anything

- **Adding a New Service:** Open Notion Database Settings -> `Services Required` property -> Add a new option (e.g. `8. PhD Thesis Defense Coaching`).
- **Adding a New Column:** Add any new column in Notion or Google Sheets. The system uses **Dynamic Column Mapping**, so existing sync functions will **NEVER break**.
