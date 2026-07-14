---
name: agent-adapt
description: Use when someone asks to migrate, install, adapt, or copy skills, plugins, prompts, or files from Claude Code standards to Antigravity standards.
disable-model-invocation: true
---

## What This Skill Does

This skill coordinates the migration and adaptation of coding plugins, custom skills, and configuration files from Claude Code conventions to native Antigravity standards. It prioritizes searching for native ports, handles file copying/replacements as a last resort, cleans up Claude CLI traces, and enforces verification testing exclusively under the Antigravity platform.

---

## Steps

### Step 1: Research Native Antigravity Equivalents First
- Before downloading any Claude Code plugin, search the web (GitHub, documentation) to check if a native Antigravity port or equivalent exists.
- **CRITICAL RULE:** If the guide or links refer to Claude Code, you MUST prioritize finding a native Antigravity installation path rather than downloading for Claude and copy-pasting.
- **Last Resort Confirmation:** Only copy-paste Claude configurations to Antigravity if no native port exists, and *only* after showing the plan and receiving explicit user confirmation.

### Step 2: Install Native Ports or Copy Files
- If a native Antigravity plugin/package is found, install it in your Antigravity environment.
- If copying local Claude skill files (from `C:\Users\HP\.claude\skills/` or marketplace clones) is confirmed:
  - Copy the target skill folders recursively to the Antigravity global customization directory (`C:\Users\HP\.gemini\config\skills/`) or workspace customizations directory (`.agents/skills/`).

### Step 3: Run Adapt Replacements in Copied Files
- Recursively scan all copied text-based files (`.md`, `.json`, `.txt`, `.py`, `.js`, `.ts`) and perform the following exact string replacements:
  - `Claude Code` -> `Antigravity`
  - `Claude` -> `Antigravity`
  - `CLAUDE.md` -> `GEMINI.md`
  - `.claude` -> `.agents`
  - `CLAUDE_SESSION_ID` -> `ANTIGRAVITY_SESSION_ID`
  - `claude` -> `antigravity`
  - `claude-code` -> `antigravity`
- Preserve structural instructions, attributions, and authors unchanged.

### Step 4: Clean Up Claude CLI Traces
- Run `claude plugin uninstall <plugin>` for any duplicate plugins in the Claude CLI so that its internal registry remains clean.
- Delete the local Claude Code skills/plugins directories (like `C:\Users\HP\.claude\skills/` and conflicting marketplace folders) to prevent configuration clutter and duplicate memory writes.

### Step 5: Demo Test Under Antigravity Only
- **CRITICAL RULE:** Never execute verification commands or demo tests in the Claude CLI. Always run checks, syntax verification, and simulation scripts under the Antigravity CLI and environment.
- Verify that:
  - The copied skills load without frontmatter errors.
  - The slash commands trigger correctly in Antigravity.
  - Dynamic arguments substitute correctly.

### Step 6: Log Decisions & Indexes
- Append a detailed entry to the root Decisions Log ([log.md](file:///d:/AI-OS/decisions/log.md)).
- Update and index the references inside the Obsidian vaults:
  - [brain-aios index](file:///d:/AI-OS/brain-aios/wiki/index.md)
  - [second-brain-zorixel index](file:///d:/AI-OS/second-brain-zorixel/wiki/index.md)

---

## Guardrails & Notes

- **No Claude Testing:** Do not attempt to run `claude plugin list` or similar checks to verify Antigravity functionality. Test exclusively against Antigravity files/commands.
- **Attribution Guard:** Maintain Nate Herk's Three Ms of AI™ copyright and other source trademarks intact in all adapted documents.
- **Confirm Before Direct Copying:** Always report search results first and request approval before moving Claude directories.
