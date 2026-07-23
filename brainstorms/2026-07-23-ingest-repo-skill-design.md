# Repository Ingestion & Skill Adaptation Engine (ingest-repo): Brainstorm / Discovery Notes
Date: 2026-07-23 · Goal: Design and implement an intelligent end-to-end repository ingestion, security audit, comparative analysis, roast council validation, and multi-artifact skill adaptation engine for AIOS.

## Summary / key decisions
- **Skill Command & Naming**: Primary skill is `/ingest-repo`, and `/ingest-skills` is upgraded as a full alias to route to the new 8-phase engine.
- **Two-Tier Feature Categorization & Automatic Search**: Tier 1 (Immediate active scripts/skills) vs. Tier 2 (Future research library under `skills-library/`). AI agent MUST automatically search and check all guides under `brain-aios/wiki/research/skills-library/` whenever relevant without prompting the user.

- **Adversarial Roast Council Gate (Mandatory Phase 5)**: Automatically spin up 5 persona agents in parallel (Contrarian, Expansionist, Logician, Researcher, Buyer) to roast the repo ingestion plan. Judge verdict (GO/RESHAPE/KILL) must address and resolve all objections before code generation.

## Q&A log
### Q1 — Command Name & Aliases
- Asked: How should we name and trigger this new skill?
- Captured: Primary skill `/ingest-repo`, upgrading `/ingest-skills` so both commands trigger the new 8-phase deep ingestion & roast council engine.
- Flags: None.

### Q2 — Feature Categorization & Auto-Search Rule
- Asked: How should `/ingest-repo` structure and handle features that provide immediate value vs. future potential?
- Captured: Two-tier strategy: Tier 1 (Active immediate scripts & skills) + Tier 2 (Future vault reference library in `brain-aios/wiki/research/skills-library/[repo-name]/`). Crucially: The AI must automatically check and scan all reference manuals in `skills-library/` whenever relevant without needing explicit prompt requests.
- Flags: None.

### Q3 — Mandatory Roast Council Integration
- Asked: How strictly should `/roast` be integrated into the repository ingestion pipeline?
- Captured: Mandatory Phase 5 Roast Council evaluation. All 5 personas run in parallel, and the Judge verdict must explicitly address every risk, flaw, or alternative before code is produced.
- Flags: None.

## Adversarial Roast Council Evaluation on Skill Design
- **Contrarian (6/10)**: Warns against workspace pollution and token leaks from uncleaned scratch clones. Fix: Strictly isolate clones in `scratch/ingest-[repo-name]/` and force cleanup post-ingestion.
- **Expansionist (9/10)**: Highlights huge leverage of turning any GitHub repo into active Antigravity skills and Obsidian research libraries autonomously.
- **Logician (8/10)**: Validates 8-phase logic and mandatory `validate_workspace_map.py` execution.
- **Researcher (8/10)**: Confirms progressive disclosure approach minimizes token context bloat.
- **Buyer/Developer (9/10)**: Saves hours of manual repo auditing, security checking, and skill authoring.

**Verdict: GO (High Confidence)**
Contrarian 6/10 · Expansionist 9/10 · Logician 8/10 · Researcher 8/10 · Buyer 9/10

## Open flags (pending input)
- None. All flags resolved.
