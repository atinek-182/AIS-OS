---
name: improve-system
description: Analyze the current session transcript to update skill instructions, save lessons, update memory, and prune stale configurations.
argument-hint: "[optional focus or specific file]"
---

# System Self-Improvement Workflow

Use this skill when you finish a major milestone, significantly refine a custom skill, or want to log a critical life/business lesson learned during the session.

## Triggering Rules
- Proactively recommend invoking `/improve-system` at the end of a session where significant architectural iterations, bug workarounds, or custom skill updates occurred.
- Triggered when the user runs `/improve-system` or asks to "improve the system", "save lessons", "update memory", or "log this experience".

## Execution Workflow

### Step 1: Ingest Session Logs
1. Locate the active conversation's `transcript.jsonl` under:
   `C:/Users/HP/.gemini/antigravity-ide/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`
   (Substituting the active `Conversation ID` from your session metadata).
2. Scan the transcript backward to identify key user prompts, corrections, and tool failure workarounds (e.g. Playwright permission errors, Git pre-commit hook alerts, custom script bugs).

### Step 2: Extract & Categorize Insights
Identify and parse three distinct categories of improvements:
1. **Developer Lessons / Stories**: High-leverage developer insights (e.g., node static server bypasses, selective component extraction, design taste boundaries).
2. **Skill / System Refinements**: Corrections made to `.agents/skills/` configurations, templates, or instructions.
3. **Implicit User Preferences**: Repeated user feedback regarding formatting, communication style, coding simplicity, or layout taste.
4. **Stale Configurations**: Orphaned workspace files, obsolete rules in `AGENTS.md`, or broken links in Obsidian indexes.

### Step 3: Compile System Update Proposal
Create a structured Markdown proposal for the user containing:
- **Learnings & Experiences**: Title, date, detailed story, and system guidelines to be written.
- **Skill Updates**: Proposed diffs for target `.agents/skills/[skill-name]/SKILL.md` files.
- **Memory & Rules Updates**: Diffs or additions for `MEMORY.md` (user preferences) or `AGENTS.md` (coding rules).
- **Pruning & Cleanup Plan**: List of files to delete, move to `archives/`, or register in `WORKSPACE_MAP.md`.

Wait for the user's explicit confirmation: *"Would you like me to apply these updates to your system?"*

### Step 4: Execute approved changes
Upon approval, perform the following edits:
1. **Write Experience Document**:
   - Create a new markdown file in `brain-aios/wiki/experiences/YYYY-MM-DD-[slug].md`.
   - Update the table of contents index in `context/experiences/README.md`.
2. **Modify Skills**:
   - Apply edits to the designated `.agents/skills/[name]/SKILL.md` files.
3. **Update Memory & Rules**:
   - Update user preferences in `MEMORY.md`.
   - Update coding rules in `AGENTS.md`.
4. **Clean & Log**:
   - Remove any temporary scratch files or unused scripts.
   - Log decisions in `decisions/log.md` (workspace changes) and `brain-aios/wiki/log.md` (Obsidian index changes).
   - Ensure the Git pre-commit validators (`validate_links.py` and `validate_workspace_map.py`) are run to confirm the system's structural integrity.

---

## Experience Document Template

Files created in `brain-aios/wiki/experiences/` must follow this structure:

```markdown
# [Title of the Experience]

## Lesson / Story
[A narrative paragraph explaining what happened, the problem encountered, and how it was solved.]

## System Guidelines Established
- **[Constraint/Rule Name]:** [The concrete guideline to prevent this issue in the future.]
- **[Constraint/Rule Name]:** [Another concrete guideline.]
```
