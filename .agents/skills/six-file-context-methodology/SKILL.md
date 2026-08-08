---
title: Six-File Context Methodology (`/six-file-context-methodology` v3.2)
domain: skill
summary: 'This skill supports Tri-Mode Flexible Execution: - Slash Command: Explicitly run `/six-file-context-methodology
  [init|scaffold|spec <feature-name>|spec-all|execute|verify|check|resume]` in chat.'
critical_directives:
- 'Per-Reference Socratic Interview Rule**: For every reference asset added to `reference/`, the AI engine interactively in'
- '`/six-file-context-methodology init` executes a mandatory 4-Phase Socratic Interview (Brand & Vision -> Architecture &
  D'
- 'Strict Token Safeguards: Surgical context ingestion (subagents receive only exact target files, never full context folde'
- 'Catalog-First Rule: Prohibits writing UI components from scratch when matching catalog components exist.'
section_outline:
- Six-File Context Methodology (`/six-file-context-methodology` v3.2)
- Invocation & Tri-Mode Routing
- Addressed Vulnerabilities & v3.2 System Upgrades
- Hard-and-Fast System Mandates
- Commands & Workflow Guide
read_triggers:
- When working on skill in .agents/skills/six-file-context-methodology/SKILL.md
- When reading context for Six-File Context Methodology (`/six-file-context-methodology` v3.2)
tags:
- skill
- SKILL
updated: '2026-08-08'
name: six-file-context-methodology
description: Senior AI Engineering 7-File Context Methodology v3.2. Scaffolds 7-File Context System, project-local reference/
  priority vault, granular reference deconstruction manifests (MANIFEST.md), 4-phase Socratic init interview, feature-specific
  spec Socratic sessions, Graphify knowledge graph integration (.planning/graphs/), Interactive Playwright 5-viewport visual
  handoff gate, Multi-Session state persistence (zero context loss), Token-Optimized Wave Execution, and OWASP LLM & Server
  Action security gates.
argument-hint: '[init|scaffold|spec <feature-name>|spec-all|execute [ticket|wave|all]|verify|check|resume]'
---

# Six-File Context Methodology (`/six-file-context-methodology` v3.2)

## Invocation & Tri-Mode Routing

This skill supports Tri-Mode Flexible Execution:
- Slash Command: Explicitly run `/six-file-context-methodology [init|scaffold|spec <feature-name>|spec-all|execute|verify|check|resume]` in chat.
- Dynamic Intent Matching: Triggered automatically when task context involves context scaffolding, feature specs, ticket deconstruction, design reference ingestion, or senior AI engineering workflows.
- Inter-Skill & AIOS Calling: Programmatically invokable by parent skills (e.g. `/new-project`, `/make-plan`, `/website-design-engine`) or subagents via `/six-file-context-methodology` or reading `SKILL.md` directly.

---

## Addressed Vulnerabilities & v3.2 System Upgrades

1. Mandatory Project-Local `reference/` Vault & Per-Reference Granular Deconstruction (`reference/MANIFEST.md`):
   - Scaffolds a project-local `reference/` directory during `/six-file-context-methodology init`.
   - Stores screenshots (`.png`, `.jpg`), screen recordings (`.mp4`), HTML gallery files (e.g. WebGL shaders), TSX/CSS component snippets, and design briefs.
   - Enforces `reference/` as the **#1 Priority Source of Truth** for visual designs and component implementations.
   - **Per-Reference Socratic Interview Rule**: For every reference asset added to `reference/`, the AI engine interactively interviews the operator to clarify: (1) What specific elements to keep vs remove, (2) Whether to use the full layout or a targeted sub-component/motion/shader, and (3) How to re-bind the design into project OKLCH brand tokens within `reference/MANIFEST.md`.

2. 4-Phase Socratic Discovery (`init`) & Feature-Specific Spec Socratic Sessions:
   - `/six-file-context-methodology init` executes a mandatory 4-Phase Socratic Interview (Brand & Vision -> Architecture & Data -> Component & Motion Choreography -> Conversion & Store Flows) explaining concepts before asking questions.
   - **Feature-Specific Socratic Sessions**: Every feature spec command (`spec <feature-name>`) triggers a dedicated feature-level Socratic Q&A session before writing `context/specs/NN-feature.md` or deconstructing tickets.

3. Interactive Human-in-the-Loop Visual QA Gate (`verify`):
   - Runs automated Playwright headless browser testing across 5 viewports (Desktop, Laptop, Tablet, Mobile Portrait, Mobile Landscape) for every completed UI component ticket.
   - Pauses execution, presents screenshot artifact paths and visual evaluation summary to the operator, and waits for explicit operator approval (or user-uploaded feedback screenshots) before signing off on ticket Definition of Done (DoD).

4. Graphify Knowledge Graph Integration (`.planning/graphs/`):
   - Integrates `graphify update .` and `graphify query` into project initialization and spec creation.
   - Builds and maintains a local AST and architectural dependency knowledge graph under `.planning/graphs/` tracking node links, layout dependencies, and decision tickets.

5. Multi-Session Zero-Context-Loss Protocol (`/six-file-context-methodology resume`):
   - Prevents AI model hallucination when starting fresh chat sessions for the same project.
   - Continuously persists project state, active tickets, and completed DoD milestones in `context/progress-tracker.md`, `docs/wayfinder/map.md`, `context/specs/`, and `decisions/log.md`.
   - Running `/six-file-context-methodology resume` in a new chat session immediately restores 100% accurate context without re-reading entire conversation transcripts.

6. Dual Spec & Ticket Pipeline (Matt Pocock Integration):
   - Generates high-level technical feature specs in `context/specs/NN-feature.md`.
   - Automatically deconstructs feature specs into atomic engineering tickets in `docs/tickets/` with verifiable DoD.
   - Synchronizes multi-session destinations in `docs/wayfinder/map.md`.

7. Token-Optimized Wave Execution (`/six-file-context-methodology execute`):
   - Executes tickets in wave-based parallel streams (Dependencies -> Auth/DB -> API Routes -> UI Components).
   - Strict Token Safeguards: Surgical context ingestion (subagents receive only exact target files, never full context folders), 2-attempt max retry hard stop, and 1-3 file boundary caps per ticket.

8. Catalog-First Component Sourcing & Token Theme Adaptation:
   - Queries 300+ Component Synthesis Engine (`component_registry_cli.py search`), prioritizing operator favorites and custom user-provided lists.
   - Catalog-First Rule: Prohibits writing UI components from scratch when matching catalog components exist.
   - Token Theme Adaptation: Strips inline hardcoded component colors and re-binds styles strictly to project OKLCH/CSS tokens in `ui-context.md`.

9. Comprehensive Security Quality Gates (VibeSec + OWASP LLM):
   - Embeds `/vibesec` rules directly into `code-standards.md` and ticket DoD.
   - Next.js 15 / React 19 Server Action Security: Forces in-function `auth()` verification and `import 'server-only'` to prevent public endpoint invocation or server secret leaks.
   - OWASP LLM Application Security: Prompt injection defense, RAG vector tenant isolation (`workspace_id` filtering), Excessive Agency safeguards, and Unbounded Consumption rate limiting.

10. Strict Zero-Emoji Mandate:
    - No emojis used anywhere in skill markdown, output logs, or code artifacts.

---

## Hard-and-Fast System Mandates

1. Global Zero-Hurry Rule: Never rush execution. Architectural rigor, deep option-based Q&A, web search research, Playwright visual QA, and pre-coding backstops take precedence over speed.
2. Interactive 4-Phase Discovery (`init`): Runs a 4-phase Socratic interview before scaffolding the 7 context files.
3. Mandatory Project-Local `reference/` & `MANIFEST.md`: Automatically creates `reference/` folder and interviews operator for every reference asset added.
4. Graphify AST Knowledge Graph: Runs `graphify update .` during initialization and maintains `.planning/graphs/`.
5. 7-File Context Foundation (Pro Mode):
   - `context/project-overview.md`
   - `context/architecture.md`
   - `context/code-standards.md`
   - `context/ui-context.md` (Integrated with 4-level component priority chain & `component_registry_cli.py`)
   - `context/ai-workflow-rules.md`
   - `context/progress-tracker.md`
   - `context/seo-context.md` (Integrated with 23-skill SEO vault)
6. Dynamic Unbounded Specs & Feature-Specific Socratic Q&A (`spec`): Generates feature specs upfront in `context/specs/` and compiles atomic tickets in `docs/tickets/`.
7. Mandatory Pre-Write `/roast` Council: Runs `/roast` gatekeeper audit before creating any document file.
8. Interactive Playwright Visual QA Engine (`verify`): Captures 5-viewport screenshots, presents them to operator, and waits for manual approval.
9. Multi-Session Resume Protocol (`resume`): Restores project state cleanly in fresh chat windows using `progress-tracker.md` and `wayfinder/map.md`.
10. Pre-Coding Backstop: Always asks: "Is there anything else remaining before we touch the code?"

---

## Commands & Workflow Guide

### 1. `/six-file-context-methodology init`
Runs 4-phase Socratic discovery interview, creates project `reference/` directory, initializes Graphify knowledge graph (`.planning/graphs/`), queries component synthesis CLI, and scaffolds 7 context files in `context/`.

### 2. `/six-file-context-methodology spec <feature-name>`
Triggers feature-specific Socratic Q&A session, generates a numbered 5-section feature spec in `context/specs/NN-<feature-name>.md`, and compiles atomic tickets in `docs/tickets/`. Runs `/roast` before emitting file content.

### 3. `/six-file-context-methodology spec-all`
Decomposes `project-overview.md` into an unbounded list of feature specs upfront in `context/specs/`, compiling corresponding ticket streams in `docs/tickets/`.

### 4. `/six-file-context-methodology execute [ticket|wave|all]`
Dispatches background developer agents using wave-based parallelization protected by strict token efficiency rules.

### 5. `/six-file-context-methodology verify`
Executes Playwright CLI to capture 5-viewport screenshots, presents visual artifacts to operator, and waits for manual approval/feedback.

### 6. `/six-file-context-methodology check`
Audits context state synchronization against git commit history and Graphify AST nodes to detect and fix documentation drift.

### 7. `/six-file-context-methodology resume`
Restores project context state in a fresh chat window by reading `context/progress-tracker.md` and `docs/wayfinder/map.md`.

---

## Knowledge Base References & Clean Templates

- Clean Real Templates: [6-file-context-templates/](file:///d:/AI-OS/references/six-file-context-methodology/6-file-context-templates/)
- Official Template Guide: [TEMPLATE_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/6-file-context-templates/TEMPLATE_GUIDE.md)
- Masterclass Handbook: [STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md)
- Creator Project Reference Vault: [creator-project-reference/](file:///d:/AI-OS/references/six-file-context-methodology/creator-project-reference/)

---

## Inter-Skill Connections & Handoff Pipeline
- 6-File Architecture: Senior AI engineering 7-file context scaffolding + local `reference/` vault + `MANIFEST.md`.
- Graphify Knowledge Graph: Integrated AST dependency & node tracking (`.planning/graphs/`).
- Web Design Engine Sync: Directly provides layout & UI context specifications for `/website-design-engine` v3.0.
- Macro Planning & Multi-Session Maps: Integrates with `/mattpocock-wayfinder` (`docs/wayfinder/map.md`).
- Spec & Ticket Integration: Connects with `/mattpocock-to-spec`, `/jsmastery-scope`, `/mattpocock-to-tickets`, and `/storm-research-project`.

---

## Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

