---
name: website-design-engine
description: Unified master website creation engine. Synthesizes 13 design skills,
  147 curated UI components, Obys grid math, Hallmark anti-slop gates, and 5-viewport
  visual QA into a self-improving phase-gated execution pipeline for building websites
  from scratch. Invokable directly via /website-design-engine.
argument-hint: '[optional parameters]'
---



# 🚀 Website Design Engine (Master Web Creation Skill)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/website-design-engine [optional parameters]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills or subagents via `/website-design-engine` or by reading `SKILL.md` directly.


> **Purpose:** Build distinctive, non-templated, world-class websites from scratch by orchestrating visual identity, 147 curated UI components, grid math, motion engineering, and Playwright visual QA without instruction fatigue or prompt bloat.

---

## 🧭 Phase-Gated Execution Architecture

To prevent instruction collision and token fatigue, follow this **8-Phase Sequence**. Load reference files ONLY during the active phase:

```
[Phase 0: Intent Discovery Q&A]     ──► Interactive Q&A or Brief Confirmation
[Phase 1: Concept & Brand Read]     ──► Reads references/01-macrostructures-and-brand.md
[Phase 2: Grid & Layout Math]       ──► Reads references/02-layout-and-grid-rules.md
[Phase 3: Component Sourcing]        ──► Executes python scripts/component_registry_cli.py search
[Phase 4: Code Assembly & Motion]    ──► Reads references/04-motion-and-shaders.md (if needed)
[Phase 5: Pre-Emit Quality Audit]    ──► Reads references/05-anti-slop-quality-gates.md & runs hallmark_runner.py
[Phase 6: Playwright Visual QA]     ──► Reads references/06-visual-qa-verification.md & runs verify_design_milestone.py
[Phase 7: Auto-Evolution & Memory]   ──► Appends new lessons, components & rules to references/
```

---

## 📋 Step-by-Step Phase Instructions

### Phase 0: Interactive Brief & Intent Discovery
Before writing code or selecting templates, conduct a targeted discovery pass:
1. **If the brief is underspecified**, ask up to 3 tight clarifying questions:
   - **Target Audience & Job**: Who is this site for, and what is its single primary action/CTA?
   - **Vibe & Aesthetic Risk**: Linear-clean, Awwwards-experimental, Editorial, Brutalist, Premium Consumer, or Dark Tech?
   - **Motion & Shader Intensity**: Static/Airy (Dial 3) vs Kinetic/GSAP (Dial 6) vs 3D/GLSL Canvas (Dial 8)?
2. **If context is clear**, output a 1-line **Design Read**:
   - *"Reading this as: [Page Kind] for [Audience], with [Vibe] language, using [Macrostructure Archetype]."*

### Phase 1: Concept, Macrostructure & Brand Token Setup
1. Read `references/01-macrostructures-and-brand.md`.
2. Select 1 of 21 Hallmark macrostructure archetypes.
3. Lock brand typography (Nuqun for logo, Rosehot for display headings, Outfit/Geist for body text).
4. Establish OKLCH color tokens (1 primary accent, high-contrast neutrals, zero un-tokenized hex codes).

### Phase 2: Grid Canons & Layout Architecture
1. Read `references/02-layout-and-grid-rules.md`.
2. Apply Obys 4 Grid Canons & Vertical Rhythm math (`leading-none`, `max-w-[65ch]`, grid baseline alignment).
3. Enforce Hero Stack Discipline (max 4 text elements; hero must fit in 100dvh viewport without forced scroll).
4. Enforce Eyebrow Restraint (max 1 eyebrow per 3 sections) and Section-Layout-Repetition Ban.

### Phase 3: Mandatory Component Sourcing (147 Catalog)
1. Read `references/03-component-catalog-guide.md`.
2. Execute CLI query for required sections:
   `python scripts/component_registry_cli.py search <query>`
3. Select matching components from the **147 catalog** (Aceternity UI, Animate UI React, Vengence UI, Forge UI) or Shadcn MCP. Do NOT write generic placeholder divs.

