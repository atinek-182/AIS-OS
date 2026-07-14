---
name: agent-adapt
description: Use when you want to scan and tweak skills, prompts, or files in the project workspace to migrate them from Claude Code to Antigravity.
disable-model-invocation: true
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually first.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk.
---

## What This Skill Does

Scans skills, references, or other project files and migrates Claude-specific terms and path references to Antigravity standards.

---

## Steps

1. Check if a specific file or directory is passed as `$ARGUMENTS`. 
   - If not specified, default to scanning the entire project workspace root recursively.
2. Find all text-based files (specifically `.md`, `.json`, `.txt`, `.py`, `.js`, `.ts`) in the target path.
3. For each file found, scan for and replace the following patterns:
   - `Claude Code` -> `Antigravity`
   - `Claude` -> `Antigravity`
   - `CLAUDE.md` -> `GEMINI.md`
   - `.claude` -> `.agents`
   - `CLAUDE_SESSION_ID` -> `ANTIGRAVITY_SESSION_ID`
4. Apply the replacements in-place without altering the structural instructions, logic, or workflows of the skill.
5. Print a report listing:
   - All scanned files
   - Any files modified
   - A summary of replacements made per file

---

## Guardrails & Notes

- **Read-Only Safeties**: Do not touch files in `.git/`, `.obsidian/`, `node_modules/`, or any binary assets (images, PDFs).
- **Exact Replacement Only**: Do not rewrite sentences or change workflow descriptions. Maintain identical instructions and formatting.
- **Attribution**: Do not delete any trademark or author attribution notices in the files.
