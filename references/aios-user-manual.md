# ZORIXEL AIOS User Manual & Execution Guide

Welcome to the central operational manual for your personal AI Operating System (AIOS). This handbook contains instructions on how to trigger and use the custom workspace skills and global plugins set up in your environment.

---

## 🛠️ Part 1: Custom Workspace Skills

These skills reside in `.agents/skills/` and can be triggered in conversation by typing their slash commands or requesting them in natural language.

### 1. `/plan-day` (Daily Morning Loop)
- **Purpose:** Starts your morning. Pulls tasks, priorities, and Google Calendar events, fanning them into a structured hourly schedule.
- **How to Use:**
  - Type `/plan-day` in your terminal.
  - The AIOS will query [priorities.md](file:///d:/AI-OS/context/priorities.md), [master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md), and pull GCal events using the `gws` CLI under your Personal profile.
  - It outputs a tabular daily calendar and asks for confirmation.

### 2. `/review-day` (Daily Evening Loop)
- **Purpose:** Concludes your workday. Prompts you for completed tasks, audits manual repetitive overhead, and updates checklist files.
- **How to Use:**
  - Type `/review-day` at the end of the day.
  - Provide a list of completed items, manual tasks done 3+ times, and estimated time saved.
  - The AIOS will update [master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md) to mark items completed and append notes to the log.

### 3. `/scrape-competitor` (Competitor Scraper Ingest)
- **Purpose:** Automates ingestion of competitor reels/posts research into your Zorixel Second Brain.
- **How to Use:**
  - Type `/scrape-competitor` or `/scrape-competitor [url/topic]`.
  - Open Instagram, run the `rtrvr.ai` extension, and copy the scraped data fields (hook, CTA, transcript, offering).
  - Paste the raw data into the chat. The AIOS parses it, groups it under content pillars, and saves a markdown file to `second-brain-zorixel/wiki/research/`.

### 4. `/draft-message` (On-Brand DM & Email Copywriter)
- **Purpose:** Drafts variations for emails, DMs, or comments matching the ZORIXEL voice guidelines.
- **How to Use:**
  - Type `/draft-message` or `/draft-message [recipient & intent]`.
  - The AIOS reads the voice instructions in `second-brain-zorixel/wiki/brand/personality-and-voice.md` and generates 3 casual, energetic variations.
  - Choose one to copy, or instruct the AIOS to base64-encode and create a draft in Gmail using the `gws` CLI.

### 5. `/file-search` (Multi-Vault Keyword Retrieval)
- **Purpose:** Fast keyword and phrase finder across both Obsidian vaults.
- **How to Use:**
  - Type `/file-search [query]` (e.g. `/file-search GSAP`).
  - The AIOS scans both `brain-aios/` and `second-brain-zorixel/` folders, displaying matching lines with clickable `file:///` links.

### 6. `/agent-adapt` (Claude-to-Antigravity Migration Orchestrator)
- **Purpose:** Standardizes, installs, and cleans up plugins and configuration files to transition the AIOS setup from Claude to native Antigravity rules.
- **How to Use:**
  - Type `/agent-adapt`.
  - The AIOS searches for Antigravity native equivalents of requested plugins, replaces Claude patterns, cleans up local configuration traces, and runs verification tests under the Antigravity developer environment.

---


## ⚙️ Part 2: Global Plugins

These plugins are installed globally inside your Antigravity environment and run automatically to optimize reasoning, memory, and context.

### 1. Superpowers (`superpowers`)
- **Enforced Rule:** Enforces plan-first, TDD, and code reviews.
- **How it works:** When you assign a development goal, it will automatically prompt you with research findings, request approval on an `implementation_plan.md`, write tests, and run quality checks before declaring task completion.

### 2. Context Mode (`context-mode`)
- **Enforced Rule:** Routes CLI log outputs and Playwright HTML files through an isolated compressing sandbox to avoid token bloat.
- **Commands:**
  - Type `/contextmode:ctx-stats` to view the percentage of tokens saved during the session.
  - Run `/context-mode:ctx-doctor` to run diagnostics on local cache indexes.

### 3. Memory & Decisions (`antigravity-mem`)
- **Enforced Rule:** Intercepts project modifications and logs them locally in a SQLite database. On session startup, it auto-restores files and remembers what was decided.
- **Commands:**
  - Type `/mem-search` to query vector memory of past session actions and fixes.

### 4. Get Shit Done (GSD)
- **Enforced Rule:** Coordinates parallel sub-agents to divide-and-conquer heavy software tasks.
- **Commands:**
  - Type `/gsd-help` to list commands.
  - Run `npx get-shit-done-cc --antigravity` or use `/gsd-progress` to triage active projects.

### 5. Front-End Design (`frontend-design`)
- **Enforced Rule:** Automatically applies styling rules (harmony color palettes, Outfit/Inter fonts, micro-interactions, responsive sizing) so that HTML mockups look premium and custom-coded.

