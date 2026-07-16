---
name: design-direction
description: Generate a premium visual design direction file and run the adversarial roast council on the concept.
argument-hint: "[project-name]"
---

# Design Direction Generator

Use this skill to compile a premium visual style guide and design concept before writing layout or animation code.

## Triggering Rules
- Triggered when the user runs `/design-direction` or when a project brief is approved.
- Exclusively deals with website visual design; completely decoupled from Zorixel social carousel structures.

## Context Optimization Rule
- To avoid context bloat, the agent must **not** load the entire design system. Read only the specific target `PROJECT_BRIEF.md`, [[POLICIES.md]] (for tokens), and the specific files under `references/` related to the project type.

## Execution Steps

1. **Read Inputs**:
   - Locate and read `projects/[project_dir]/PROJECT_BRIEF.md`.
   - Resolve design tokens and curves from [[POLICIES.md]].

2. **Generate Design Direction**:
   - Compile a detailed `DESIGN_DIRECTION.md` under `projects/[project_dir]/`.
   - Incorporate the structured output format:
     - **Project Understanding**
     - **Core Visual Concept** (specific editorial, product, or brutalist concept)
     - **First 5-Second Impression**
     - **Typography Scale** (Major Third or Golden Ratio, letter spacing, font families)
     - **Color System** (semantic tokens, backgrounds, contrast ratios)
     - **Layout Grid & Spacing** (gutters, containers max-width `1440px`, screen margins)
     - **Component Styling** (Tailwind v4 tokens, borders, shadow styles)
     - **Motion Language** (Transitions, curves like `cubic-bezier(0.16, 1, 0.3, 1)`)
     - **WebGL/Shader Decision** (Justification, fallback, mobile behavior)
     - **Reference Principles** (adapted from [[godly-references.md]] or [[great-sites.md]])
     - **What to Avoid** (purple glowing blobs, default SaaS outlines, uppercase tracked eyebrows)
     - **Milestone 1 Scope** (Hero section plan)
     - **Design QA Scores** (1 to 10 scale for layout, type, color, motion, contrast)
   - Ensure the file contains relative Obsidian bracket links to parent manuals: `[[../../POLICIES.md]]` and `[[../../WORKFLOWS_AND_QA.md]]`.

3. **Convene Roast Council**:
   - Automatically compile a brief of this design direction.
   - Run the `/roast` adversarial council on the brief to stress-test the concept, identify fatal visual or technical flaws, and output a GO / RESHAPE verdict.
   - Append the council's scores and recommendations to the `DESIGN_DIRECTION.md` and log them in `decisions/log.md`.
