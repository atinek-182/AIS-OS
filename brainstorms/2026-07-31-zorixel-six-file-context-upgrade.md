# Zorixel Web Project & Six-File Context Upgrade: Discovery & Brainstorm Notes
Date: 2026-07-31 · Goal: Final Socratic Grilling to Tailor `/six-file-context-methodology` v3.2 for the Zorixel Brand Website Build · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Session Objective**: Conduct final Socratic grilling session to optimize `/six-file-context-methodology` (v3.2) specifically for launching the official Zorixel brand website (`projects/zorixel-website/`).
- **Focus Areas**: Scaffolding rules, local `reference/` vault strategy, 7-file context defaults, component synthesis priority, and Playwright 5-viewport visual QA loop.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **Zorixel Brand Web Architecture**: The fullstack Next.js 15 App Router structure powering Zorixel's educational website, component showcase, and digital product store.
- **Project-Local Reference Vault (`reference/`)**: Target directory inside `projects/zorixel-website/reference/` storing local brand assets, font files, SVG logotypes (`Nuqun`), and shader background references.

## Q&A Log
### Q1 — Scaffolding Mode & Deep Q&A Protocol
- **Concept Explained**: Pro Mode (7-file context scaffolding) vs Lite Mode.
- **Asked**: Should `/six-file-context-methodology init` target `projects/zorixel-website/` using full 7-File Pro Mode pre-populated with Zorixel brand defaults?
- **Captured Decision**: Option 1 (Pro Mode 7-File Scaffolding with Zorixel Brand Pre-population) + Extensive Deep Q&A Protocol.
- **Rationale**: Pre-loads Zorixel identity (color tokens, font hierarchy, tech stack) while engaging the operator in exhaustive deep Q&A during `init` to clarify every structural preference and feature requirement before writing code.

### Q2 — Project-Local `reference/` Design Vault & Style Adaptation
- **Concept Explained**: Local `reference/` vault as #1 priority source of truth for assets, layouts, feel, shaders, and component references.
- **Asked**: How should the skill handle seeding `projects/zorixel-website/reference/` and ingesting operator design references?
- **Captured Decision**: Option 1 + Design Reference Adaptation Protocol.
- **Rationale**: Automatically syncs brand assets (SVG logos, font files) into `reference/`, while ingesting external user design references (feel, layout, animations, WebGL shaders, UI components) and mandatory adapting them into the Zorixel brand identity system (Obsidian Midnight, Warm Linen Cream, Velvet Burgundy, Electric Crimson, Vintage Ochre Gold).

### Q3 — Automated Playwright QA & Human-in-the-Loop Visual Feedback Gate
- **Concept Explained**: Playwright 5-viewport screenshot verification vs manual visual checks.
- **Asked**: How should UI ticket visual verification be structured?
- **Captured Decision**: Option 1 + Operator Interactive Feedback Gate.
- **Rationale**: Automated Playwright 5-viewport screenshot audits run on every UI ticket, followed by presenting visual outputs to the operator for explicit human approval. Allows the operator to report issues, suggest fine-tuning, or provide custom screenshot overlays before signing off on ticket Definition of Done (DoD).

### Q4 — Per-Reference Granular Deconstruction & Adaptation Interview
- **Concept Explained**: Automated manifest generation vs interactive granular reference intake.
- **Asked**: How should `/six-file-context-methodology` deconstruct and catalog design references in `reference/`?
- **Captured Decision**: Option 1 + Per-Reference Socratic Interview Protocol.
- **Rationale**: For EVERY reference placed into `reference/`, the AI engine must interactively interview the operator, asking: (1) What specific elements to keep vs remove, (2) Whether to use the full layout or a single component/motion/shader, and (3) How to re-bind the asset into Zorixel's brand tokens in `reference/MANIFEST.md`.

### Q5 — 4-Phase Deep Interview (`init`) + Feature-Specific Socratic Spec Sessions
- **Concept Explained**: Structured interview depth across system initialization and individual feature specifications.
- **Asked**: How deep should questioning extend across project phases?
- **Captured Decision**: Option 1 + Feature-Specific Socratic Spec Engine.
- **Rationale**: `/six-file-context-methodology init` executes a 4-Phase Deep Socratic Interview before writing context files. In addition, EVERY feature spec (`context/specs/NN-feature.md`) triggers a dedicated feature-specific Socratic interview to lock down user flows, edge cases, DB schemas, and UI components before compiling tickets.

### Q6 — Interactive Human-in-the-Loop Visual QA & Screenshot Feedback Protocol
- **Concept Explained**: Playwright 5-viewport screenshot sweep + pause execution for manual check.
- **Asked**: How should UI ticket visual verification be handed off to the operator?
- **Captured Decision**: Option 1 (Interactive Visual Handoff & Screenshot Feedback Protocol).
- **Rationale**: Runs Playwright 5-viewport screenshot audits for every UI component, pauses execution, displays screenshot paths, and waits for explicit operator visual feedback (or uploaded screenshots) before signing off on ticket Definition of Done (DoD).

### System Architecture & Operational Rules (Multi-Session & Workspace)
- **Graphify Knowledge Graph Integration**: Automatically builds and updates `.planning/graphs/` knowledge graph (`graphify update .`) during context scaffolding, tracking AST nodes, layout dependencies, decision tickets, and component links.
- **Multi-Session Zero-Context-Loss Protocol**: Eliminates hallucination across fresh chat sessions. Session state is continuously persisted in `context/progress-tracker.md`, `docs/wayfinder/map.md`, `context/specs/`, and `decisions/log.md`. In a fresh chat session, invoking `/six-file-context-methodology resume` or reading tracker files restores 100% accurate project state instantly.
- **Workspace Directory Recommendation**: Open the primary **`d:\AI-OS`** workspace in Antigravity IDE. This gives the AI full access to all AIOS tools, skills, scripts (`scripts/component_registry_cli.py`, `scripts/graphify_runner.py`), and reference vaults, while executing all project commands with target working directory (`Cwd`) pointed at `d:\AI-OS\projects\zorixel-website`.
