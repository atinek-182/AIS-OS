---
name: agent-adapt
description: Migrate, adapt, or copy custom skills, prompts, or files from Claude Code standard to native Antigravity standard, avoiding blind find-and-replaces.
---

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

