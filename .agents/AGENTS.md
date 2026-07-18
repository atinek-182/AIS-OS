# Workspace Rules

## Maintenance of WORKSPACE_MAP.md

- When creating a new folder, junction, or config file (like adding an MCP server or utility script), you MUST update [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) immediately before concluding the task.

## System Self-Improvement
- Suggest invoking `/improve-system` when:
  - A custom skill's output is iterated upon or corrected multiple times.
  - A significant lesson, decision, or business story is shared by the user.
  - Do NOT suggest it for minor syntax fixes or small one-off file edits. Suggest it only for high-leverage changes.

## Adapting Skills to Antigravity & Gemini
- Whenever reading or invoking any custom skill, prompt, or reference guide (especially those originally written for Claude Code, Cursor, or other AI agents):
  1. Scan the contents for platform-specific references (e.g., `Claude`, `Claude Code`, `Cursor`, `.claude/skills/`) and dynamically adapt them to `Antigravity` or `Gemini` equivalents.
  2. Preserve all core execution logic, design frameworks, and copywriting/audit guidelines without changing their meaning or losing their original capabilities.
  3. Run all tests, verifications, and directory-level checks strictly under the Antigravity environment.

## Sandboxed Font Rendering & SVG Outline Layouts
- Never assume local asset files load via `file:///` inside headless browser screenshots (Playwright); always prefer base64 Data URIs for local fonts in temporary HTML pages.
- Double-check that user-finalized fonts (e.g. `Nuqun` logo, `Rosehot` headings, `Outfit` body) are strictly preserved, and avoid switching brand typefaces.
