---
title: Utility Scripts Reference Guide
domain: architecture
summary: This document describes the utility scripts stored under the [scripts/](file:///d:/AI-OS/scripts/) folder of the
  workspace and provides instructions for running them. - **Location:** `scripts/agent_adapt.py`
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Utility Scripts Reference Guide
- 1. `agent_adapt.py`
- 2. `rename_and_link_update.py`
- 3. `verify_skills.py`
- 4. `design_synthesis_engine.py`
read_triggers:
- When working on architecture in references/utility-scripts.md
- When reading context for Utility Scripts Reference Guide
tags:
- architecture
- utility-scripts
updated: '2026-08-08'
---

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

## 4. `design_synthesis_engine.py`
- **Location:** `scripts/design_synthesis_engine.py`
- **Purpose:** Zero-bloat indexer and recommendation engine synthesizing 23 reference sites. Parses TSX extractions, OKLCH tokens, section taxonomy, and UX psychology into `references/23-sites-matrix.json`.
- **How to Run:**
  ```powershell
  python scripts/design_synthesis_engine.py index
  python scripts/design_synthesis_engine.py search-pattern "hero"
  python scripts/design_synthesis_engine.py recommend-layout --niche saas
  ```

---

## 5. `component_registry_cli.py`
- **Location:** `scripts/component_registry_cli.py`
- **Purpose:** Unified component search CLI querying 300+ cataloged UI components AND 23 reference sites extractions.
- **How to Run:**
  ```powershell
  python scripts/component_registry_cli.py search "bento"
  python scripts/component_registry_cli.py adapt <component_name>
  ```

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
- **Purpose:** Simulates the workflow execution logic of the workspace skills (`daily-plan-day`, `daily-review-day`, `scrape-competitor`, `draft-message`, `file-search`) to verify their behaviors and specs compliance.
- **How to Run:**
  ```powershell
  python scripts/demo_test_skills.py
  ```


