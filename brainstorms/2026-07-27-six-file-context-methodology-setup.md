# Six-File Context Methodology & System Guide: Brainstorm / Discovery Notes
Date: 2026-07-27 · Goal: Establish user preferences for scaffolding the 6-file context methodology, upgrading the skill, and creating a step-by-step master guide connected to the transcript and Ghost AI codebase.

## Summary / key decisions
- **Playbook Ingested**: Ingested full `Six-File+Context+Methodology/README.md` (Mindset, Conversation Before Code, 6-File System, Spec-Driven Development, Build Order Rules, 3-Prompt Workflow).
- **Codebase Material**: Ingested `01 — How Real Engineers Build Liveblocks, Trigger.dev` (Ghost AI material: 29 feature specs, completed context files, current issues).
- **Initialization Mode**: Option A (Interactive Architect Mode). `/six-file-context-methodology init` will run an interactive Q&A discovery loop using the Playbook's exact prompts before generating custom context files.
- **Spec Generation Strategy**: Option C (Full Upfront Spec Batching) with dynamic/unbounded spec count (10 to 50+).
- **Proactive Web Search & Deep Refinement**: Search the web for industry-leading features, conduct detailed option-based Q&A interviews, and run `/roast` before finalizing document content.
- **Global Zero-Hurry & Rigor Mandate**: Hard-and-fast rule across ALL skills and projects: Never rush. Deep questioning, web search research, explicit user confirmations, Playwright visual QA, and pre-coding backstops take precedence over speed.

## Q&A log
### Q1 — Scaffolding / Initialization Mode
- Asked: How should `/six-file-context-methodology` scaffold new projects in your workspace?
- Captured: Option A — Interactive Architect Mode. Launch an interactive Q&A discovery loop using Playbook prompts to gather product vision, stack choices, UI tokens, and invariants before creating the 6 context files.
- Flags: None.

### Q2 — Spec Generation & Refinement Strategy
- Asked: How should `/six-file-context-methodology` handle creating build plans and feature specs?
- Captured: Option C — Full Upfront Spec Batching, customized with:
  1. Unbounded Spec Counts: Spec count is dynamic based on app complexity (10, 15, 20, 40, 50+ specs).
  2. Web Search Ingestion: Search the web to recommend modern/trending features for the user's project.
  3. Exhaustive Option-Based Questioning: Ask detailed, structured option-based questions (no 2-3 question limits).
  4. Mandatory Pre-Write `/roast` Council: Run the `/roast` skill to pressure-test every document concept before emitting final content.
- Flags: None.

### Q3 — Execution Loop, Verification, & Global Rigor Mandate
- Asked: How should the upgraded skill manage execution and progress tracking?
- Captured: Option A — Automated Execution Loop with Checkpoints, customized with hard-and-fast global rules:
  1. Explicit Tracker Approval: Ask for user confirmation before modifying `progress-tracker.md` or completing a spec.
  2. Playwright Visual QA Engine: Execute automated Playwright CLI screenshot capture and visual verification for every project feature so the user doesn't have to inspect manually.
  3. Global Zero-Hurry Mandate: Hard-and-fast rule across ALL skills and AIOS projects: Never rush execution. Systems take time (weeks/months). Ask unlimited option-based questions with recommendations.
  4. Web Search First: Search the web for the best technical solutions before proposing implementations.
  5. Pre-Coding Backstop: Always ask *"Is there anything else remaining before we touch the code?"* prior to implementation.
  6. Skill Upgrades Required: Upgrade `/six-file-context-methodology`, `/grill-me`, and `AGENTS.md` / `GEMINI.md` with these mandates.
- Flags: None.

### Q4 — Advanced Protocol Customizations
- Asked: Is there any other rule or preference you want to add before upgrading skills and guide?
- Captured: Combined Option C (Pre-Write Roast Protocol Customization) + Option B (Default Stack & Tooling Preferences). Conduct detailed Q&A on both topics before writing final skills and rules.
- Flags: None.

### Q5 — Pre-Write Roast Council Enforcement
- Asked: How should the Pre-Write Roast Council handle identified risks or flaws?
- Captured: Option A — High-Rigor Gatekeeper Mode. If the Roast Council catches security risks (VibeSec), design slop (Hallmark), or over-engineering (Karpathy), it blocks document emission, presents explicit flaws with recommended fixes, and waits for user confirmation before writing the file.
- Flags: None.

### Q6 — Full-Stack Architecture Choices & Technical SEO Integration
- Asked: Provide 4 top free-tier full-stack architectures (with pros/cons) and integrate technical SEO/GEO requirements into the 6-file system.
- Captured: Option A — Smart Multi-Stack Decision Engine:
  1. Next.js 15 + Supabase + Clerk (Default for general SaaS & Web Apps - 10/10 SEO).
  2. Astro 5 + React (Default for marketing/content/SEO speed sites - 100/100 Core Web Vitals).
  3. Vite + React 19 + Supabase Realtime (Default for client-heavy real-time canvas editors & internal tools).
  4. Component Sourcing Freedom: Not restricted to plain Shadcn UI. Fully integrated with our AIOS's 4 curated libraries (Aceternity UI, Animate UI React, Forge UI, Vengence UI) containing 147 cataloged components.
- Flags: None.

### Q7 — SEO & GEO Deep Integration (7-File Context System)
- Asked: How should SEO and GEO requirements be enforced in your context files?
- Captured: Option A — Dedicated 7th Context File (`context/seo-context.md`) expanding to a 7-File Context System:
  1. Deep SEO Vault Integration: Query `brain-aios/wiki/research/skills-library/seo-audit-reference/` (23 sub-skills: `seo-technical`, `seo-schema`, `seo-geo`, `seo-cluster`, `seo-flow`, `seo-google`, `seo-sitemap`, `seo-images`, etc.) for every project.
  2. Auto-Generated `context/seo-context.md`: Defines dynamic metadata API rules, OpenGraph templates, JSON-LD schema definitions, LLMs.txt AI search guidelines, and topic clusters.
  3. Auto-Generated Technical SEO Specs: Feature specs for `sitemap.ts`, `robots.txt`, dynamic metadata, and JSON-LD schema injections.
  4. Pre-Launch SEO Audit: Run automated python scripts (`scrapling_runner.py`, `schema_ecommerce_validate.py`, `pagespeed_check.py`) before launching any web project.
- Flags: None.

## Open flags (pending input)
- None yet.








