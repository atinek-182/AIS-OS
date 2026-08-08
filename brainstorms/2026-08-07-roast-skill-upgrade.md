# Roast Skill Upgrade: Discovery & Brainstorm Notes
Date: 2026-08-07 · Goal: Upgrade /roast skill into a universal, multi-domain, zero-emoji, persistent multi-agent red-teaming engine · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- Vision: Transform /roast into a universal, modular, multi-domain red-teaming engine usable across any domain (code, architecture, business offers, content, research, AI workflows).
- Key Safeguards: 100% Zero-Emoji Mandate, automatic disk persistence, structured refinement ticket generation, flexible domain adapters.

## Q&A Log
### Q1 — Universal Domain Adapters & Dynamic Context Injection
- **Decision Captured**: Option A (Auto-detect domain from context + support optional explicit `--domain [code|offer|copy|workflow|strategy]` flag).

### Q2 — Multi-Turn Adversarial Red-Teaming Loop ("Attack & Patch" Mode)
- **Decision Captured**: Option A with Smart Triggering (Single-pass fast roast by default; prompt/recommend `--deep` mode when complex architectures, security boundaries, or core revenue models are detected).

### Q3 — Disk Persistence & Handoff Artifacts
- **Decision Captured**: Option B (Save structured artifact `brainstorms/roast_{date}_{slug}.md` when `--save` flag is passed or when `--deep` mode is triggered).

### Q4 — Persona Count & Extended Council (Baseline 5 Personas + Specialized 6th/7th Roles)
- **Decision Captured**: Maintain baseline 5-Persona Council across all standard roasts. For specialized deep roasts (`--deep` or specialized domains), dynamically expand the council with specialized 6th and 7th personas:
  - *Security Auditor (Code/Architecture)*: Deep /vibesec pen-testing, IDOR/SSRF prevention, and data leakage.
  - *Product Economist (SaaS/Pricing)*: API token unit economics, margin modeling, and payback velocity.
  - *UX & Friction Specialist (Web App/UI)*: Conversion friction, cognitive load, and zero-slop UI quality gates.

### Q5 — Automated `--deep` Trigger Recommendations
- **Decision Captured**: Enabled. Automatically scan roast targets for Security/Auth boundaries, Core Revenue/Pricing models, or Multi-System Refactors, displaying a clear recommendation box: `[RECOMMENDED: Re-run with --deep for multi-turn attack & patch loop]`.

### Q6 — Quantitative Risk Matrix & Refinement Ticket (`ROAST_REFINEMENT_SPEC`)
- **Decision Captured**: Enabled. Calculate a 4-axis numerical risk matrix (Security/Failure Risk, Implementation Friction, Value/ROI, Simplicity) and output a copyable `ROAST_REFINEMENT_SPEC` fix checklist when the verdict is RESHAPE.


