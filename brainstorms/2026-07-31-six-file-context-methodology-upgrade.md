# Six-File Context Methodology Upgrade: Discovery & Brainstorm Notes
Date: 2026-07-31 · Goal: Deep Socratic grilling and architectural alignment to upgrade the `/six-file-context-methodology` skill to v3.0 · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Spec & Ticket Deconstruction (Option 1)**: `/six-file-context-methodology` will feature Deep Dual-Pipeline Integration. It generates high-level technical feature specs in `context/specs/`, automatically compiles atomic engineering tickets in `docs/tickets/` with verifiable DoD (Definition of Done), and updates the multi-session roadmap in `docs/wayfinder/map.md`.
- **Token-Optimized Wave Execution (Option 1 + Token Safeguards)**: `/six-file-context-methodology execute` runs wave-based parallel subagent orchestration, protected by strict Token Optimization Rules (Surgical Context Ingestion, Max 2-Attempt Loop Backstop, Atomic Ticket Scope Capping) to prevent token credit burn.
- **Catalog-First Component Sourcing & Token Theme Adaptation (Option 1 + User Rules)**: `/six-file-context-methodology` automatically queries our 300+ component synthesis engine (`component_registry_cli.py search`), prioritizing operator favorites and custom user-provided lists. Prohibits creating generic components from scratch when catalog matches exist, and strictly refactors hardcoded component colors into the project's exact `ui-context.md` OKLCH design tokens.
- **Comprehensive Security Quality Gates (Option 1 + OWASP LLM & Server Action Additions)**: Embeds explicit `/vibesec` security contracts into `code-standards.md` and ticket DoD. Augments `vibesec` with Next.js 15 Server Action isolation (`import 'server-only'`, in-function auth checks), raw webhook signature verification, and OWASP Top 10 for LLM Applications (Prompt injection defense, RAG tenant isolation, Excessive Agency safeguards, and Unbounded Consumption rate limits).
- **Smart Conditional STORM Research Integration & Persistent Brain Memory (Option 1 + 7 Lenses)**: Duplicates `storm-research` into a dedicated skill `storm-research-project` featuring 7 specialized research lenses (adding AI/LLM Integration & Latency Specialist and Developer Ergonomics & Token Footprint Auditor). Triggered conditionally on high-complexity architecture choices. Logs research findings to `brain-aios/wiki/research/` and `MEMORY.md` so the AIOS persistently retains research insights across sessions without re-invoking tools.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **7-File Context Methodology**: Context scaffolding framework (`project-overview.md`, `architecture.md`, `code-standards.md`, `ui-context.md`, `ai-workflow-rules.md`, `progress-tracker.md`, `seo-context.md`).
- **Lite Mode vs Pro Mode**: Dual-tier context complexity to prevent tooling overhead on micro-projects vs full SaaS.
- **Wayfinder Decision Map**: Multi-session roadmap stored in `docs/wayfinder/map.md` tracking active build streams and decision tickets.
- **Wave-Based Parallel Orchestration**: Grouping non-dependent tickets into parallel execution streams while enforcing strict build order.
- **Surgical Context Ingestion**: Passing only exact required files to subagents to minimize token footprint.
- **Token Theme Adaptation**: Stripping inline hardcoded component colors and rebinding them to project OKLCH CSS variables/tokens.
- **Catalog-First Component Rule**: Mandate to use existing 300+ cataloged components before writing custom code.
- **Server Action Auth Guard**: Enforcing in-function `auth()` verification and `server-only` guards on Next.js 15 Server Actions.
- **OWASP LLM Application Security**: Defense against prompt injection, excessive agency, RAG vector data leakage, and LLM financial exhaustion.
- **STORM Project Research (7 Lenses)**: Extended multi-perspective research engine for architecture trade-offs.
- **Persistent AIOS Brain Memory**: Auto-logging research reports to `brain-aios/wiki/research/` to prevent redundant research.

## Q&A Log
### Q1 — Spec Engineering & Ticket Pipeline Structure
- **Concept Explained**: Integrating Matt Pocock's ticket compiler (`mattpocock-to-tickets`) and Wayfinder decision maps (`mattpocock-wayfinder`) with high-level feature specs.
- **Asked**: How should `/six-file-context-methodology` structure feature spec generation and ticket deconstruction?
- **Options Provided**: 1. Deep Dual-Pipeline Integration (Specs + Atomic Tickets + Wayfinder Map) [RECOMMENDED] | 2. Single Unified Feature Spec Standard | 3. Hybrid Mode
- **Captured Decision**: Option 1 (Deep Dual-Pipeline Integration).
- **Rationale & Trade-offs**: Gives high-level architecture vision in `context/specs/` while providing bite-sized, verifiable tasks in `docs/tickets/` that background developer agents (`project-agent` / `do`) can execute with zero ambiguity.

