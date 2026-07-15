# AIOS Git Hook Workspace Map Validation: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Design and implement a Git pre-commit hook to verify that all directories, junctions, and configs are mapped in WORKSPACE_MAP.md before committing changes.

## Summary / key decisions
- **Decision 1**: Implement the map validation check in `scripts/validate_workspace_map.py`, scanning root files/folders, custom skill subfolders inside `.agents/skills/`, and reference files in `references/`.
- **Decision 2**: Deploy the pre-commit hook file directly to `.git/hooks/pre-commit` and check in a tracked backup copy at `scripts/hooks/pre-commit` to prevent local hook loss.



## Q&A log
### Q1 — Validation Script Scope
- Asked: What items at the workspace root should the Git pre-commit hook check against `WORKSPACE_MAP.md`?
- Captured: The script will check all immediate files/folders at the workspace root, plus key nested directories:
  * Root-level files and folders (excluding `.git`, `.obsidian`, `.gitignore`, `.gitattributes`, `.env`, and `node_modules`).
  * Immediate subfolders inside `.agents/skills/` (e.g., each custom skill folder).
  * Reference markdown files inside `references/`.
  * Behavior: Any unmapped item blocks the commit and exits with code 1.
- Flags: None.

### Q2 — Hook Deployment and Versioning
- Asked: Should the pre-commit hook file be created automatically by a setup script, or should we write it directly to `.git/hooks/pre-commit`?
- Captured: Write directly to `.git/hooks/pre-commit` and maintain a tracked backup copy at `scripts/hooks/pre-commit` to prevent local hook loss.
- Flags: None.

## Open flags (pending input)
- None.

