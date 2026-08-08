# SDLC & AIOS Unified Workflows, Skills, Scripts & Automations Integration
Date: 2026-08-08 · Goal: Unify all 240+ skills, 80+ scripts, 6-Phase SDLC, and Agency Automations into a single seamless, automated execution pipeline · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Dual-Engine Master Architecture**: Decoupled Technical 6-Phase SDLC Engine (`DEFINE` -> `PLAN` -> `BUILD` -> `VERIFY` -> `REVIEW` -> `SHIP`) for core software engineering, linked to the 7-Stage ZORIXEL Client Agency Engine for client sprints ($1,500–$5,000+).
- **Hybrid Execution Discipline**: Interactive atomic builds by default; autonomous multi-task pass on `/build auto` and parallel 4-persona security/qa/perf sign-offs on `/ship`.
- **Master CLI Bridge (`scripts/aios_master_runner.py`)**: Unified entrypoint executing 1-second pre-flight health checks (`aios_master_runner.py health`) across all 240+ skills, 80+ scripts, auth tokens, and AST graphs, while triggering auto-evolution on skill additions.


## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **6-Phase Master SDLC**: The overarching engineering lifecycle (Define -> Plan -> Build -> Verify -> Review -> Ship) governing software production.
- **Agency Pipeline**: The business and client acquisition workflow (Intake -> Audit -> Design -> Proposal -> Build Sprint -> SLA Health -> Vault Handoff).

## Q&A Log
### Q1 — Unification Architecture for SDLC Engine & Existing AIOS Skill Vault
- **Concept Explained**: We now have 4 major skill ecosystems in AIOS: (1) Addy Osmani's 24 SDLC skills & 4 review personas, (2) Superpowers' autonomous subagents & TDD loops, (3) Matt Pocock's interrogation (`/grill-me`) & ticket mechanics (`/to-tickets`), and (4) ZORIXEL's agency engines (`/website-design-engine`, `/hallmark`, `/vibesec`, `/gstack`, `/composio`, `/gws-automation-engine`). Unification means creating a single, deterministic orchestration matrix where running any phase command (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`) automatically triggers the exact scripts, subagents, and tools required without missing steps.
- **Asked**: How should we structure the master unification matrix across all skills, scripts, and automations?
- **Options Provided**:
  1. Option A (Dual Engine Architecture: Technical SDLC + Client Agency Engine) [RECOMMENDED]
  2. Option B (Single Master SDLC Router with Auto-Subagent Cascade)
  3. Option C (Loose Phase Commands with Manual Handoffs)
- **Captured Decision**: Option A (Dual-Engine Architecture: Technical SDLC + Client Agency Engine)
- **Rationale & Trade-offs**: Keeps technical software development (`DEFINE` -> `PLAN` -> `BUILD` -> `VERIFY` -> `REVIEW` -> `SHIP`) razor-sharp and decoupled while connecting cleanly to the 7-Stage ZORIXEL Client Agency Engine (Intake -> Proposal -> Build Sprint -> SLA Health -> Vault Handoff) whenever building client projects.

## Open Flags & Deferred Decisions

### Q2 — Execution & Subagent Cascade Discipline in Build & Ship Phases
- **Concept Explained**: During Phase 3 (`/build`) and Phase 6 (`/ship`), AIOS can either interactively ask for confirmation after every single file edit/task, run fully autonomously using subagent loops and persona fanouts, or provide a hybrid mode where standard builds are interactive while `/build auto` and `/ship` run autonomous multi-persona verification.
- **Asked**: How should automated subagents, persona fanouts, and script execution be triggered during `/build` and `/ship`?
- **Options Provided**:
  1. Option A (Hybrid Mode: Interactive by default, Autonomous on `/build auto` & `/ship` 4-Persona Fanout) [RECOMMENDED]
  2. Option B (100% Fully Autonomous by Default)
  3. Option C (Strict Sequential Single-Session Only)
### Q3 — Automated CLI Runners, Script Bridges & Auto-Evolution Integration
- **Concept Explained**: We have multiple specialized Python runner scripts (`agent_skills_runner.py`, `graphify_runner.py`, `composio_runner.py`, `youtube_skills_runner.py`, `skill_workflow_evolver_runner.py`, `aios_gws_health_check.py`). We can either create a single unified master CLI entrypoint (`aios_master_runner.py`) that pre-flights and orchestrates all scripts, keep them as independent scripts called per domain, or rely solely on LLM shell calls.
- **Asked**: How should we structure the Python runner scripts and automated validation bridges across the system?
- **Options Provided**:
  1. Option A (Unified Master CLI Bridge `aios_master_runner.py` + Skill Workflow Auto-Evolver) [RECOMMENDED]
  2. Option B (Independent Domain-Specific Python Scripts)
  3. Option C (Inline LLM Shell Execution Only)
- **Captured Decision**: Option A (Unified Master CLI Bridge `aios_master_runner.py` + Skill Auto-Evolver)
- **Rationale & Trade-offs**: Provides a single, 100% deterministic 1-second pre-flight health runner (`aios_master_runner.py health`) that validates all skills, scripts, auth tokens, and knowledge graphs while triggering auto-evolution whenever new skills are added.








