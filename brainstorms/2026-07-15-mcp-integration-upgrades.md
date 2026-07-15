# Global MCP Integration: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Integrate 6 new global MCP servers (context7, codegraph, playwright, github, magic, chrome-devtools-mcp, notion-mcp-server) into the ZORIXEL AIOS, download and install related skills, and update all manuals and guides.

## Summary / key decisions
- **GitHub Integration:** Automate PR babysitting, issue triage, and git workflows.
- **Playwright & Chrome DevTools Integration:** Automate frontend visual tests, DOM inspecting, and accessibility (a11y) audits.
- **Notion Integration:** Sync decision logs, content strategy, or task checklists directly to Notion pages/databases.
- **Magic Integration:** Retrieve UI design inspiration, search brand logos, and build components.
- **Codegraph Integration:** Build and query interactive codebase maps.
- **Notion Skill:** Create a new custom workspace skill `notion-sync` under `.agents/skills/notion-sync/SKILL.md` to orchestrate syncing workspace logs, decision records, and checklists to Notion pages/databases.
- **Modular Documentation:** Create individual API guides in `references/` for each new integration (e.g., `notion-api.md`, `github-api.md`, `playwright-api.md`, `codegraph-api.md`, `magic-api.md`, `chrome-devtools-api.md`).
- **Dynamic Configuration:** Design skills and guides to consume parameters dynamically (e.g. environment variables or prompt inputs) rather than hardcoding specific Notion database IDs or GitHub repositories.

## Q&A log
### Q1 — Primary MCP Workflows
- Asked: What are the primary workflows or tasks you want the ZORIXEL AIOS to automate using these new MCP servers?
- Captured: Selected all standard workflows for GitHub, Playwright/Chrome-DevTools, Notion, Magic, and Codegraph to align with the core AIOS automation suite.
- Flags: none

### Q2 — Notion Skill Integration
- Asked: Would you like to create a new custom skill for Notion integration, or just document the tool usage in the manuals?
- Captured: Create a new custom `notion-sync` skill under `.agents/skills/notion-sync/SKILL.md`.
- Flags: none

### Q3 — Reference Documentation Structure
- Asked: How would you like to structure the reference API guides for these new MCP servers?
- Captured: Create separate modular reference files for each MCP server (e.g. `references/notion-api.md`, etc.).
- Flags: none

### Q4 — Hardcoded IDs vs. Dynamic Configuration
- Asked: Do you have specific Notion database/page IDs or GitHub repo structures to hardcode, or should we make them dynamic?
- Captured: Design the skills and documentation dynamically using standard placeholders and environment variables.
- Flags: none

## Open flags (pending input)
