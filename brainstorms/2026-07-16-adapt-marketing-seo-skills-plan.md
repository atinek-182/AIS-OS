# Marketing and SEO-Audit Skills Integration Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate Corey Haynes' marketing copy frameworks and Daniel Agrici's SEO audit tools into Atinek's AIOS without causing context bloat or slash command collisions.

**Architecture:** We will set up a static library `d:\AI-OS\brain-aios\wiki\research\skills-library/` to hold 70+ reference skills/scripts, and create two clean router skills (`marketing` and `seo-audit`) under `.agents/skills/` to load frameworks on demand and run python audit scripts.

**Tech Stack:** Antigravity custom skills (YAML frontmatter + Markdown), Python 3, Git.

---

## Global Constraints
* No command prefix collisions under `.agents/skills/`.
* Preserved capability to run Python files in `claude-seo/scripts/` directly using python.
* Update `WORKSPACE_MAP.md`, `GEMINI.md`, and `decisions/log.md` immediately upon completing implementation.

---

## Proposed Changes

### [Component Name] Setup Static Reference Library
* Clean up cloned repositories in `d:\AI-OS\scratch/` (removing `.git` and unnecessary files) and move them to `d:\AI-OS\brain-aios\wiki\research\skills-library/`.

### Task 1: Set up Static Reference Library

**Files:**
* Modify: Clean up `d:\AI-OS\scratch/marketingskills`
* Modify: Clean up `d:\AI-OS\scratch/claude-seo`
* Create: `d:\AI-OS\brain-aios\wiki\research\skills-library/marketingskills/`
* Create: `d:\AI-OS\brain-aios\wiki\research\skills-library/claude-seo/`

**Interfaces:**
* Produces: Reference folder structure with all `.md` skills and Python scripts.

- [ ] **Step 1: Clean up `.git` directories and test files in cloned scratch folders to avoid nested git repo issues**
  Run commands to remove `.git` folders in `d:\AI-OS\scratch/marketingskills` and `d:\AI-OS\scratch/claude-seo`.
- [ ] **Step 2: Create target directory `d:\AI-OS\brain-aios\wiki\research\skills-library/`**
- [ ] **Step 3: Move clean files from scratch to the target skills-library folder**
  Move `marketingskills` and `claude-seo` directories into `d:\AI-OS\brain-aios\wiki\research\skills-library/`.
- [ ] **Step 4: Commit changes to Git**
  ```bash
  git add d:/AI-OS/brain-aios/wiki/research/skills-library
  git commit -m "feat: initialize static skills-library for marketing and seo"
  ```

---

### Task 2: Create Active `marketing` Router Skill

**Files:**
* Create: `d:\AI-OS\.agents\skills\marketing\SKILL.md`

**Interfaces:**
* Consumes: Marketing files in `d:\AI-OS\brain-aios\wiki\research\skills-library/marketingskills/skills/`
* Produces: `/marketing` slash command and auto-trigger on copywriting terms.

- [ ] **Step 1: Write `d:\AI-OS\.agents\skills\marketing\SKILL.md` with trigger rules and dynamic file reading instructions**
  Ensure frontmatter triggers on: copywriting, landing page, headline help, CTA, email copy, captions.
  Ensure body instructions teach the agent to identify the sub-category, use `view_file` to read the corresponding reference skill at `d:\AI-OS\brain-aios\wiki\research\skills-library/marketingskills/skills/{sub-category}/SKILL.md`, and apply it.
- [ ] **Step 2: Run verification to check syntax of the new skill**
- [ ] **Step 3: Commit changes to Git**
  ```bash
  git add d:/AI-OS/.agents/skills/marketing
  git commit -m "feat: add active marketing router skill"
  ```

---

### Task 3: Create Active `seo-audit` Router Skill

**Files:**
* Create: `d:\AI-OS\.agents\skills\seo-audit\SKILL.md`

**Interfaces:**
* Consumes: SEO files in `d:\AI-OS\brain-aios\wiki\research\skills-library/claude-seo/`
* Produces: `/seo-audit` slash command and auto-trigger on SEO terms.

- [ ] **Step 1: Write `d:\AI-OS\.agents\skills\seo-audit\SKILL.md` with trigger rules, file reading, and script execution instructions**
  Ensure frontmatter triggers on: SEO, technical SEO, schema, sitemaps, GEO, AEO, pagespeed.
  Ensure body instructions teach the agent to locate the matching `.md` file or python script in `skills-library/claude-seo/` and execute it if necessary.
- [ ] **Step 2: Run verification to check syntax of the new skill**
- [ ] **Step 3: Commit changes to Git**
  ```bash
  git add d:/AI-OS/.agents/skills/seo-audit
  git commit -m "feat: add active seo-audit router skill"
  ```

---

### Task 4: System Configurations & Workspace Updates

**Files:**
* Modify: `d:\AI-OS\GEMINI.md`
* Modify: `d:\AI-OS\WORKSPACE_MAP.md`
* Modify: `d:\AI-OS\decisions/log.md`

**Interfaces:**
* Produces: Updated central configurations and maps registering the new skills.

- [ ] **Step 1: Update `GEMINI.md` to register `/marketing` and `/seo-audit` in the "Your skills" section**
- [ ] **Step 2: Update `WORKSPACE_MAP.md` to register the new skill folders and the `skills-library/` directory**
- [ ] **Step 3: Append decision log entries to `decisions/log.md` detailing the integration**
- [ ] **Step 4: Run workspace map validation script to ensure no syntax errors or unmapped files**
  Run: `python d:/AI-OS/scripts/validate_workspace_map.py`
- [ ] **Step 5: Commit configuration changes to Git**
  ```bash
  git add d:/AI-OS/GEMINI.md d:/AI-OS/WORKSPACE_MAP.md d:/AI-OS/decisions/log.md
  git commit -m "config: update workspace configuration and maps for marketing/seo skills"
  ```

---

## Verification Plan

### Automated/Local Tests
* Run a mock copywriting check and mock SEO audit command to verify that the router skills correctly trigger, read reference files, and execute scripts without error.
