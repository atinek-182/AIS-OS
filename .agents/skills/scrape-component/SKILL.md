---
title: Scrape Component Skill
domain: skill
summary: 'This skill supports **Tri-Mode Flexible Execution**: - **Slash Command**: Explicitly run `/scrape-component [optional
  parameters]` in chat.'
critical_directives:
- Extract its computed CSS styles or find the specific stylesheet rules mapping to its selectors.
- If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.m
section_outline:
- Scrape Component Skill
- Invocation & Tri-Mode Routing
- 'Phase 1: Clarification & Targeted Q&A (Do FIRST)'
- 'Phase 2: Isolated Extraction & Dependency Audit'
- 'Phase 3: Visual Verification & Auditing (Playwright Bypass)'
read_triggers:
- When working on skill in .agents/skills/scrape-component/SKILL.md
- When reading context for Scrape Component Skill
tags:
- skill
- SKILL
updated: '2026-08-08'
name: scrape-component
description: Extract a specific UI component, animation, or style from a website URL. Conducts a target-selection Q&A, downloads
  only relevant code and assets, hosts a local test server, and performs a visual audit. Invokable directly via /scrape-component.
argument-hint: '[optional parameters]'
---

# Scrape Component Skill

## Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/scrape-component [optional parameters]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills or subagents via `/scrape-component` or by reading `SKILL.md` directly.


Use this skill when the user likes a specific component, effect, or animation on a website and wants to extract only that element (and its dependencies) instead of mirroring the entire website.

## Phase 1: Clarification & Targeted Q&A (Do FIRST)

1. **Target Selection Interview:**
   - Execute a `/grill-me` style discovery session asking:
     1. *Which component, styling, or motion effect do you want to extract?* (e.g. the spring cursor, the draggable cards, a bento hover animation).
     2. *Where is it located on the page or what is its CSS selector?*
     3. *Is this for a Zorixel Brand Reference or a Premium Design Reference?*
     4. *Should we keep the isolated component files permanently in our AIOS reference vault, or delete them after creating the documentation?*
2. **Setup Folder Path:**
   - **Brand Reference:** Save under `second-brain-zorixel/wiki/research/components/[component-slug]/`.
   - **Premium Design Reference:** Save under `premium-frontend-experience-system/reference-inputs/components/[component-slug]/`.

## Phase 2: Isolated Extraction & Dependency Audit

1. **Selective Extraction Script:**
   - Write a Node.js script in the `scripts/` directory (e.g. `scripts/extract-[component-slug].js`) using Playwright to:
     - Load the URL.
     - Extract the target element's HTML structure.
     - Extract its computed CSS styles or find the specific stylesheet rules mapping to its selectors.
     - Inspect script imports and event listeners on the element to identify dynamic dependencies (e.g. GSAP hooks, canvas texture drawings).
     - Download only the specific assets (fonts, icons, SVGs, images) used by the component.
2. **Assemble Standalone Prototype:**
   - Package the HTML, CSS, JS, and assets into a single, self-contained prototype file (e.g. `index.html` and `style.css` in the component folder).

## Phase 3: Visual Verification & Auditing (Playwright Bypass)

1. **Local localhost Server:**
   - Run the workspace static server at `scripts/serve.js` in the background, passing the target component folder path as the argument:
     ```powershell
     node scripts/serve.js <absolute-path-to-component-folder> 3000
     ```
2. **Playwright Visual Verification:**
   - Open `http://localhost:3000` via the Playwright `browser_navigate` tool.
   - Verify that the component functions correctly, animations execute cleanly, and the browser console contains zero errors.
   - Take desktop and mobile screenshots of the component in active/hover states.

## Phase 4: Analysis & System Adaptation

1. **Write Analysis Document:**
   - Save a markdown analysis file (`analysis.md`) in the component folder outlining:
     - **Component Structure:** The HTML markup and layout logic.
     - **Style Tokens:** Spacing, fonts, and colors utilized.
     - **Motion Mechanics:** GSAP/CSS animation easing, timing, and trigg points.
     - **Integration Plan:** Concrete steps on how to rewrite and adapt the component into Zorixel's design tokens (Tailwind, Framer Motion, or GSAP Contexts).
2. **AIOS Upgrades:**
   - Update `premium-frontend-experience-system/POLICIES.md` or `DESIGN_DIRECTION.md` if the component introduces premium design patterns.
   - Run `/improve-system` to save lessons to `brain-aios/wiki/experiences/`.
   - Delete the raw files if the temporary retention policy was requested, leaving only the visual screenshots and `analysis.md` documentation.
3. **Roast Phase:**
   - Offer the user to run `/roast` to pressure-test the integration strategy.

---

## Inter-Skill Connections & Handoff Pipeline
- **Component Extraction**: Extracts specific UI components, animations, or styles from website URLs.
- **Vault Integration**: Saves extracted .tsx components into premium-frontend-experience-system/references/component-vault/.

---

## Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

