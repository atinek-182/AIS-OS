# Brainstorm Spec: /improve-system Skill

## Goal
Implement the `/improve-system` custom skill. The skill is designed to automatically analyze the current conversation transcript (`transcript.jsonl`) to:
1. Identify when the user iterated on a skill's output or provided correction feedback, and suggest corresponding updates to that skill's instructions (`.agents/skills/[skill-name]/SKILL.md`).
2. Identify when the user shared a personal lesson, story, or insight, and draft/save a new experience file to `brain-aios/wiki/experiences/`.
3. Link new experience files to `context/experiences/README.md` to keep them organized.
4. Flag any configurations, rules, or files that feel stale or duplicated.
5. Present a unified structured proposal to the user and request approval before modifying any files.
6. Suggest calling `/improve-system` after major milestones/changes (configured via prompt rules in `GEMINI.md`).

## Proposed Design & Architecture

### 1. Skill Manifest (`.agents/skills/improve-system/SKILL.md`)
- **Name:** `improve-system`
- **Description:** `"Use when the user wants to analyze the current session to update skill instructions, save lessons/experiences, or flag stale configurations."`
- **Argument-hint:** `[optional focus or specific skill/file]`
- **Model / Options:** `disable-model-invocation: true` (forces explicit invocation).

### 2. File Layout
- **Experiences Vault Path:** `brain-aios/wiki/experiences/YYYY-MM-DD-<slug>.md`
- **Experiences Index:** `context/experiences/README.md`
- **Skills Directory:** `.agents/skills/`
- **Root Decision Log:** `decisions/log.md`
- **General AIOS Log:** `brain-aios/wiki/log.md`
- **General AIOS Index:** `brain-aios/wiki/index.md`
- **Workspace Map:** `WORKSPACE_MAP.md`
- **System Prompt:** `GEMINI.md`

### 3. Step-by-Step Workflow
1. **Context Sourcing:**
   - Find the current conversation ID and read `<appDataDir>\brain\<conversation-id>\.system_generated\logs\transcript.jsonl`.
   - Read the optional focus argument if provided.
2. **Subagent Execution:**
   - Spawn a token-isolated subagent to analyze the transcript.
   - Instruct the subagent to extract:
     - **Skill Iterations:** Explicit corrections, guidelines refined, or output iterations.
     - **Lessons/Stories:** Principles or insights shared by the user.
     - **Stale/Duplicated Content:** Config files or instructions that seem redundant.
   - Subagent returns a structured JSON/markdown proposal.
3. **User Review Gate:**
   - Present the proposal in a clean layout.
   - Ask for confirmation: *"Would you like me to apply these updates to your system?"*
4. **Execution (Upon Approval):**
   - Write new experience files to `brain-aios/wiki/experiences/`.
   - Update `context/experiences/README.md` index.
   - Edit target skill `SKILL.md` instructions.
   - Flag stale configs to the user.
   - Append to logs (`decisions/log.md` and `brain-aios/wiki/log.md`).
   - Register any new file paths in `WORKSPACE_MAP.md` and `brain-aios/wiki/index.md`.
   - Register the new skill in `GEMINI.md`.

## Verification Plan
1. Validate directory structures.
2. Verify that `validate_workspace_map.py` runs and passes after updating files.
3. Test natural language triggering and slash command autocomplete.
