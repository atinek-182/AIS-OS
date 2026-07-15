# AIOS Skill Adaptation Redesign: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Resolve blind replacement issues in `agent-adapt` skill and upgrade AIOS capability to adapt Claude Code skills safely.

## Summary / key decisions
- **Decision 1**: Adopt a two-phase LLM-driven adaptation workflow (Scan & Query + Draft & Review) with search-first verification and interactive approval, rejecting regex-based shortcuts.
- **Decision 2**: Drive the adaptation process natively as an instruction-based skill in `SKILL.md` (deleting `disable-model-invocation: true`), utilizing the agent's LLM engine and web-search directly rather than a separate Python runner script.
- **Decision 3**: For non-equivalent Claude items (plugins, settings, or CLI commands), the agent must inject warning callouts (`> [!WARNING]`), outline workarounds (like MCP alternatives), and present them as interactive confirmation prompts, strictly avoiding blind name swaps.
- **Decision 4**: The adaptation workflow will proactively scan existing global and workspace skills before creating new ones. If a matching skill or one with overlapping functionality is found, the agent must check if they can be merged or reused to keep the AIOS lean and clean.
- **Decision 5**: Execute a staged batch migration (Raw Copy -> Scan & Categorize -> Batch Write & Verify) for all 122 legacy skills, generating a unified report for user approval to avoid manual review fatigue.

## Q&A log
### Q1 — Migration Strategy
- Asked: How should the AIOS handle third-party Claude skills instead of running a find-and-replace script?
- Captured: The user approved the two-phase LLM-driven adaptation workflow (Scan & Query + Draft & Review) with search-first verification and interactive approval. We must build a permanent, smart solution (an interactive tool adaptation engine) and reject shortcuts.
- Flags: None.

### Q2 — Transpiler Architecture
- Asked: Should the transpiler be driven by a Python script using external APIs, or should it be an instruction-based skill where the Antigravity agent uses its own LLM capabilities (web search, file reads/writes, interactive diff generation) to adapt files?
- Captured: The user confirmed it should be an instruction-based skill. We will modify `d:\AI-OS\.agents\skills\agent-adapt\SKILL.md` directly, removing the `disable-model-invocation` flag and converting the skill into a guide for the agent's LLM engine.
- Flags: None.

### Q3 — Handling Non-Equivalent Commands and Packages
- Asked: When adapting a Claude-specific step or command that has no direct Antigravity equivalent (e.g., a proprietary Claude plugin or API parameter), how should the agent adapt it?
- Captured: The user agreed to combine warning callouts and manual checklists:
  - No Blind Renames: Never rename a Claude command/package to antigravity if that target doesn't exist.
  - Warning Alerts: Inject a markdown warning alert (e.g. `> [!WARNING] This command is Claude-specific...`) above the command.
  - Workarounds: Outline alternative tools/MCPs if available; otherwise, flag it as a manual action item for the user.
- Flags: None.

### Q4 — Skill Deduplication & Reuse
- Asked: How should the adaptation workflow utilize existing custom skills in the workspace?
- Captured: The agent should scan existing global and workspace skills (`.agents/skills/` and `C:\Users\HP\.gemini\config\skills/`) to check if any existing skill already solves the target problem or can be reused. This prevents duplicate skills and makes the system stronger.
- Flags: None.

### Q5 — Executing Batch Migration
- Asked: How should we execute the migration of your 122 legacy skills right now without causing prompt fatigue?
- Captured: The user approved the staged batch migration: Stage 1 (Raw Copy), Stage 2 (Batch Transpilation), Stage 3 (Commit & Verify) to run the pipeline on all custom skills.
- Flags: None.

## Open flags (pending input)
- None.








