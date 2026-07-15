# Subagent Configuration: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Define specialized background agent behaviors and create a subagent configuration file under .agents/agents/.

## Summary / key decisions
- **Workspace Junctions:** Mapped projects inside `projects/` using directory junctions to allow the AIOS to access context cleanly.
- **Goal:** Create a subagent configuration file under `.agents/agents/` that defines specialized background agent behaviors (such as a project developer agent, content researcher, or other role).
- **Core Role & Responsibilities:** The subagent acts as a project lead developer, executing programming/content tasks, following the Superpowers workflow (planning, TDD, implementation, verification), auto-generating/updating `walkthrough.md`, and returning a clean final summary.
- **Frontmatter Configuration:** Model is set to `inherit`, Color is set to `blue`, and Tools are omitted to permit full tool access (required for compiling, running tests, and executing commands).
- **Execution Process:** The agent must follow a strict Superpowers engineering loop: Plan -> TDD (failing tests first) -> Implement -> Verify (lint/compile/test) -> Document changes in a project-specific `walkthrough.md`.
- **Trigger Scenarios:** The agent handles:
  - Feature Development (implementing features/pages)
  - Bug Fixing (remediating failing tests/defects)
  - Refactoring/Upgrades (refactoring files, standardizing layout tokens).

## Q&A log
### Q1 — Core Role and Responsibilities
- Asked: What should be the core role and responsibilities of the 'developer' subagent when spawned inside a project folder?
- Captured: Act as a project lead developer: execute tasks, follow superpowers workflow (plan, TDD, verify), auto-generate/update walkthrough.md, and return a clean final summary.
- Flags: None.

### Q2 — Frontmatter Configuration
- Asked: What frontmatter settings (Model, Color, Tools) should be configured for the 'developer' agent?
- Captured: Model: inherit, Color: blue, Tools: Omitted (Full access to all tools to allow running tests and managing files).
- Flags: None.

### Q3 — Agent Execution Process
- Asked: What process/workflow steps should the 'developer' subagent follow inside its system prompt?
- Captured: Plan -> TDD -> Implement -> Verify -> Document in walkthrough.md (Strict adherence to Superpowers engineering workflow).
- Flags: None.

### Q4 — Trigger Scenarios (When to Invoke)
- Asked: What scenarios should be listed under 'When to invoke' in the developer agent body?
- Captured: Standard: Feature Development, Bug Fixing, and Refactoring/Upgrades.
- Flags: None.

### Q5 — Completeness Check
- Asked: Is there anything else we should touch upon before we generate and write the agent configuration file?
- Captured: No, we have defined all the required specifications. Let's proceed to write the file under `.agents/agents/developer.md`.
- Flags: None.

## Open flags (pending input)
- None.
