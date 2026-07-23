# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Bank Account & UPI (tracked via Google Sheets) | not yet connected | — | — |
| 2 | Customer interactions | Instagram DMs / Gmail / Website Contact Form | script (GWS CLI) | — | 2026-07-14 |
| 3 | Calendar | Google Calendar (inferred from Gmail) | script (GWS CLI) | — | 2026-07-14 |
| 4 | Communication | WhatsApp / Telegram / YouTube Comments | script (GWS CLI) | — | 2026-07-14 |
| 5 | Project / task tracking | Obsidian Master Task List | local_path (Junction: brain-aios/) | — | 2026-07-14 |
| 6 | Meeting intelligence | None (no meetings/calls recorded) | not yet connected | — | — |
| 7 | Knowledge / files | Obsidian (Second Brain) / Google Drive / GitHub / Local | local_path (Junctions: brain-aios/, second-brain-zorixel/) | — | 2026-07-14 |
| 8 | External Documentation | Upstash Context7 | mcp | — | 2026-07-15 |
| 9 | Code Structure Mapping | Codegraph | mcp | — | 2026-07-15 |
| 10 | Headless Browser Driver | Playwright | mcp | — | 2026-07-15 |
| 11 | Repository Management | GitHub | mcp | GITHUB_PERSONAL_ACCESS_TOKEN | 2026-07-15 |
| 12 | UI Component Sourcing | Magic | mcp | API_KEY | 2026-07-15 |
| 13 | Browser Diagnostics | Chrome DevTools | mcp | — | 2026-07-15 |
| 14 | Document Database | Notion | mcp | OPENAPI_MCP_HEADERS | 2026-07-15 |
| 15 | Design Context Extraction | Figma | mcp | PAT | 2026-07-19 |
| 16 | Stealth Web Data Extraction | Scrapling | script | local_python | 2026-07-23 |
| 17 | Multi-Platform Internet Engine | Agent Reach | skill | local_cli + keyring | 2026-07-23 |



**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
