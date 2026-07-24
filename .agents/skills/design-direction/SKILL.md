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

2. **Generate Design Direction (Hallmark Anti-Slop System)**:
   - Compile a detailed `DESIGN_DIRECTION.md` under `projects/[project_dir]/`.
   - Select a macrostructure layout archetype from Hallmark's 21 catalog patterns (e.g. `split-hero-stage`, `bento-stage`, `asymmetric-editorial`, `ticker-grid`) rather than generic SaaS layout templates.
   - Select a color palette from Hallmark's 20 OKLCH themes or construct a custom OKLCH palette.
   - Incorporate the structured output format:
     - **Project Understanding**
     - **Core Visual Concept & Hallmark Macrostructure** (selected from 21 macrostructure archetypes)
     - **First 5-Second Impression**
     - **Typography Scale** (Major Third or Golden Ratio, letter spacing, font families)
     - **Color System & OKLCH Theme** (semantic tokens, backgrounds, locked OKLCH theme variables)
     - **Layout Grid & Spacing (Obys Agency Canons)** (Selected archetype: 12/10/8 Column Grid with 30px/60px/80px margins & 20px gutters, Van De Graaff Golden Canon with diagonal Power Lines, Rectangular/Modular Grid, or Horizontal Baseline Rhythm with $\text{fontSize} \times \text{lineHeight}$ unit math)
     - **Component Styling** (Tailwind v4 tokens, borders, shadow styles)
     - **Motion Language** (Transitions, curves like `cubic-bezier(0.16, 1, 0.3, 1)`)
     - **WebGL/Shader Decision** (Justification, fallback, mobile behavior)
     - **Reference Principles** (adapted from [[godly-references.md]] or [[great-sites.md]])
     - **What to Avoid (57 Slop Gates)** (fake invented metrics, generic purple/blue gradients, default SaaS outlines, uppercase tracked eyebrows)
     - **Milestone 1 Scope** (Hero section plan)
     - **Design QA & Hallmark Pre-Emit Critique** (6-axis pre-emit self-critique: Philosophy, Hierarchy, Execution, Specificity, Restraint, Variety)
   - Ensure the file contains relative Obsidian bracket links to parent manuals: `[[../../POLICIES.md]]` and `[[../../WORKFLOWS_AND_QA.md]]`.

3. **Convene Roast Council & Run Hallmark Audit**:
   - Automatically compile a brief of this design direction.
   - Run `python scripts/hallmark_runner.py audit projects/[project_dir]/` to verify zero slop-test violations.
   - Run the `/roast` adversarial council on the brief to stress-test the concept, identify fatal visual or technical flaws, and output a GO / RESHAPE verdict.
   - Append the council's scores, Hallmark audit results, and recommendations to `DESIGN_DIRECTION.md` and log them in `decisions/log.md`.

