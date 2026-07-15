# Canvas Design Skill Integration Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Canvas Design skill (`/canvas-design`) that programmatically generates premium posters, social media posts, and brand banners using the visual specifications in `Temporary brand design.md` and the Playwright browser subagent.

**Architecture:** Decouple into a static reference folder `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design/` (holding brand assets, styles, base templates) and an active workspace skill `.agents/skills/canvas-design/` (containing browser execution and visual review instructions).

**Tech Stack:** HTML/CSS (Garamond + Inter typography, cream/coral/navy color block system), Playwright Browser Subagent, Git.

---

## Global Constraints
* Preset dimensions must match exact values (instagram-square: 1080x1080, instagram-portrait: 1080x1350, story-reel: 1080x1920, youtube-thumbnail: 1280x720, youtube-banner: 2560x1440).
* Visual self-review is mandatory before presenting final PNGs.
* Update `WORKSPACE_MAP.md` and `decisions/log.md` immediately upon completing implementation.

---

## Proposed Changes

### [Component Name] Setup Static Reference Library
* Copy the brand design specification and build stylesheets/templates in `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design/`.

### Task 1: Set up Static Reference Library

**Files:**
* Create: `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\brand-design.md`
* Create: `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\styles.css`
* Create: `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\template-base.html`

**Interfaces:**
* Produces: Brand styling tokens and HTML/CSS templates for rendering.

- [ ] **Step 1: Copy `Temporary brand design.md` from Downloads to target library**
  Copy `C:\Users\HP\Downloads\Temporary brand design.md` to `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\brand-design.md`.
- [ ] **Step 2: Create `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\styles.css` with CSS variables**
  Map: `--color-canvas: #faf9f5; --color-ink: #141413; --color-primary: #cc785c; --color-surface-card: #efe9de; --color-surface-dark: #181715; --font-display: 'Cormorant Garamond', serif; --font-body: 'Inter', sans-serif;`.
- [ ] **Step 3: Create `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\template-base.html` with responsive layouts**
  Include Google Fonts integrations for Cormorant Garamond and Inter. Add CSS classes for `editorial-quote`, `code-showcase`, `bento-features`, and `full-bleed-callout` layout formats.
- [ ] **Step 4: Commit changes to Git**
  Stage and commit inside `d:/AI-OS/brain-aios` repository.

---

### Task 2: Create Active `canvas-design` Workspace Skill

**Files:**
* Create: `d:\AI-OS\.agents\skills\canvas-design\SKILL.md`

**Interfaces:**
* Consumes: `template-base.html` and styles.
* Produces: `/canvas-design` slash command and auto-trigger on design phrases.

- [ ] **Step 1: Write `d:\AI-OS\.agents\skills\canvas-design\SKILL.md` with trigger rules, layout choices, and Playwright execution flow**
  Set up triggers on: poster, social graphic, banner design, carousel slide, slide background.
  Add instructions for compiling `temp_preview.html` by replacing template variables.
  Add instructions for invoking `browser_subagent` to resize viewport to specified preset dimensions and take a PNG screenshot saved in `d:/AI-OS/brainstorms/`.
  Add instructions for viewing the PNG and running the visual self-correction loop.
- [ ] **Step 2: Commit changes to Git**
  Stage in root repository.

---

### Task 3: Workspace Configs & Updates

**Files:**
* Modify: `d:\AI-OS\WORKSPACE_MAP.md`
* Modify: `d:\AI-OS\decisions\log.md`

**Interfaces:**
* Produces: Updated configurations and registration maps.

- [ ] **Step 1: Update `WORKSPACE_MAP.md` to register `.agents/skills/canvas-design` and `brain-aios/wiki/research/skills-library/canvas-design`**
- [ ] **Step 2: Append decision log entries to `decisions/log.md` and `brain-aios/wiki/log.md`**
- [ ] **Step 3: Run `validate_workspace_map.py` to ensure validation passes**
- [ ] **Step 4: Commit configurations to Git**
  Stage and commit in root repository.

---

## Verification Plan

### Automated/Local Tests
* Run `/canvas-design` to generate a mock Instagram Square graphic. Verify that the agent compiles HTML, calls the browser subagent, renders, and outputs a valid PNG screenshot file.
