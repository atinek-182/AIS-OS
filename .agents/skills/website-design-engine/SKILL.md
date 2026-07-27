---
name: website-design-engine
description: Master 10-Phase Web Creation Engine. Synthesizes multi-page sitemap architecture, design system token extraction, 147 curated UI components, Motion Dialing (0-10), GSAP/ThreeJS WebGL fallbacks, zero-cost Nano Banana & Veo asset pipelines (with Unsplash fallback), Hallmark anti-slop gates, and 5-viewport Playwright visual QA into a zero-rush, JIT-loaded execution framework. Invokable directly via /website-design-engine.
argument-hint: '[optional parameters or target URL/brief]'
---

# 🚀 Website Design Engine (Master Web Creation Skill v2.2)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/website-design-engine [optional parameters]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves web design, frontend creation, or site generation.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills (`/new-project`, `/gstack`) or subagents via `/website-design-engine` or by reading `SKILL.md` directly.

> **Purpose:** Build distinctive, non-templated, world-class multi-page websites from scratch by orchestrating visual identity, 147 curated UI components, grid math, motion engineering, zero-cost asset generation, and Playwright multi-viewport visual QA—without context bloat, prompt fatigue, or rushing.

---

## ⛔ Non-Negotiable Core Mandates

1. **Global Zero-Hurry & Architectural Rigor Mandate**:  
   Never rush execution. Quality, option-based Q&A, wireframe planning, Playwright visual QA, pre-write audits, and pre-coding backstops take absolute precedence over speed. Stop at designated phase checkpoints.
2. **Just-In-Time (JIT) Phase Reference Loading**:  
   To prevent context bloat and "skill blindness", do NOT load multiple large skill files simultaneously. Load ONLY the specific 1-page reference file listed for the active phase.
3. **AUTOMATIC MANDATORY VAULT & PURE SKILLS READING**:  
   Do NOT wait for the user to tell you to use frontend vault references or pure skills. In Phase 1, Phase 2, and Phase 4, you MUST automatically execute `view_file` or `grep_search` on the target vault reference files before writing code.
4. **STRICT ZERO-COST MEDIA GENERATION GUARD**:  
   Only use Nano Banana (`generate_image`) or Google Veo (`credentials_personal.json`) if 100% covered under active free allocations or subscriptions. If ANY generation step asks for payment or extra billing (even ₹1), IMMEDIATELY abort AI generation and automatically use high-quality Unsplash image URLs (`https://images.unsplash.com/photo-...`) or CSS ambient video loops.
5. **Strict AI Slop & Generic Gradient Ban**:  
   - **BANNED**: Generic purple/blue gradient backgrounds (`bg-gradient-to-r from-purple-500 to-indigo-600`), floating blurred color blobs (`blur-3xl opacity-30 bg-purple-500`), invented fake metric cards ("+47% conversion", "50,000+ teams"), un-tokenized Hex/HSL strings, and default rounded-2xl cards.
   - **REQUIRED**: OKLCH color token math (1 primary accent, high-contrast neutrals), Stark typographic hierarchy, and Hallmark pre-emit critique headers.

---

## 🧭 10-Phase Execution Architecture

```
[Phase 0: Intent Discovery & Brief Q&A]    ──► Interactive Q&A (Audience, Vibe, Motion Dial 0-10)
[Phase 0.5: Sitemap & Shared Architecture] ──► Reads references/00-sitemap-and-architecture.md
[Phase 1: Brand, Tokens & Targeted Vault Ingestion]──► AUTOMATICALLY reads target granularity master in vault-references/
[Phase 2: Grid Canons & Obys Math]        ──► AUTOMATICALLY reads brain-aios/wiki/sops/grid-systems-sop.md
[Phase 3: Component Sourcing (147 Catalog)] ──► Executes python scripts/component_registry_cli.py search
[Phase 4: Motion, Shaders & Pure Skills]   ──► AUTOMATICALLY reads skills-library/gsap-skills/ or threejs-skills/
[Phase 4.5: Zero-Cost Asset Pipeline]     ──► Free Nano Banana/Veo OR Unsplash Fallback URLs
[Phase 5: Pre-Emit Anti-Slop, SEO & Security]──► Reads references/05-anti-slop-quality-gates.md & runs hallmark_runner.py
[Phase 6: Playwright 5-Viewport Visual QA] ──► Reads references/06-visual-qa-verification.md & runs verify_design_milestone.py
[Phase 7: Auto-Evolution & Memory Sync]    ──► Appends lessons to references/ & triggers /improve-system
```