### Phase 4: Code Assembly, Motion & Shader Engineering
1. If motion/WebGL is required, read `references/04-motion-and-shaders.md`.
2. Assemble layout using Tailwind CSS v4, Motion/React, GSAP ScrollTrigger skeletons (Sticky-Stack, Horizontal-Pan), or Three.js GLSL shaders.
3. Apply `vibesec` sanitization and `react-performance` optimization (`useMotionValue` instead of `useState` on scroll).

### Phase 5: Pre-Emit Anti-Slop & Accessibility Audit
1. Read `references/05-anti-slop-quality-gates.md`.
2. Execute automated anti-slop audit runner:
   `python scripts/hallmark_runner.py`
3. Stamp the pre-emit critique header: `/* Hallmark · P5 H4 E5 S4 R5 V5 */`.
4. Verify WCAG AA contrast (4.5:1 text, 3:1 large text) and keyboard focus rings.

### Phase 6: Playwright Visual Verification & Responsive Sweep
1. Read `references/06-visual-qa-verification.md`.
2. Run automated multi-viewport verification:
   `python scripts/verify_design_milestone.py`
3. Confirm 0 console errors and inspect screenshots across 5 viewports (Desktop 1920x1080, Laptop 1440x900, Tablet 768x1024, Mobile 375x812, Small Mobile 320x568).

### Phase 7: Continuous Self-Improvement & Auto-Evolution Protocol (MANDATORY)
After completing any design session, or whenever the user introduces a new design pattern, asset, correction, or reference:
1. **Identify the Lesson / Upgrade**: Determine which reference file needs updating:
   - Macrostructure / Brand / Palette -> `references/01-macrostructures-and-brand.md`
   - Layout / Grid / Spacing Rule -> `references/02-layout-and-grid-rules.md`
   - New Component / Library -> `references/03-component-catalog-guide.md`
   - Motion Skeleton / Shader -> `references/04-motion-and-shaders.md`
   - Anti-Slop Gate / A11y / Security -> `references/05-anti-slop-quality-gates.md`
2. **Auto-Persist**: Append the new rule, code snippet, or constraint directly to the target reference file.
3. **Trigger System Self-Improvement**: Suggest invoking `/improve-system` to save cross-session learnings to `MEMORY.md`.

---

## 📚 On-Demand Deep Skill & Skills-Library Escalation

If any phase requires specialized, deep-dive technical guidance beyond the phase reference summaries, inspect the full skill file or vault reference manual:

| Requirement | Deep Skill / Vault Reference Path |
| :--- | :--- |
| **Full Hallmark Anti-Slop System** | [hallmark/SKILL.md](file:///d:/AI-OS/.agents/skills/hallmark/SKILL.md) & [skills-library/hallmark/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/hallmark/) |
| **Full GSAP Motion & ScrollTrigger** | [gsap-animation/SKILL.md](file:///C:/Users/HP/.gemini/config/skills/gsap-animation/SKILL.md) & [skills-library/gsap-skills/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/gsap-skills/) |
| **Full Three.js & GLSL Shaders** | [threejs-webgl/SKILL.md](file:///C:/Users/HP/.gemini/config/skills/threejs-webgl/SKILL.md) & [skills-library/threejs-skills/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/threejs-skills/) |
| **Full GStack Executive Review** | [gstack/SKILL.md](file:///d:/AI-OS/.agents/skills/gstack/SKILL.md) & [skills-library/gstack/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/gstack/) |
| **Full UI/UX Pro Max Rules** | [ui-ux-pro-max/SKILL.md](file:///C:/Users/HP/.gemini/config/skills/ui-ux-pro-max/SKILL.md) |
| **Full Accessibility Audit** | [accesslint-a11y/SKILL.md](file:///C:/Users/HP/.gemini/config/skills/accesslint-a11y/SKILL.md) |
| **Obys Grid Systems SOP** | [grid-systems-sop.md](file:///d:/AI-OS/brain-aios/wiki/sops/grid-systems-sop.md) |
