# Six-File Context & Website Design Engine Integration: Brainstorm / Discovery Notes
Date: 2026-07-27 · Goal: Integrate the master 10-phase Website Design Engine (Awwwards-grade visual design, Obys grids, 147 components, motion dialing, Hallmark anti-slop, zero-cost media pipelines) into the 7-File Context Methodology & Senior AI Engineering System.

## Summary / key decisions
- **Skill Target**: Interlink `/website-design-engine` into `/six-file-context-methodology` skill, masterclass guide (`STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md`), and default `ui-context.md` / `code-standards.md` templates.
- **Integration Mode**: Option A — Full 10-Phase Pipeline Integration. Automatically runs token extraction, Obys grid math, and 147 component sourcing during context initialization.
- **Pure Frontend Boundaries**: `website-design-engine` handles 100% of pure frontend design (layouts, typography, motion 0-10, component sourcing, visual QA).
- **Flexible Template Rule**: Enforces Hallmark 57 anti-slop quality gates without restricting code to rigid or templated layouts.
- **Hybrid Motion Architecture**: Global motion rhythm & easing curves defined in `ui-context.md` for visual unity, paired with component-specific technology escalation (GSAP, Three.js, WebGL, Framer Motion, CSS) in individual feature specs.
- **Anti-Slop Hybrid Media Pipeline**: High-engineering AI prompts (`generate_image`) avoiding generic AI purple/glow slop, combined with curated Unsplash photography. Zero-cost fallback to Unsplash or user prompt if AI output risks slop or payment triggers.

## Q&A log
### Q1 — Website Design Engine Integration Strategy
- Asked: How should `website-design-engine` collaborate with `/six-file-context-methodology`?
- Captured: Option A — Full 10-Phase Pipeline Integration. `ui-context.md` and `code-standards.md` automatically ingest `website-design-engine`'s pure frontend pipeline (Obys grid math, OKLCH tokens, 147 component queries, Motion Dialing 0-10, Hallmark 57 anti-slop gates, zero-cost media fallbacks, Playwright 5-viewport QA) for all pure frontend work. Hallmark quality gates apply as visual standards without forcing rigid page template structures.
- Flags: None.

### Q2 — Hybrid Motion & Animation Architecture
- Asked: How should Motion Intensity Dialing (0-10) and component sourcing be configured?
- Captured: Hybrid Motion Architecture (Mix of Option A + Option B):
  1. Global Motion Rhythm (`ui-context.md`): Defines global easing curves (`cubic-bezier(0.16, 1, 0.3, 1)` / `power3.out`), transition timing, and visual DNA so all components feel unified on the page.
  2. Component-Specific Technology Escalation (`context/specs/NN-component.md`): Each component selects its tailored animation technology (GSAP ScrollTrigger for heroes, Three.js/WebGL for 3D stages, Framer Motion for UI widgets, CSS for buttons) while strictly obeying the global easing & visual feel.
- Flags: None.

### Q3 — Anti-Slop Hybrid Media Pipeline
- Asked: How should media assets (images/videos) be generated in pure frontend specs?
- Captured: Hybrid Option A + Option B with Anti-Slop Guardrails:
  1. High-Engineering AI Generation (`generate_image`): Use advanced anti-slop prompts (no plastic textures, no glowing purple hands, no generic stock AI look).
  2. Unsplash & Curated Free Image Sources: Use high-definition Unsplash URLs (`https://images.unsplash.com/photo-...`) whenever AI prompts risk slop or zero-cost payment triggers occur.
  3. User Option: Ask the user directly if custom brand images or specific assets are preferred.
- Flags: None.

## Open flags (pending input)
- None.


### Q4 — Contrarian Audit Resolution: Animation Bundle Size & Performance Guard
- Asked: How to prevent multi-library animation bloat (GSAP + Framer Motion + Three.js) from slowing down page loads?
- Captured: Enforced 3-tier Bundle Size & Script Tree Hygiene Guard:
  1. Tree-shaken modular imports for GSAP and Framer Motion.
  2. Dynamic lazy loading (`ssr: false`) with skeleton loaders for Three.js/WebGL canvases to preserve 100/100 Core Web Vitals.
  3. No duplicate library imports for basic UI widgets.
- Flags: None.