---

## 📋 Step-by-Step Phase Instructions

### Phase 0: Interactive Brief & Intent Discovery
1. **If the brief is underspecified**, ask up to 3 tight clarifying questions:
   - **Target Audience & Job**: Who is this site for, and what is its primary CTA?
   - **Vibe Archetype**: Linear-Clean, Awwwards-Experimental, Editorial, Brutalist, Premium Consumer, or Dark Tech?
   - **Motion & Shader Intensity (Motion Dial 0–10)**: Static/Airy (Dial 0-3) vs Kinetic/GSAP (Dial 4-6) vs 3D/GLSL Canvas (Dial 7-10)?
2. Output a 1-line **Design Read**: *"Reading this as: [Page Kind] for [Audience], with [Vibe] language, Motion Dial [X], using [Macrostructure Archetype]."*

### Phase 0.5: Sitemap & Shared Architecture Scaffolding
1. Read `references/00-sitemap-and-architecture.md`.
2. Define route tree (`/`, `/about`, `/features`, `/pricing`, `/contact`).
3. Scaffold `RootLayout` with persistent responsive navigation, route indicator state, and shared global footer.

### Phase 1: Brand, Token Setup & Targeted Vault Ingestion
1. **AUTOMATIC MANDATORY STEP**: Target and call `view_file` on the specific visual DNA master manual matching the brief:
   - For Grid/Agency layouts: `premium-frontend-experience-system/vault-references/grids-obys-agency-granularity-master.md`
   - For Editorial/Studio layouts: `premium-frontend-experience-system/vault-references/sondaven-granularity-master.md`
   - For Dark Tech/SaaS layouts: `premium-frontend-experience-system/vault-references/oryzo-ai-granularity-master.md`
   - For Portfolio/Creative layouts: `premium-frontend-experience-system/vault-references/the-shift-tokyo-granularity-master.md`
2. Read `references/01-macrostructures-and-brand.md`. Select 1 of 21 Hallmark macrostructure archetypes.
3. Lock OKLCH color tokens in `index.css` (1 primary accent, stark neutrals, zero un-tokenized hex codes).

### Phase 2: Grid Canons & Obys Layout Math
1. **AUTOMATIC MANDATORY STEP**: Call `view_file` on `brain-aios/wiki/sops/grid-systems-sop.md`.
2. Read `references/02-layout-and-grid-rules.md`.
3. Apply Obys 4 Grid Canons & Vertical Rhythm (`leading-none`, `max-w-[65ch]`, grid baseline alignment).
4. Enforce Hero Stack Discipline (max 4 text elements; hero must fit in `100dvh` without forced scroll).

### Phase 3: Mandatory Component Sourcing (147 Catalog)
1. Read `references/03-component-catalog-guide.md`.
2. Query component catalog via CLI:
   `python scripts/component_registry_cli.py search <query>`
3. Select matching components from Aceternity UI, Animate UI React, Vengence UI, or Forge UI. Never write generic placeholder divs.

### Phase 4: Motion, Shaders & Mandatory Pure Skills Ingestion
1. Read `references/04-motion-and-shaders.md`.
2. **AUTOMATIC MANDATORY STEP**: If Motion Dial > 3, call `view_file` on:
   - For GSAP/ScrollTrigger: `brain-aios/wiki/research/skills-library/gsap-skills/SKILL.md`
   - For Three.js/WebGL: `brain-aios/wiki/research/skills-library/threejs-skills/SKILL.md`
