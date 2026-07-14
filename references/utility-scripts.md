# Utility Scripts Reference Guide

This document describes the utility scripts stored under the [scripts/](file:///d:/AI-OS/scripts/) folder of the workspace and provides instructions for running them.

---

## 1. `agent_adapt.py`
- **Location:** `scripts/agent_adapt.py`
- **Purpose:** Automatically scans text files in the workspace (excluding `.git/`, `.obsidian/`, and `node_modules/`) and replaces Claude Code references with Antigravity equivalents:
  - `Claude Code` -> `Antigravity`
  - `Claude` -> `Antigravity`
  - `CLAUDE.md` -> `GEMINI.md`
  - `.claude` -> `.agents`
  - `CLAUDE_SESSION_ID` -> `ANTIGRAVITY_SESSION_ID`
- **How to Run:**
  ```powershell
  python scripts/agent_adapt.py
  ```

---

## 2. `rename_and_link_update.py`
- **Location:** `scripts/rename_and_link_update.py`
- **Purpose:** Renames file names containing `claude` (e.g. course files, raw source files) and automatically updates all double-bracket links `[[...]]` and file header metadata in other Markdown files to prevent broken linkages.
- **How to Run:**
  ```powershell
  python scripts/rename_and_link_update.py
  ```

---

## 3. `verify_skills.py`
- **Location:** `scripts/verify_skills.py`
- **Purpose:** Fast syntax parser that reads the custom skills inside `.agents/skills/`, parses their frontmatter headers, and checks for errors to verify they load correctly in Antigravity.
- **How to Run:**
  ```powershell
  python scripts/verify_skills.py
  ```

---

## 4. `copy_skills_to_antigravity.py`
- **Location:** `scripts/copy_skills_to_antigravity.py`
- **Purpose:** Copies all 122 custom skills from local Claude Code plugin and marketplace folders into the global Antigravity customization folder (`C:\Users\HP\.gemini\config\skills\`) and automatically updates references to be compatible.
- **How to Run:**
  ```powershell
  python scripts/copy_skills_to_antigravity.py
  ```

---

## 5. `demo_test_skills.py`
- **Location:** `scripts/demo_test_skills.py`
- **Purpose:** Simulates the workflow execution logic of the workspace skills (`plan-day`, `review-day`, `scrape-competitor`, `draft-message`, `file-search`) to verify their behaviors and specs compliance.
- **How to Run:**
  ```powershell
  python scripts/demo_test_skills.py
  ```


