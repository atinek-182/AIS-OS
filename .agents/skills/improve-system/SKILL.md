---
name: improve-system
description: Use when the user wants to analyze the current session to update skill instructions, save lessons/experiences, or flag stale configurations.
argument-hint: [optional focus or specific skill/file]
disable-model-invocation: true
---

## What This Skill Does

Analyzes the current session transcript to identify:
1. Iterated skill outputs or user corrections to update existing skills.
2. Shared lessons or stories to capture in `brain-aios/wiki/experiences/` and index in `context/experiences/README.md`.
3. Stale or duplicated workspace configurations, rules, or files.

Proposes a structured update summary for user confirmation before applying changes.

## Steps

1. **Identify Session Context:**
   - Locate the active conversation's `transcript.jsonl` under `C:/Users/HP/.gemini/antigravity-ide/brain/<conversation-id>/.system_generated/logs/transcript.jsonl` (substituting the active `Conversation ID` from your session metadata).
   - Read the optional focus argument from `$ARGUMENTS` if provided.

2. **Analyze Session via Subagent:**
   - Spawn a token-isolated subagent to read the tail of `transcript.jsonl` (e.g. the last 100 steps or the whole session if small).
   - Task the subagent with identifying:
     - Any user corrections or refinements of skill outputs (e.g. "change skill X so it does Y").
     - Any lessons, experiences, or personal stories shared during the session.
     - Any stale or duplicated rules/files.
   - Have the subagent output a structured Markdown proposal with:
     - **Skill Changes:** exact diffs/edits proposed for `.agents/skills/[skill-name]/SKILL.md`.
     - **New Experiences:** filename, title, summary, and content for a new file in `brain-aios/wiki/experiences/`.
     - **Stale Configuration Flags:** list of files or rules to prune or flag.

3. **Present & Confirm:**
   - Present the subagent's structured proposal to the user.
   - Prompt: *"Would you like me to apply these updates to your system?"*

4. **Execute (On User Approval):**
   - Write the new experiences file(s) to `brain-aios/wiki/experiences/YYYY-MM-DD-<slug>.md`.
   - Update the index table in `context/experiences/README.md`.
   - Apply modifications to target skill `SKILL.md` files.
   - Register new experience files in `brain-aios/wiki/index.md`.
   - Append change summaries to:
     - `decisions/log.md` (for skill changes, workspace map updates).
     - `brain-aios/wiki/log.md` (for new experience files).
   - Update `WORKSPACE_MAP.md` if new directories or files were created.
