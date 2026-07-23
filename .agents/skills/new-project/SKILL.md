---
name: new-project
description: Initialize a new Premium Frontend website project. Scaffolds GSD project directories, copies design/asset briefs templates, and starts the discovery Q&A loop.
argument-hint: "[project-name]"
---

# New Project Initialization

Use this skill when starting a new premium frontend website project under the Premium Frontend Experience System.

## Triggering Rules
- Triggered when the user runs `/new-project` or asks to "start a new website project" or "initialize website".
- This skill deals exclusively with web layout structures (portfolios, landing pages, SaaS websites) and is **strictly decoupled** from Instagram/Zorixel brand graphics.

## Execution Steps

1. **Resolve Project Name & Path**:
   - Get the project name from arguments (e.g. `test-landing`).
   - Settle the path to: `projects/[project-name]`. (Verify if `projects/` folder exists at root; create it if not).

2. **Scaffold Directory Structure**:
   - Create directories:
     - `projects/[project-name]/`
     - `projects/[project-name]/design-briefs/`
     - `projects/[project-name]/assets-briefs/`
     - `projects/[project-name]/qa/`
     - `projects/[project-name]/src/` (if coding)

3. **Copy Streamlined Templates**:
   - Copy templates from `premium-frontend-experience-system/design-briefs/` to `projects/[project-name]/design-briefs/`.
   - Copy templates from `premium-frontend-experience-system/assets-briefs/` to `projects/[project-name]/assets-briefs/`.
   - Ensure the copied templates contain the relative Obsidian cross-links pointing back to `../../PROJECT_BRIEF.md`.

4. **Initialize Project Files**:
   - Create `projects/[project-name]/PROJECT_BRIEF.md` containing empty fields for the discovery answers.
   - Create a base GSD `PROJECT.md` at the root of `projects/[project-name]/` outlining the 4 Milestones:
     - Milestone 1: Hero Section
     - Milestone 2: Page Subsections
     - Milestone 3: Motion Choreography
     - Milestone 4: Visual Polish & QA

5. **Start Discovery Q&A & Apply Hallmark Engine (`/hallmark`)**:
   - Run the `/grill-me` slash command or ask the 10 Project Discovery questions defined in [[INTAKE_AND_REFERENCES.md]]:
     1. What is the website name and type?
     2. What is the primary goal?
     3. Who is the target audience?
     4. What should the first 5 seconds feel like?
     5. Which reference URLs or layouts should guide the design? (If URLs/screenshots are provided, run `/hallmark study <target>` to extract design DNA into `design.md`).
     6. What sections are needed? (Select a layout archetype from Hallmark's 21 macrostructures rather than standard hero-3feature-CTA templates).
     7. Should it support Dark mode, Light mode, or both? (Select an OKLCH theme palette from Hallmark's 20 themes or custom engine).
     8. What is the motion language?
     9. Are WebGL, 3D assets, or custom shaders needed or optional?
     10. What elements, colors, or layouts must be avoided? (Enforce Hallmark's 57 anti-slop test gates).

6. **Validate**:
   - Ensure all files are written correctly and run `python scripts/hallmark_runner.py audit <project-dir>` and the pre-commit link validation check to verify all links inside `projects/[project-name]/` are active.

