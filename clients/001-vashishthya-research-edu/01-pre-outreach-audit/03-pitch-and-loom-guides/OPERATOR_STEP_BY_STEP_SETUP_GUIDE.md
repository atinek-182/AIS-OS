---
title: 'Operator Step-by-Step Setup Guide: Building Notion OS & Google Workspace Sync from Scratch'
domain: audit
summary: '**Target Operator:** Atinek Maurya **Goal:** Build the live Notion Master Database in your own free Notion account,
  generate the shareable template link, and set up Google Apps Script live sync in 6 minutes.'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- '📌 PART 1: BUILD THE NOTION DATABASE IN YOUR ACCOUNT (3 MINUTES)'
- '📊 PART 2: BUILD GOOGLE SHEETS & APPS SCRIPT (3 MINUTES)'
- '🎥 PART 3: RECORDING YOUR LOOM VIDEO DEMO'
read_triggers:
- When working on audit in clients/001-vashishthya-research-edu/01-pre-outreach-audit/03-pitch-and-loom-guides/OPERATOR_STEP_BY_STEP_SETUP_GUIDE.md
- 'When reading context for Operator Step-by-Step Setup Guide: Building Notion OS & Google Workspace Sync from Scratch'
tags:
- audit
- OPERATOR_STEP_BY_STEP_SETUP_GUIDE
updated: '2026-08-08'
---

# Operator Step-by-Step Setup Guide: Building Notion OS & Google Workspace Sync from Scratch

**Target Operator:** Atinek Maurya  
**Goal:** Build the live Notion Master Database in your own free Notion account, generate the shareable template link, and set up Google Apps Script live sync in 6 minutes.

---

## 📌 PART 1: BUILD THE NOTION DATABASE IN YOUR ACCOUNT (3 MINUTES)

1. **Create Page:**
   - Open [notion.so](https://notion.so) in your browser.
   - Click **+ Add a page** in your left sidebar.
   - Title it: **`Vashishthya Master Client Desk`**.

2. **Insert Database:**
   - On the blank page, type `/table` and press Enter.
   - Click **New database**.

3. **Add Properties (Click `+` icon on column header to add each property):**

   | Property Name | Property Type | Options / Formula / Details |
   |---|---|---|
   | **Scholar Name** | `Title` | Default primary title field |
   | **Contact / WhatsApp Number** | `Phone` | e.g. `8319353139` |
   | **Email Address** | `Email` | e.g. `parsjp17@gmail.com` |
   | **Services Required** | `Multi-select` | Add 7 Options (Ph.D. ₹20k, PG Project ₹5k, Book Pub ₹3k-5k, Paper Writing ₹2k, Reports ₹100-200, Patents ₹15k, Certificates/Awards) |
   | **Agreed Total Fee (INR)** | `Number` | Number format -> Select **Rupee** |
   | **Advance Received (INR)** | `Number` | Number format -> Select **Rupee** |
   | **Balance Due (INR)** | `Formula` | Paste formula: `prop("Agreed Total Fee (INR)") - prop("Advance Received (INR)")` |
   | **Payment Status** | `Select` | Options: `Unpaid` (Red), `Partially Paid` (Yellow), `Fully Settled` (Green) |
   | **Status** | `Status` | Options: `New Intake` (Gray), `In Progress` (Blue), `Client Review` (Yellow), `Completed` (Green) |
   | **Assigned Team Member** | `Select` | Options: `Dr. Prashant Singh`, `Dr. Pooja Singh`, `Assigned Staff Lead` |
   | **Target Deadline** | `Date` | Select deadline date |
   | **Step 1: Scope & Topic Confirmation** | `Checkbox` | Checkbox |
   | **Step 2: Outline & Literature Gathering** | `Checkbox` | Checkbox |
   | **Step 3: Draft Writing & Data Analysis** | `Checkbox` | Checkbox |
   | **Step 4: Plagiarism (<10%) & Format Check** | `Checkbox` | Checkbox |
   | **Step 5: Final Delivery & Archive** | `Checkbox` | Checkbox |
   | **Progress Bar** | `Formula` | Paste formula: `(if(prop("Step 1: Scope & Topic Confirmation"), 1, 0) + if(prop("Step 2: Outline & Literature Gathering"), 1, 0) + if(prop("Step 3: Draft Writing & Data Analysis"), 1, 0) + if(prop("Step 4: Plagiarism (<10%) & Format Check"), 1, 0) + if(prop("Step 5: Final Delivery & Archive"), 1, 0)) * 0.20` -> Set Display to **Bar** |
   | **1-Click WhatsApp Link** | `Formula` | Paste formula: `"https://wa.me/91" + replaceAll(prop("Contact / WhatsApp Number"), "[^0-9]", "") + "?text=Hello%20" + encodeURIComponent(prop("Scholar Name")) + "%2C%20status%3A%20" + encodeURIComponent(prop("Status"))` |

4. **Add 3 Role Views (Top left tab bar of Notion database):**
   - **View 1 ("Call Intake Desk")**: Form / Table view displaying only intake fields.
   - **View 2 ("My Work Queue")**: Board view grouped by `Status`, showing checkboxes & Progress Bar.
   - **View 3 ("Executive Master Overview")**: Full Table view showing all fields.

5. **Generate Your Shareable Notion Template Link:**
   - Click **Share** (Top Right corner of Notion page).
   - Click **Publish** tab -> Click **Publish to web**.
   - Ensure **Allow duplication as template** is turned **ON**.
   - Click **Copy web link**.  
   *Result:* This is your shareable link to demonstrate on Loom and share with Dr. Prashant Singh!

---

## 📊 PART 2: BUILD GOOGLE SHEETS & APPS SCRIPT (3 MINUTES)

1. Open `drive.google.com` in browser.
2. Create folder: **`VASHISTHYA OPERATIONAL HUB`**.
3. Create Google Sheet: **`01-Vashishthya-Master-OS`**. Rename first sheet tab to `Scholars Intake`.
4. Click **Extensions** -> **Apps Script**.
5. Delete default code in `Code.gs` and paste the contents of [GoogleAppsScript_NotionSync.gs](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/02-notion-and-automation-specs/GoogleAppsScript_NotionSync.gs).
6. Click **Save** (Ctrl+S) -> Click **Run** (`runMasterSync`).

---

## 🎥 PART 3: RECORDING YOUR LOOM VIDEO DEMO

1. Open your new Notion database (`Vashishthya Master Client Desk`) in Tab 1.
2. Open `ijorarjournal.com` in Tab 2.
3. Open [setup_guide_visual.html](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/04-visual-assets-and-previews/setup_guide_visual.html) in Tab 3.
4. Click Record on Loom and follow the bullet points in [LOOM_VIDEO_DEMO_SCRIPT_GUIDE.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/03-pitch-and-loom-guides/LOOM_VIDEO_DEMO_SCRIPT_GUIDE.md).
