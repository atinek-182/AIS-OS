---
name: six-file-context-methodology
description: Apply Senior AI Engineering 7-File Context Methodology, Spec-Driven Development, Playwright Visual QA, and Global Zero-Hurry Mandate (from JavaScript Mastery masterclass). Use when initializing new projects, structuring AI coding context, or creating feature specifications.
argument-hint: '[init|scaffold|spec <feature-name>|spec-all|verify|check]'
---

# ⚡ Six-File Context Methodology (`/six-file-context-methodology`)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/six-file-context-methodology [init|scaffold|spec <feature-name>|spec-all|verify]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description (e.g. "scaffold context", "7-file context", "feature spec", "senior AI workflow").
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills (e.g. `/new-project`, `/make-plan`) or subagents via `/six-file-context-methodology` or reading `SKILL.md` directly.

---

## 🛡️ Addressed Vulnerabilities & Quality Fixes (From Roast Council Audit)

1. **Lite Mode vs Pro Mode Selector (Eliminates Build-Tooling Tax)**:
   - **Pro Mode (Default for Full SaaS)**: Scaffolds the full 7-File Context System (`project-overview.md`, `architecture.md`, `code-standards.md`, `ui-context.md`, `ai-workflow-rules.md`, `progress-tracker.md`, `seo-context.md` + root `AGENTS.md`) and handles unbounded 10-50+ feature specs.
   - **Lite Mode (For Micro-Tools & Landing Pages)**: Scaffolds a 4-File Minimal System (`project-overview.md`, `architecture.md`, `ui-context.md`, `progress-tracker.md`) + 3-5 specs to eliminate setup overhead on small 1-day builds.

2. **Token Footprint & Prompt Context Optimization**:
   - To avoid token context churn, the agent reads only relevant context files during specific sub-tasks:
     - *UI Tasks*: Reads `ui-context.md` + `code-standards.md`.
     - *DB / API Tasks*: Reads `architecture.md` + `code-standards.md` + `vibesec` security rules.
     - *SEO Tasks*: Reads `seo-context.md` + `seo-audit-reference/` vault.

3. **State Synchronization & Drift Prevention**:
   - Automated check during `/six-file-context-methodology check` comparing git commit history against `progress-tracker.md` entries to prevent stale documentation.

---

## 📌 Hard-and-Fast System Mandates

1. **Global Zero-Hurry Rule**: Never rush execution. Systems take time (weeks/months). Architectural rigor, deep questioning, and web research take precedence over speed.
2. **Interactive Architect Discovery (`init`)**: Run Playbook prompts in an interactive option-based Q&A loop before writing context files. Offers **Lite Mode vs Pro Mode** choice.
3. **7-File Context Foundation (Pro Mode)**:
   - `context/project-overview.md`
   - `context/architecture.md`
   - `context/code-standards.md`
   - `context/ui-context.md` (Integrated with 147 components from Aceternity, Animate UI, Forge UI, Vengence UI)
   - `context/ai-workflow-rules.md`
   - `context/progress-tracker.md`
   - `context/seo-context.md` (Integrated with 23-skill SEO skills-library vault)
   - Root `AGENTS.md` / `CLAUDE.md`
4. **Dynamic Unbounded Specs (`spec-all`)**: Generate all feature specs upfront (can be 10, 15, 20, 40, 50+ specs).
5. **Mandatory Pre-Write `/roast` Council**: Run `/roast` gatekeeper audit before creating any document file.
6. **Playwright Visual QA Engine (`verify`)**: Run Playwright CLI headless browser screenshots and console audits for every spec unit.
7. **Explicit Tracker Confirmation**: Ask user confirmation before updating `progress-tracker.md`.
8. **Pre-Coding Backstop**: Always ask: *"Is there anything else remaining before we touch the code?"*

