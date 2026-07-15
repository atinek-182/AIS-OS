# AIOS Directory Map and Configuration Registry: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Design and implement a centralized index/map of config files, manuals, logs, and assets to prevent workspace fragmentation.

## Summary / key decisions
- **Decision 1**: Create a new root-level index file `WORKSPACE_MAP.md` that maps out config directories, skills, scripts, connections, and logs. Link this file in `GEMINI.md` and both Obsidian vault indexes.
- **Decision 2**: Include a Read/Write Policy & Log Alignment Table in `WORKSPACE_MAP.md` to define explicit boundaries and logging rules for each vault, scripts, and general AIOS repositories.
- **Decision 3**: Codify maintenance rule in `AGENTS.md` and update `/review-day` instructions to require updating `WORKSPACE_MAP.md` whenever the workspace layout changes.




## Q&A log
### Q1 — Directory Map Location
- Asked: Where should the centralized configuration and directory map live in the AIOS?
- Captured: The user agreed to create a new root markdown file named `WORKSPACE_MAP.md` to map out all config directories, scripts, connections, logs, and skills. We will link this file in `GEMINI.md` and both Obsidian indexes (`brain-aios` and `second-brain-zorixel`).
- Flags: None.

### Q2 — Directory Write Policies & Log Alignment
- Asked: Should the workspace map include a "write policy" for each directory to enforce the log alignment rules?
- Captured: The user confirmed we should include a Read/Write Policy & Log Alignment Table in `WORKSPACE_MAP.md` to prevent LLMs from drifting and keeping Obsidian/Git boundaries separated.
- Flags: None.

### Q3 — Map Maintenance and Drift Prevention
- Asked: How should we ensure the WORKSPACE_MAP.md is updated when the workspace layout changes in the future?
- Captured: The user confirmed we should codify a rule in `AGENTS.md` requiring the agent to update `WORKSPACE_MAP.md` immediately upon layout changes, and to integrate a check in `/review-day` skill to verify map alignment during wrap-ups.
- Flags: None.

## Open flags (pending input)
- None.

