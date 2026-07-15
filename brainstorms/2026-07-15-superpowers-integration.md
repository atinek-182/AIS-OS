# Integrating Superpowers Skill: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Integrate superpowers skill/workflow into the ZORIXEL AIOS.

## Summary / key decisions
- **Scope of Integration:** Integrate the superpowers skill/workflow based on the official `obra/superpowers` repository (https://github.com/obra/superpowers).
- **Local vs. Global Setup:** Copy the `using-superpowers` skill to `.agents/skills/using-superpowers/` and register it in `GEMINI.md` and `references/aios-user-manual.md`. Also setup globally by writing instructions in the global `AGENTS.md` to use the superpower skill in each project before anything else.
- **Global Rule Content:** Enforce the superpowers workflow in the global `AGENTS.md` by requiring scanning and invoking skills, plan-first, TDD, and rigorous verification.

## Q&A log
### Q1 — Scope of Integration
- Asked: Do you want to integrate the superpowers workflow by (1) copying local instructions, (2) cloning global plugin, or (3) both?
- Captured: The user provided the official GitHub link (https://github.com/obra/superpowers) and instructed to "do that." This means configuring the global `using-superpowers` skill and aligning the AIOS to follow the core superpowers workflow guidelines.
- Flags: none

### Q2 — Local Customization vs. Global Registration
- Asked: Do you want to copy the `using-superpowers` skill files to the local customizations folder and register it in GEMINI.md/user manual?
- Captured: The user said yes, and also requested a global setup by writing global instructions in the global `AGENTS.md` rule file to enforce using the superpower skill in each project before anything else.
- Flags: none

### Q3 — Proposed Global Rule Text
- Asked: Does the proposed global rules text (covering check-first, plan-first, TDD, and verification) meet your needs?
- Captured: The user approved the text exactly as written to enforce the superpowers workflow globally.
- Flags: none

### Q4 — Completeness Backstop
- Asked: Is there anything else we need to cover for the superpowers integration, or are we ready to lock in the plan and proceed to implementation?
- Captured: The user confirmed we are ready to implement: copying the skill, updating GEMINI.md, updating the user manual, creating the global AGENTS.md file, and logging all operations.
- Flags: none

## Open flags (pending input)
