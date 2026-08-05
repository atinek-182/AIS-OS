# Vashishthya Research, IJORAR & MJAP: Client Pitch & Pilot Production Master Plan
**Client Vault:** `clients/001-vashishthya-research-edu/`  
**Date:** 2026-08-03  
**Status:** Ingested & Blueprint Finalized (Awaiting Sister's Inputs for Placeholders)  

---

## Executive Summary & Strategic Positioning
- **Target Client**: Dr. Prashant Singh & Dr. Pooja Singh (Vashishthya Research & Educational Academy + Academic Journals).
- **Core Friction**: Founder handles phone calls directly $\rightarrow$ scribbles on paper or memorizes details $\rightarrow$ verbal staff handoffs $\rightarrow$ constant nagging ("Is the work done?").
- **Solution Engine**: Zero-code **Notion Operational Hub** (Intake Form + Employee Dispatcher + Auto-Progress Bars) backed by optional Google Sheets sync.
- **Client Vault Deliverables**:
  - Loom Cheat Sheet: [LOOM_MOBILE_CHEAT_SHEET.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/LOOM_MOBILE_CHEAT_SHEET.md)
  - Raw Deep Research: [DEEP_RESEARCH_REPORT.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/DEEP_RESEARCH_REPORT.md)
  - Master Pre-Outreach Audit: [AUDIT.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/AUDIT.md)
  - Commercial Proposal: [PROPOSAL.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/02-proposal-and-agreement/PROPOSAL.md)

---

## 🛠️ Notion + Google Sheets Agentic Workflow Blueprint

### 1. Database Architecture (Single Source of Truth)
To prevent fragile sync failures, the entire system lives inside **One Master Notion Database** (`Vashishthya Master Deliverables DB`), with custom Database Views for different roles:

#### View A: "Call Intake Desk" (Prashant Sir & Pooja Mam Phone/Desktop View)
- **Properties**:
  - `Scholar Name` (Title)
  - `Contact / WhatsApp Number` (Phone)
  - `Services Required` (Multi-Select Checkboxes):
    - `[ ] 1. Ph.D. Writing & Thesis (₹20,000)`
    - `[ ] 2. PG Project & Dissertation (MCA/MBA/MSc/MA/MTech) (₹5,000)`
    - `[ ] 3. Book Writing (₹3,000) / Hard Copy Publication (₹5,000)`
    - `[ ] 4. Paper Writing & Peer-Reviewed Journal Publication (₹2,000)`
    - `[ ] 5. Academic Reports & Removal (Turnitin ₹100 / Drillbit ₹200 / Plagiarism Removal)`
    - `[ ] 6. Patent Services (UK/Germany/South Africa/India - Utility & Design) (₹15,000)`
    - `[ ] 7. Academic Certificates & Awards (Reviewer / Board / Proposals: AICTE/UGC/DST/DRDO/ISRO)`
  - `Agreed Fee (INR)` (Number)
  - `Target Deadline` (Date)
  - `Assigned Team Member` (Select): `Dr. Prashant Singh` | `Dr. Pooja Singh` | `Assigned Staff Lead`
  - `Status`: `New Intake` $\rightarrow$ `In Progress` $\rightarrow$ `Client Review` $\rightarrow$ `Completed`

#### View B: "My Work Queue" (Employee Personal Board)
- Filtered automatically by `Assigned Team Member = [Current User]` and `Status != Completed`.
- Shows a 5-Step Sub-Task Checklist:
  - `[ ] Step 1: Topic & Scope Confirmation`
  - `[ ] Step 2: Outline & Literature Gathering`
  - `[ ] Step 3: Core Draft & Data Analysis`
  - `[ ] Step 4: Plagiarism & Formatting Check`
  - `[ ] Step 5: Final Client Delivery & PDF Archive`
- As employees check off steps, a Notion Rollup Formula automatically displays a live percentage bar (`0%` $\rightarrow$ `20%` $\rightarrow$ `40%` $\rightarrow$ `60%` $\rightarrow$ `80%` $\rightarrow$ `100%`).

#### View C: "Executive Overview" (Founder High-Level Control Bar)
- Visual Kanban / Table showing all scholars, progress percentage bars, assigned team members, and overdue alerts.

### 2. Google Sheets Backup & Employee Sync Plan
- **Primary Hub**: Notion (used for daily work and call intake).
- **Sync Mechanism**: A lightweight Google Workspace CLI (`gws`) script or n8n webhook syncs Notion Database rows to a shared **Google Sheet** (`Vashishthya Master Client CRM.xlsx`) every night or on row creation.
- **Fail-Safe**: If external sync fails, Notion remains 100% functional.

### 3. Remote Setup & Installation Plan (15-Minute Zoom Onboarding)
1. **Desktop Setup**: Share screen during Zoom call $\rightarrow$ Duplicate `Vashishthya Operational OS` Notion Template into Dr. Prashant Singh's free Notion account.
2. **Mobile Setup**: Have Prashant Sir download the free Notion Mobile App (iOS/Android) $\rightarrow$ Pin the **"Call Intake"** view shortcut directly to his smartphone home screen.
3. **Staff Onboarding**: Invite employees as free Guest Collaborators in Notion $\rightarrow$ Bookmark their "My Work Queue" view.

---

## 👥 5-PERSONA ADVERSARIAL ROAST AUDIT (`/roast`)

### 1. The Contrarian (Red Team)
> **Roast**: "What happens if Prashant Sir is driving or taking a call on the go and can't open Notion? What if staff forget to update task statuses in Notion, forcing him back into manual WhatsApp nagging?"
> **Fix / Mitigation**: 
> 1. Make the Mobile Notion Intake Form reachable in **1 tap** via a Phone Home Screen Shortcut Icon.
> 2. Implement an automated daily reminder (via n8n or WhatsApp webhook) sent to staff at 6:00 PM: *"Please update your active scholar checklists before leaving today."*

### 2. The Expansionist (Bull)
> **Roast**: "Giving away a Notion template for free is nice, but where is the $1,500 - $3,000 retainer upside for ZORIXEL?"
> **Upside Leverage**: 
> 1. Once Prashant Sir sees Notion working for 14 days, propose **Wave 2 Automation**: Auto-sending instant WhatsApp confirmation receipts to scholars when Prashant Sir clicks 'Submit', and auto-generating CrossRef/Google Scholar XML files for published papers.
> 2. Position ZORIXEL as their **Retainer Fractional AI Partner** (₹30,000–₹50,000/mo).

### 3. The Logician (First Principles)
> **Roast**: "Does the Notion-to-Google Sheets sync add fragile point-of-failure dependencies?"
> **Logic Read**: 
> Keeping 100% of the operational logic inside Notion first eliminates external API dependencies. Google Sheets acts strictly as a passive read-only backup, guaranteeing zero workflow downtime even if network scripts drop.

### 4. The Researcher (Evidence & Market Data)
> **Roast**: "Will non-tech founders in Raipur actually adopt Notion?"
> **Market Data**: 
> Research shows non-tech agency founders reject complex CRMs (HubSpot/Salesforce) due to bloated menus, but adoption rate for Notion mobile checklists is >80% because it mirrors a digital notepad with checkboxes.

### 5. The Buyer (Dr. Prashant Singh & Dr. Pooja Singh)
> **Roast**: "Will Prashant Sir feel overwhelmed during a Zoom demo?"
> **Buyer Read**: 
> If you talk about 'databases', 'schemas', or 'JSON-LD', he will tune out. But if you show: *"Sir, call ke waqt 3 ticks kijiye, staff ke paas kaam chala jayega, aur aapko puchna nahi padega"*, he will immediately say **YES** to the Zoom call.

---

## ⚖️ THE VERDICT: GO (Reshaped for Notion Operational OS)
**Confidence:** High · **Operator:** Atinek Maurya  
**The Call in One Line:** Execute the Loom pitch using the Mobile Bullet Cheat Sheet, leading with the zero-code Notion Operational OS and Google Scholar metadata fixes.
