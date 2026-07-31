---
name: six-file-context-methodology
description: Senior AI Engineering 7-File Context Methodology v3.0. Scaffolds 7-File Context System, Spec & Ticket Pipeline (docs/tickets/), Token-Optimized Wave Execution, Catalog-First Component Synthesis, Modern Security Quality Gates (OWASP LLM & Server Actions), and Smart STORM 7-Lens Research Integration.
argument-hint: '[init|scaffold|spec <feature-name>|spec-all|execute [ticket|wave|all]|verify|check]'
---

# Six-File Context Methodology (`/six-file-context-methodology` v3.0)

## Invocation & Tri-Mode Routing

This skill supports Tri-Mode Flexible Execution:
- Slash Command: Explicitly run `/six-file-context-methodology [init|scaffold|spec <feature-name>|spec-all|execute|verify|check]` in chat.
- Dynamic Intent Matching: Triggered automatically when task context involves context scaffolding, feature specs, ticket deconstruction, or senior AI engineering workflows.
- Inter-Skill & AIOS Calling: Programmatically invokable by parent skills (e.g. `/new-project`, `/make-plan`, `/website-design-engine`) or subagents via `/six-file-context-methodology` or reading `SKILL.md` directly.

---

## Addressed Vulnerabilities & v3.0 System Upgrades

1. Dual Spec & Ticket Pipeline (Matt Pocock Integration):
   - Generates high-level technical feature specs in `context/specs/NN-feature.md`.
   - Automatically deconstructs feature specs into atomic engineering tickets in `docs/tickets/` with verifiable DoD (Definition of Done).
   - Synchronizes multi-session destinations in `docs/wayfinder/map.md`.

2. Token-Optimized Wave Execution (`/six-file-context-methodology execute`):
   - Executes tickets in wave-based parallel streams (Dependencies -> Auth/DB -> API Routes -> UI Components).
   - Strict Token Safeguards: Surgical context ingestion (subagents receive only exact target files, never full context folders), 2-attempt max retry hard stop, and 1-3 file boundary caps per ticket.

3. Catalog-First Component Sourcing & Token Theme Adaptation:
   - Queries 300+ Component Synthesis Engine (`component_registry_cli.py search`), prioritizing operator favorites and custom user-provided lists.
   - Catalog-First Rule: Prohibits writing UI components from scratch when matching catalog components exist.
   - Token Theme Adaptation: Strips inline hardcoded component colors and re-binds styles strictly to project OKLCH/CSS tokens in `ui-context.md`.

4. Comprehensive Security Quality Gates (VibeSec + OWASP LLM):
   - Embeds `/vibesec` rules directly into `code-standards.md` and ticket DoD.
   - Next.js 15 / React 19 Server Action Security: Forces in-function `auth()` verification and `import 'server-only'` to prevent public endpoint invocation or server secret leaks.
   - OWASP LLM Application Security: Prompt injection defense, RAG vector tenant isolation (`workspace_id` filtering), Excessive Agency safeguards (human approval for destructive actions), and Unbounded Consumption rate limiting.
   - Raw Webhook Signature Verification: Validates HMAC signatures (Stripe Svix/Supabase) on raw request buffers before JSON parsing.

5. Smart Conditional STORM 7-Lens Research Integration:
   - Triggers `/storm-research-project` (7 specialized research lenses) conditionally during `init` or complex `spec` trade-offs.
   - Logs research summaries to `brain-aios/wiki/research/` and `MEMORY.md` so the AIOS persistently retains research insights across sessions without re-running tools.

6. Strict Zero-Emoji Mandate:
   - No emojis used anywhere in skill markdown, output logs, or code artifacts.

---

## Hard-and-Fast System Mandates

1. Global Zero-Hurry Rule: Never rush execution. Architectural rigor, deep option-based Q&A, web search research, Playwright visual QA, and pre-coding backstops take precedence over speed.
2. Interactive Architect Discovery (`init`): Runs an interactive option-based Q&A loop before creating context files. Offers Lite Mode vs Pro Mode choice.
3. 7-File Context Foundation (Pro Mode):
   - `context/project-overview.md`
   - `context/architecture.md`
   - `context/code-standards.md`
   - `context/ui-context.md` (Integrated with 300+ components via `component_registry_cli.py`)
   - `context/ai-workflow-rules.md`
   - `context/progress-tracker.md`
   - `context/seo-context.md` (Integrated with 23-skill SEO vault)
4. Dynamic Unbounded Specs (`spec-all`): Generates feature specs upfront in `context/specs/` and compiles atomic tickets in `docs/tickets/`.
5. Mandatory Pre-Write `/roast` Council: Runs `/roast` gatekeeper audit before creating any document file.
6. Playwright Visual QA Engine (`verify`): Runs Playwright CLI headless browser screenshots and console audits for every spec unit.
7. Pre-Coding Backstop: Always asks: "Is there anything else remaining before we touch the code?"

---

## Commands & Workflow Guide

### 1. `/six-file-context-methodology init`
Runs interactive Q&A discovery loop, queries component synthesis CLI, and scaffolds 7 context files in `context/`.

### 2. `/six-file-context-methodology spec <feature-name>`
Generates a numbered, 5-section feature spec in `context/specs/NN-<feature-name>.md` and compiles atomic tickets in `docs/tickets/`. Runs `/roast` before emitting file content.

### 3. `/six-file-context-methodology spec-all`
Decomposes `project-overview.md` into an unbounded list of feature specs upfront in `context/specs/`, compiling corresponding ticket streams in `docs/tickets/`.

### 4. `/six-file-context-methodology execute [ticket|wave|all]`
Dispatches background developer agents using wave-based parallelization protected by strict token efficiency rules.

### 5. `/six-file-context-methodology verify`
Executes Playwright CLI to capture 5-viewport screenshots and verify console error cleanliness for completed feature units.

### 6. `/six-file-context-methodology check`
Audits context state synchronization against git commit history to detect and fix documentation drift.

---

## Knowledge Base References & Clean Templates

- Clean Real Templates: [6-file-context-templates/](file:///d:/AI-OS/references/six-file-context-methodology/6-file-context-templates/)
- Official Template Guide: [TEMPLATE_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/6-file-context-templates/TEMPLATE_GUIDE.md)
- Masterclass Handbook: [STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md)
- Creator Project Reference Vault: [creator-project-reference/](file:///d:/AI-OS/references/six-file-context-methodology/creator-project-reference/)

---

## Inter-Skill Connections & Handoff Pipeline
- 6-File Architecture: Senior AI engineering 7-file context scaffolding.
- Macro Planning & Multi-Session Maps: Integrates with `/mattpocock-wayfinder` (`docs/wayfinder/map.md`).
- Spec & Ticket Integration: Connects with `/mattpocock-to-spec`, `/jsmastery-scope`, `/mattpocock-to-tickets`, and `/storm-research-project`.
