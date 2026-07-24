# Unified AI OS Design System Engine: Brainstorm & Planning
Date: 2026-07-24 · Goal: Create a unified website-creation master skill (`website-design-engine`) that integrates all web design skills, 147 components, site teardowns, workflows, and quality gates for building websites from scratch without breakage.

## Summary / Key Decisions
1. **Target Scope**: Focus strictly on building **new websites from scratch**.
2. **Consolidated Skill Ingestion**: Integrate 13 design skills (`frontend-design`, `taste`, `design-is`, `design-loop-controlled`, `ui-ux-pro-max`, `gsap-animation`, `threejs-webgl`, `tailwind-patterns`, `browser-testing`, `vercel-web-design-guidelines`, `react-performance`, `remotion`, `impeccable`), removing bloat & duplicate rules.
3. **Reference Exclusions**: Exclude `premium-frontend-experience-system/references/` from this master skill as it is outdated and poorly structured.
4. **Interactive Brief Discovery (Phase 0)**: Before generating any code, the skill conducts a brief, structured Q&A (or infers and presents a 1-line Design Read for confirmation) to pin down website goal, audience, vibe/aesthetic risk, key sections, and motion intensity level.
5. **Phase-Gated Progressive Disclosure**: `SKILL.md` is a lightweight orchestrator (< 150 lines). It instructs the agent to read reference files in `references/` ONLY during the specific phase where they apply.
6. **Deterministic Script Offloading**: Shift heavy quality audits (57 Hallmark gates, 5-viewport screenshot sweep) to Python runner scripts (`hallmark_runner.py`, `verify_design_milestone.py`).

## 7-Phase Execution Architecture

```
Phase 0: Interactive Brief & Intent Discovery ──► Target Q&A / Design Read Confirmation
Phase 1: Concept & Design Read             ──► Reads references/01-macrostructures-and-brand.md
Phase 2: Grid & Layout Architecture        ──► Reads references/02-layout-and-grid-rules.md
Phase 3: Component Sourcing                ──► Executes python scripts/component_registry_cli.py search
Phase 4: Code Assembly & Motion            ──► Reads references/04-motion-and-shaders.md (if needed)
Phase 5: Pre-Emit Anti-Slop Audit          ──► Runs python scripts/hallmark_runner.py
Phase 6: Playwright Visual QA               ──► Runs python scripts/verify_design_milestone.py (5 viewports)
```

## Approved File Structure

```
d:\AI-OS\.agents\skills\website-design-engine\
├── SKILL.md                          <-- (Lightweight Master Orchestrator, < 150 lines)
└── references\
    ├── 01-macrostructures-and-brand.md <-- (Hallmark 21 archetypes, Zorixel brand fonts, OKLCH themes)
    ├── 02-layout-and-grid-rules.md     <-- (Obys 4 Canons, vertical rhythm, ui-ux-pro-max layout rules)
    ├── 03-component-catalog-guide.md   <-- (147 component CLI integration & sourcing rules)
    ├── 04-motion-and-shaders.md        <-- (GSAP ScrollTrigger skeletons, Three.js GLSL, Motion/React)
    ├── 05-anti-slop-quality-gates.md   <-- (Hallmark 57 gates, Dieter Rams 10 principles, Vercel guidelines)
    └── 06-visual-qa-verification.md    <-- (Playwright 5-viewport screenshot sweep & console checks)
```