10. **Website Design Engine Integration (`website-design-engine` v2.2)**:
    - *Pure Frontend Boundary*: `website-design-engine` powers 100% of pure frontend design (layouts, typography, motion, component sourcing, visual QA).
    - *Flexible Template Rule*: Enforces Together AI Hallmark 57 anti-slop quality gates as visual standards without forcing rigid or templated code structures.
    
    - *Bundle Size & Script Hygiene Guard (Contrarian Fix)*:
      1. Zero-Duplicate Libraries: Never mix Framer Motion and GSAP for simple widgets when one suffices.
      2. Tree-Shaking Discipline: Use modular imports (`import { gsap } from 'gsap'`) — never import un-shaken full bundles.
      3. Dynamic Lazy Loading: Heavy 3D WebGL components (`Three.js`) or complex GSAP timelines MUST use dynamic lazy imports (`ssr: false`) with a lightweight fallback skeleton to guarantee 100/100 Core Web Vitals page speed.
    - *Hybrid Motion Architecture*: `ui-context.md` sets global motion rhythm & easing curves (`cubic-bezier(0.16, 1, 0.3, 1)` / `power3.out`) for visual cohesion across the entire site. Individual feature specs (`NN-component.md`) escalate to specialized animation tech (GSAP ScrollTrigger, Three.js WebGL shaders, Framer Motion, CSS) while strictly obeying the global easing DNA.
    - *Component Sourcing*: Queries 147 cataloged components from Aceternity UI, Animate UI React, Forge UI, Vengence UI via `python scripts/component_registry_cli.py search <query>`.
    - *Anti-Slop Hybrid Media Pipeline*: Uses high-engineering prompts for `generate_image` (no plastic textures or generic purple AI slop), paired with high-definition Unsplash URLs (`https://images.unsplash.com/photo-...`) and automatic zero-cost fallbacks.
9. **Security-First & Auto-Skill Ingestion Mandate**: Security is top priority. Always apply `/vibesec` rules (IDOR, JWT HttpOnly cookies, Zod Mass Assignment validation, SSRF private IP blocking). Automatically detect, scan, and apply ANY present or future security/backend skill in `.agents/skills/` or `skills-library/` during planning, spec generation, and pre-write `/roast` audits.

---

## 🛠️ Commands & Workflow Guide

### 1. `/six-file-context-methodology init`
Runs an interactive Q&A discovery loop using Playbook prompts to gather product vision, scope mode (Lite vs Pro), stack choices, UI tokens, SEO strategy, and invariants before creating context files in `context/`.

### 2. `/six-file-context-methodology spec <feature-name>`
Generates a numbered, 5-section feature spec in `context/specs/NN-<feature-name>.md`. Search the web for best practices and run `/roast` before emitting file content.

### 3. `/six-file-context-methodology spec-all`
Decomposes `project-overview.md` into an unbounded list of numbered units (`00-build-plan.md`) following strict build-order rules (Dependencies -> Auth -> Backend APIs -> UI Wiring), generating feature specs upfront in `context/specs/`.

### 4. `/six-file-context-methodology verify`
Executes Playwright CLI to capture 5-viewport screenshots and verify console error cleanliness for completed feature units.

### 5. `/six-file-context-methodology check`
Audits context state synchronization against git commit history to detect and fix any documentation drift.

---

## 📚 Knowledge Base References

- **Masterclass Handbook**: [STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md)
- **Full Video Transcript**: [FULL_TRANSCRIPT.md](file:///d:/AI-OS/references/six-file-context-methodology/FULL_TRANSCRIPT.md)
- **29 Ghost AI Specs Library**: [feature-specs-library/](file:///d:/AI-OS/references/six-file-context-methodology/feature-specs-library/)
- **SEO Skills Library Vault**: [seo-audit-reference/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/seo-audit-reference/)

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **6-File Architecture**: Senior AI engineering 6-file context scaffolding (PROJECT.md, REQUIREMENTS.md, ARCHITECTURE.md, DATA_FLOW.md, DECISIONS.md, PROGRESS.md).
- **Spec & Ticket Integration**: Connects with **/mattpocock-to-spec**, **/jsmastery-scope**, and **/mattpocock-to-tickets**.
