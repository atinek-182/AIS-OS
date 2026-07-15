# AIOS Validator Refinement & Duplicate Cleanup: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Refine the python validator script substring check logic and prune duplicate custom skills in the global configuration directory.

## Summary / key decisions
- **Decision 1**: Refine `scripts/validate_workspace_map.py` to use a regular expression that matches filenames either wrapped in markdown links (e.g. `[filename](file:///...)` or `file:///.../filename`) or code backticks (e.g. `` `filename` ``).
- **Decision 2**: Remove the duplicate global custom skill folders `agent-adapt`, `grill-me`, and `using-superpowers` from the global configuration directory `C:\Users\HP\.gemini\config\skills\`.


## Q&A log
### Q1 — Exact Boundary Validation Logic
- Asked: How should `validate_workspace_map.py` match names in `WORKSPACE_MAP.md` to avoid substring false positives (like `log.md` matching `decisions/log.md`)?
- Captured: Parse the map file and find filenames explicitly referenced inside markdown link labels, link targets, or backticks: e.g., `[filename](file:///...)`, `file:///.../filename`, or `` `filename` ``.
- Flags: None.


### Q2 — Duplicate Skills Cleanup
- Asked: Confirming the exact list of duplicate global skills to remove and the deletion mechanism.
- Captured: Delete `agent-adapt`, `grill-me`, and `using-superpowers` from the global `skills` directory since they exist locally in `.agents/skills/`.
- Flags: None.

## Open flags (pending input)
- None.