### Q2 — Subagent Execution & Token Efficiency Safeguards
- **Concept Explained**: Autonomous subagent orchestration using wave-based parallel execution vs sequential loops.
- **Asked**: How should `/six-file-context-methodology` delegate and execute build tasks with subagents?
- **Options Provided**: 1. Wave-Based Parallel Subagent Orchestration [RECOMMENDED] | 2. Sequential Phase-by-Phase Execution | 3. Hands-Off Autonomous Mode
- **Captured Decision**: Option 1 (Wave-Based Parallel Subagent Orchestration) with strict Token Efficiency Safeguards.
- **Rationale & Token Safeguards Enforced**:
  1. *Surgical Context Ingestion*: Subagents receive ONLY `code-standards.md`, the single target ticket file, and exact target source code files (never full context folders).
  2. *2-Attempt Hard Stop*: If a subagent fails a build/test verification twice, it immediately halts and alerts the operator, eliminating infinite retry loops.
  3. *Atomic File Boundaries*: Tickets are capped at touching 1-3 files max, preventing massive subagent context bloat.

### Q3 — Automated Component Sourcing & Design Token Adaptation
- **Concept Explained**: Automatically querying our 300+ component synthesis engine (`component_registry_cli.py search`) to source signature UI components.
- **Asked**: How should `/six-file-context-methodology` query and inject component choices into `ui-context.md` and feature specs?
- **Options Provided**: 1. Automatic Synthesis CLI Querying & Component Mapping [RECOMMENDED] | 2. On-Demand Component Sourcing | 3. Hybrid Mode
- **Captured Decision**: Option 1 (Automatic Synthesis CLI Querying) + Strict User Mandates.
- **User Rules Enforced**:
  1. *Catalog-First Mandate*: NEVER write UI components from scratch if a match exists in our 300+ component registry or user-provided component lists.
  2. *Design Token / Theme Adaptation*: Strip hardcoded component colors and re-bind all styles strictly to project OKLCH/CSS tokens in `ui-context.md`.
  3. *Favorite Component Priority*: Search results must rank user favorites and custom component additions first.

### Q4 — Security Quality Gates & Modern OWASP Additions
- **Concept Explained**: Embedding `/vibesec` security rules into `code-standards.md` and ticket DoD.
- **Asked**: How should `/six-file-context-methodology` enforce security standards in context files and subagent execution?
- **Options Provided**: 1. Explicit Security Rules in `code-standards.md` + Ticket DoD Security Verification [RECOMMENDED] | 2. Standalone Security Context File | 3. Pre-Write Roast Gate Security Audit Only
- **Captured Decision**: Option 1 (Explicit Rules in `code-standards.md` + Ticket DoD Verification) + OWASP LLM & Next.js 15 Additions.
- **Essential Security Rules Added to System**:
  1. *Next.js 15 / React 19 Server Action Security*: Force in-function `auth()` verification and `import 'server-only'` to prevent public endpoint invocation or server-secret leakage.
  2. *OWASP LLM Application Security*:
     - *Prompt Injection (LLM01)*: Strict input sanitization & RAG data isolation.
     - *Excessive Agency (LLM06)*: Human-in-the-loop approvals for destructive AI tool calls.
     - *Unbounded Consumption (LLM10)*: Token rate limits and per-user financial exhaustion safeguards (Arcjet/Upstash).
     - *RAG Vector Tenant Isolation (LLM02)*: Mandate `workspace_id` / `user_id` filtering in vector search metadata.
  3. *Raw Webhook Signature Verification*: Validate HMAC signatures (Stripe Svix/Supabase) on raw request buffers before JSON parsing.

### Q5 & Q6 — STORM Research Integration & Persistent Brain Memory
- **Concept Explained**: Utilizing Stanford STORM multi-perspective research method for non-trivial architecture trade-offs.
- **Asked**: How should `/storm-research` be triggered, and what extra research lenses should be added for AIOS projects?
- **Captured Decision**: Option 1 (Smart Conditional STORM Trigger) + Duplicate Skill to `storm-research-project` with 7 Lenses.
- **Rules Enforced**:
  1. *Duplicate & Preserve Original*: Leave `.agents/skills/storm-research/SKILL.md` completely intact. Create `.agents/skills/storm-research-project/SKILL.md`.
  2. *7 Lenses Suite*: Add Lens 6 (AI / LLM Integration & Latency Specialist) and Lens 7 (Developer Ergonomics & Token Footprint Auditor).
  3. *Zero Emoji Policy*: Do not use any emojis in skill markdown or generated reports.
  4. *Persistent AIOS Brain Memory*: Automatically log synthesized STORM research summaries to `brain-aios/wiki/research/` and update `MEMORY.md` so the AIOS retains research context across sessions without re-running tools.





