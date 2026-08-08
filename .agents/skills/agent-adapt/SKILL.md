---
title: Skill
domain: skill
summary: 'This skill supports **Tri-Mode Flexible Execution**: - **Slash Command**: Explicitly run `/agent-adapt [optional
  parameters]` in chat.'
critical_directives:
- Rules for Translation:**
- 'Inject a warning callout block above the command:'
- Warnings added for Claude-only steps.
- 'System Rules Update**: Updates registered skill paths in **`GEMINI.md`** and **`WORKSPACE_MAP.md`**.'
section_outline:
- Invocation & Tri-Mode Routing
- What This Skill Does
- Steps
- 'Step 1: Pre-Migration Deduplication Check'
- 'Step 2: Extract & Inspect Claude-Specific References'
read_triggers:
- When working on skill in .agents/skills/agent-adapt/SKILL.md
- When reading context for Skill
tags:
- skill
- SKILL
updated: '2026-08-08'
name: agent-adapt
description: Migrate, adapt, or copy custom skills, prompts, or files from Claude Code standard to native Antigravity standard,
  avoiding blind find-and-replaces. Invokable directly via /agent-adapt.
argument-hint: '[optional parameters]'
---

## Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/agent-adapt [optional parameters]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills or subagents via `/agent-adapt` or by reading `SKILL.md` directly.



## What This Skill Does

This skill coordinates the migration and adaptation of legacy coding plugins, custom skills, and configuration files from Claude Code conventions to native Antigravity standards. Instead of executing fragile regex find-and-replaces, this skill uses a smart, two-phase, interactive workflow: scanning files, searching the web for correct package and command equivalents, warning the user about Claude-specific items without direct equivalents, and asking for explicit confirmation before writing any changes.

---

## Steps

### Step 1: Pre-Migration Deduplication Check
- Before copying or modifying any files, list all current skills in `.agents/skills/` and global customizations at `C:\Users\HP\.gemini\config\skills/`.
- Check if the target legacy skill's functionality or name already exists in the workspace or global configuration.
- If a matching or highly overlapping skill is found, prompt the user with details and ask whether they want to **merge**, **overwrite**, or **skip**.

### Step 2: Extract & Inspect Claude-Specific References
- Read the content of the legacy files (`SKILL.md`, accompanying scripts, JS/TS, or JSON configs) to be adapted.
- Scan for and extract all:
  - CLI command executions (e.g. `claude`, `npx @google/claude-code`, `claude config`, `claude plugin install`).
  - Package installation names and registries.
  - Settings, parameters, and environment variables (e.g. `CLAUDE_SESSION_ID`).
  - URLs and repository paths (e.g. `github.com/google/claude-code`).

### Step 3: Web-Search and Map Equivalents
- For each extracted Claude-specific reference, run a web search to verify the correct native Antigravity equivalent.
- **Rules for Translation:**
  - **Verified equivalents:** Replace the legacy term with the verified Antigravity command or package.
  - **General text:** Safely translate descriptive text (e.g. `Claude Code` -> `Antigravity`, `CLAUDE.md` -> `GEMINI.md`, `.claude` -> `.agents`), ensuring Nate Herk's Three Ms of AI™ copyright and any original author/trademark attributions are kept intact.
  - **Unverified/Claude-only equivalents:** If no direct Antigravity equivalent exists (e.g., proprietary Claude plugins or internal APIs), **DO NOT** rename the string to "antigravity" (e.g. do not turn `@google/claude-code` into `@google/antigravity`). Instead:
    - Inject a warning callout block above the command:
      ```markdown
      > [!WARNING]
      > The command/package below is Claude-specific. Ensure you have the corresponding native setup.
      ```
    - Check if there are known workarounds (e.g., alternative MCP tools, custom scripts) and document them.
    - Flag the item for manual review.

### Step 4: Interactive Review & Diff Approval
- Present a clean Git-style diff (or bulleted summary of proposed changes) to the user.
- Detail:
  - Scanned files.
  - Files to create/modify.
  - Specific command/link translations performed.
  - Warnings added for Claude-only steps.
- **WAIT FOR EXPLICIT USER APPROVAL** before writing any modified files to `.agents/skills/` or `C:\Users\HP\.gemini\config\skills/`.

### Step 5: Post-Adaptation Verification
- Once files are written, run automated checks (like `verify_skills.py`) to confirm that:
  - Frontmatter delimiters parse correctly.
  - The skills load without syntax or formatting issues.
  - Any associated custom scripts have execution permissions.

---

## Inter-Skill Connections & Handoff Pipeline
- **Repository Ingestion**: Invoked by **`/ingest-repo`** during Phase 6 to adapt Claude Code skill references into Antigravity standards.
- **Skill Quality Audit**: Hands off newly adapted skills to **`/skill-builder`** to run the No-Op test and dual-trigger frontmatter validation.
- **System Rules Update**: Updates registered skill paths in **`GEMINI.md`** and **`WORKSPACE_MAP.md`**.

---

## Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

