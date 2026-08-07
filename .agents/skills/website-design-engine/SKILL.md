---
name: website-design-engine
description: Master 10-Phase Web Creation Engine v3.0. Synthesizes project-local reference/ priority vault (#1 source of truth), Six-File Context layout specifications (zero auto-wireframes), categorized favorite component precedence, interactive Radiant Shaders (pbakaus/radiant) HTML extraction protocol, Obys grid math, Hallmark anti-slop gates, /jsmastery-audit App Router audits, and 5-viewport Playwright visual QA into a zero-rush execution framework. Invokable via /website-design-engine.
argument-hint: '[optional parameters or target URL/brief]'
---

# 🚀 Website Design Engine (Master Web Creation Skill v3.0)

## ⚡ Invocation & Tri-Mode Routing

This skill builds distinctive, non-templated, world-class multi-page websites from scratch by orchestrating project-local `reference/` assets, categorized favorite UI components, Obys grid math, interactive WebGL shaders (`radiant-shaders`), and Playwright multi-viewport visual QA.

Invokable via:
- **Slash Command**: `/website-design-engine [brief_or_url]`
- **Dynamic Intent**: Triggered automatically when creating web applications, landing pages, agency sites, or digital product UIs.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills (`/new-project`, `/gstack`, `/six-file-context-methodology`) or subagents.

---

## 🎯 Specific Use Cases
- **ZORIXEL Product Landing Pages & Web Apps**: Create high-converting Next.js / Vite React applications featuring `Nuqun` logo typography, `Lenis` smooth inertia scroll, OKLCH color math, and custom scrollytelling.
- **Client Conversion Flagships**: Build full multi-page applications (`/`, `/work`, `/about`, `/pricing`, `/contact`) driven by local `reference/` assets and 5-viewport visual QA verification.

---

## ⛔ Non-Negotiable Core Mandates

1. **Global Zero-Hurry & Methodical Step-by-Step Mandate**:  
   Never rush execution or build everything in a single un-checked step. Quality, deep option-based Q&A (`/grill-me`), pre-write `/roast` council audit, and Playwright visual QA take absolute precedence. If there is even the slightest doubt, stop and ask the user.
2. **Project-Local `reference/` Priority Vault Protocol (#1 Source of Truth)**:  
   Inside every project directory, the `reference/` (or `references/`) folder is the **#1 Priority Source of Truth**. Before selecting components or generating styles, the AI MUST scan `reference/` for screenshots (`.png`, `.jpg`, `.webp`), screen recordings (`.mp4`), HTML gallery files, TSX/CSS component code, and design briefs. Local reference assets ALWAYS take precedence over generic catalog entries.
3. **Six-File Layout Control (No Auto-Wireframe Generation)**:  
   Do NOT generate standalone automatic wireframes. Wireframes, component layouts, and route structures are explicitly defined in project context files via the **Six-File Context Methodology** (`six-file-context-methodology`).
4. **Categorized Favorite Component Precedence**:  
   When sourcing components beyond local `reference/` files, prioritize operator favorite components (`is_favorite: true`) within each category (hero, navigation, bento, pricing, cards, scrollytelling, footers) via `component_registry_cli.py search`.
5. **Interactive Radiant Shader HTML Protocol (`pbakaus/radiant`)**:  
   Never auto-generate `.tsx` shader components blindly. When a WebGL background or generative graphic is considered in Phase 4, the AI MUST explicitly ask the user: *"Would you like a WebGL shader background here? If yes, which shader from radiant-shaders.com gallery?"* The user will place the HTML file into `reference/`, and the AI will extract and adapt the WebGL shader code directly from that HTML file.
6. **Just-In-Time (JIT) Phase Reference Loading**:  
   To prevent context bloat and "skill blindness", load ONLY the specific 1-page reference file listed for the active phase (`references/00-06.md`).
7. **Strict AI Slop & Generic Gradient Ban**:  
   Ban generic purple/blue gradients (`bg-gradient-to-r from-purple-500 to-indigo-600`), floating blurred color blobs (`blur-3xl opacity-30 bg-purple-500`), invented fake metric cards ("+47% conversion", "50,000+ teams"), un-tokenized Hex/HSL strings, and default rounded-2xl cards. Enforce OKLCH color math, stark typography, and Hallmark pre-emit critique headers.

---

## 🧭 10-Phase Execution Architecture (v3.0)

```
[Phase 0: Socratic Intent Discovery]       ──► /grill-me (Audience, Vibe, Motion Dial 0-10)
[Phase 0.2: Adversarial Pre-Build Audit]   ──► /roast (5-persona council: Contrarian, Bull, Logician, Researcher, Buyer)
[Phase 0.5: Six-File Architecture Specs]   ──► /six-file-context-methodology & /jsmastery-architect (Layouts from Six-File)
[Phase 1: Local Reference Vault & Tokens]  ──► AUTOMATICALLY scans project reference/ folder + OKLCH brand tokens
[Phase 2: Grid Canons & Obys Math]         ──► AUTOMATICALLY reads brain-aios/wiki/sops/grid-systems-sop.md & 23-SITES matrix
[Phase 3: Priority Component Sourcing]    ──► Local reference/ code -> Categorized Favorites -> 300+ Component Catalog
[Phase 4: Motion & Radiant Shader Protocol] ──► Interactive Q&A for Radiant Shaders (extract from reference/*.html)
[Phase 4.5: Zero-Cost Asset Pipeline]      ──► Free Nano Banana/Veo OR Unsplash Fallback URLs
[Phase 5: Pre-Emit Anti-Slop & Code Audit] ──► /jsmastery-audit (App Router, Security, Types) & hallmark_runner.py
[Phase 6: Playwright 5-Viewport Visual QA] ──► verify_design_milestone.py (320px to 1920px 0-regression check)
[Phase 7: Auto-Evolution & Six-File Sync]  ──► Syncs learnings to references/ & triggers /six-file-context-methodology sync
```

---

## 📋 Step-by-Step Phase Instructions

### Phase 0: Socratic Intent Discovery (`/grill-me`)
1. Run `/grill-me` on core project requirements:
   - Target Audience & Job: Who is this site for, and what is its primary CTA?
   - Vibe Archetype: Linear-Clean, Awwwards-Experimental, Editorial, Brutalist, Premium Consumer, or Dark Tech?
   - Motion & Shader Intensity (Motion Dial 0–10): Static/Airy (Dial 0-3) vs Kinetic/GSAP (Dial 4-6) vs WebGL Canvas (Dial 7-10)?
   - Domain Vocabulary: Resolve key terms using `/mattpocock-domain-modeling`.
2. Output a 1-line **Design Read**: *"Reading this as: [Page Kind] for [Audience], with [Vibe] language, Motion Dial [X], using [Macrostructure Archetype]."*

### Phase 0.2: Adversarial Roast Council Audit (`/roast`)
Run `/roast` on visual concepts, layout plans, and business targets before touching code. Obtain a **GO / RESHAPE** verdict.

### Phase 0.5: Six-File Architecture & Build Spec (`/six-file-context-methodology`)
1. Read `references/00-sitemap-and-architecture.md` and project context files in `context/`.
2. Do NOT generate automatic wireframe images/HTML. Use the layout specifications defined in `context/ui-context.md` and `context/specs/`.
3. Scaffold `RootLayout` with persistent responsive navigation, route indicator state, and shared global footer.

### Phase 1: Local `reference/` Vault Scanning & Brand Tokens
1. **AUTOMATIC MANDATORY STEP — Local Reference Scan**:
   - Inspect project-local `reference/` (or `references/`) folder.
   - Parse screenshots (`.png`, `.jpg`), screen recordings (`.mp4`), HTML gallery files, TSX/CSS snippets, and markdown briefs. Extract exact visual rules, color cues, and custom component layout instructions.
2. **AUTOMATIC MANDATORY STEP — Visual DNA Master Ingestion**:
   - For Grid/Agency layouts: `premium-frontend-experience-system/vault-references/grids-obys-agency-granularity-master.md`
   - For Editorial/Studio layouts: `premium-frontend-experience-system/vault-references/sondaven-granularity-master.md`
   - For Dark Tech/SaaS layouts: `premium-frontend-experience-system/vault-references/oryzo-ai-granularity-master.md`
   - For Portfolio/Creative layouts: `premium-frontend-experience-system/vault-references/the-shift-tokyo-granularity-master.md`
3. Read `references/01-macrostructures-and-brand.md`. Select 1 of 21 Hallmark macrostructure archetypes.
4. Lock OKLCH color tokens in `index.css` (1 primary accent, stark neutrals, zero un-tokenized hex codes).

### Phase 2: Grid Canons & Obys Layout Math
1. **AUTOMATIC MANDATORY STEP**: Call `view_file` on `brain-aios/wiki/sops/grid-systems-sop.md`.
2. Read `references/02-layout-and-grid-rules.md`.
3. Apply Obys 4 Grid Canons & Vertical Rhythm ($\text{fontSize} \times \text{lineHeight}$, `leading-none`, `max-w-[65ch]`, grid baseline alignment).
4. Enforce Hero Stack Discipline (max 4 text elements; hero must fit in `100dvh` without forced scroll).

### Phase 3: Priority Component Sourcing (Local Reference -> Favorites -> 300+ Catalog)
1. Read `references/03-component-catalog-guide.md` and `premium-frontend-experience-system/references/component-vault/INDEX.md`.
2. Check priority sources in order:
   - **Level 1**: Code snippets / HTML / TSX supplied in local project `reference/` folder.
   - **Level 2**: Search operator favorite components (`is_favorite: true`) in `component_registry_cli.py search-pattern <category>`.
   - **Level 3**: Search full 300+ Component Catalog across 11 registries.
3. Select matching components for each layout section. Never write generic placeholder divs.

### Phase 4: Motion, Pure Skills & Interactive Radiant Shader Protocol
1. Read `references/04-motion-and-shaders.md` and `premium-frontend-experience-system/references/shader-canvas-vault/INDEX.md`.
2. **AUTOMATIC MANDATORY STEP**: If Motion Dial > 3, call `view_file` on:
   - For Dedicated GLSL Shaders & Physics: `premium-frontend-experience-system/references/shader-canvas-vault/INDEX.md`
   - For GSAP/ScrollTrigger: `brain-aios/wiki/research/skills-library/gsap-skills/SKILL.md`
   - For Three.js/WebGL: `brain-aios/wiki/research/skills-library/threejs-skills/SKILL.md`
3. **Interactive Radiant Shaders Check**:
   - Ask user if a WebGL shader background is desired.
   - User places the HTML file from `radiant-shaders.com` gallery into `reference/`.
   - Extract raw WebGL shader code cleanly from the user-provided HTML file into a React/Vite canvas wrapper.
4. **Mandatory WebGL Fallback Guard**: Wrap canvas elements with automatic CSS/2D canvas fallback wrappers (`SafeCanvas`).

### Phase 4.5: Zero-Cost Asset Generation & Unsplash Fallback Pipeline
1. **Zero-Cost Audit**: Verify media generation is 100% free under subscription allocations. If any cost occurs, immediately switch to Unsplash.
2. **Image Assets**: Generate hero visuals via Nano Banana (`generate_image`). If unavailable or paid, use high-resolution Unsplash URLs (`https://images.unsplash.com/photo-...`).

### Phase 5: Pre-Emit Anti-Slop & Fullstack Code Audit (`/jsmastery-audit` + `/hallmark`)
1. Read `references/05-anti-slop-quality-gates.md`.
2. Execute `/jsmastery-audit` checking Server Action inputs (Zod), `'use client'` boundaries, and type safety.
3. Run `python scripts/hallmark_runner.py audit <project-dir>`. Ensure pre-emit self-critique score header is stamped (`/* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */`).

### Phase 6: Playwright 5-Viewport Visual QA
1. Read `references/06-visual-qa-verification.md`.
2. Run `python scripts/verify_design_milestone.py` across 5 viewports (320px, 375px, 768px, 1024px, 1920px).
3. Inspect compiled screenshots side-by-side to guarantee visual parity with designs, and confirm 0 text wrapping or scaling regressions.

### Phase 7: Auto-Evolution, Memory & Six-File Handoff
1. Persist design lessons into `references/`.
2. Sync workflow updates with `/six-file-context-methodology`.
3. Suggest running `/improve-system`.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Project Setup & Context**: Started by **`/new-project`** and **`/six-file-context-methodology`**.
- **Discovery & Validation**: Driven by **`/grill-me`** and **`/roast`**.
- **Architecture, Macro Planning & Scoping**: Guided by **`/jsmastery-architect`**, **`/mattpocock-wayfinder`**, **`/jsmastery-scope`**, and **`/mattpocock-to-spec`**.
- **Component & Motion Sourcing**: Uses project `reference/` folder, `scripts/component_registry_cli.py`, `radiant-shaders` HTML files, `shader-canvas-vault`, and `skills-library/gsap-skills/`.
- **Verification & QA**: Executed by **`/verify-design`**, **`/jsmastery-audit`**, **`/gstack`**, and `scripts/verify_design_milestone.py`.

---

## 🔄 Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