3. Assemble layout using Tailwind CSS v4, Motion/React, GSAP ScrollTrigger skeletons, or Three.js GLSL shaders.
4. **Mandatory WebGL Fallback Guard**: Wrap all Three.js / Canvas elements with automatic CSS/2D canvas fallback wrappers (`SafeCanvas`) for low-power mobile or disabled WebGL contexts.

### Phase 4.5: Zero-Cost Asset Generation & Unsplash Fallback Pipeline
1. **Zero-Cost Audit**: Verify media generation is 100% free under subscription allocations. If any cost occurs, immediately switch to Unsplash.
2. **Image Assets**: Generate hero visuals via Nano Banana (`generate_image`). If unavailable or paid, use high-resolution Unsplash URLs (`https://images.unsplash.com/photo-...`).
3. **Video Assets**: For ambient hero backgrounds, generate via Google Veo using personal account context (`$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"`). If paid/unavailable, use CSS ambient video/gradient canvas loops.

### Phase 5: Pre-Emit Anti-Slop, SEO & Security Audit
1. Read `references/05-anti-slop-quality-gates.md`.
2. Run automated anti-slop audit:
   `python scripts/hallmark_runner.py`
3. Verify JSON-LD Schema markup, canonical meta tags, single `<h1>` enforcement, and `vibesec` security sanitization.
4. Stamp pre-emit critique header: `/* Hallmark · P5 H4 E5 S4 R5 V5 */`.

### Phase 6: Playwright Visual Verification & Responsive Sweep
1. Read `references/06-visual-qa-verification.md`.
2. Run automated multi-viewport verification:
   `python scripts/verify_design_milestone.py`
3. Confirm **0 console errors**, **0 unhandled 404s**, **0 horizontal overflow scrollbars**, and inspect screenshots across 5 viewports (Desktop 1920x1080, Laptop 1440x900, Tablet 768x1024, Mobile 375x812, Small Mobile 320x568). Cap auto-fix retries to max 2 passes.

### Phase 7: Continuous Self-Improvement & Auto-Evolution Protocol
1. **Identify Upgrade**: Update the relevant reference file in `references/`:
   - Sitemap / Shared Layouts -> `references/00-sitemap-and-architecture.md`
   - Brand / Tokens / Color -> `references/01-macrostructures-and-brand.md`
   - Grid / Spacing Rules -> `references/02-layout-and-grid-rules.md`
   - Components / Registry -> `references/03-component-catalog-guide.md`
   - Motion / WebGL Shaders -> `references/04-motion-and-shaders.md`
   - Anti-Slop / SEO / A11y -> `references/05-anti-slop-quality-gates.md`
2. **Auto-Persist**: Append new patterns directly to the reference file.
3. **System Memory Sync**: Suggest invoking `/improve-system` to save cross-session learnings to `MEMORY.md`.

---

## 📚 Mandatory Vault & Pure Skills Reading Registry

| Execution Phase | Target Vault / Skill File Path (AUTOMATIC READ MANDATE) |
| :--- | :--- |
| **Phase 1 (Agency/Grid DNA)** | [grids-obys-agency-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/grids-obys-agency-granularity-master.md) |
| **Phase 1 (Editorial DNA)** | [sondaven-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/sondaven-granularity-master.md) |
| **Phase 1 (Dark Tech DNA)** | [oryzo-ai-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/oryzo-ai-granularity-master.md) |
| **Phase 2 (Grid Systems)** | [grid-systems-sop.md](file:///d:/AI-OS/brain-aios/wiki/sops/grid-systems-sop.md) |
| **Phase 4 (GSAP Motion)** | [gsap-skills/SKILL.md](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/gsap-skills/SKILL.md) |
| **Phase 4 (Three.js WebGL)** | [threejs-skills/SKILL.md](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/threejs-skills/SKILL.md) |
| **Phase 5 (Hallmark Audit)** | [hallmark/SKILL.md](file:///d:/AI-OS/.agents/skills/hallmark/SKILL.md) |
| **Phase 5 (GStack QA)** | [gstack/SKILL.md](file:///d:/AI-OS/.agents/skills/gstack/SKILL.md) |
