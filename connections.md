# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Bank Account & UPI (tracked via Google Sheets) | not yet connected | — | — |
| 2 | Customer interactions | Instagram DMs / Gmail / Website Contact Form | not yet connected | — | — |
| 3 | Calendar | Google Calendar (inferred from Gmail) | not yet connected | — | — |
| 4 | Communication | WhatsApp / Telegram / YouTube Comments | not yet connected | — | — |
| 5 | Project / task tracking | Obsidian Master Task List | local_path (Junction: brain-aios/) | — | 2026-07-14 |
| 6 | Meeting intelligence | None (no meetings/calls recorded) | not yet connected | — | — |
| 7 | Knowledge / files | Obsidian (Second Brain) / Google Drive / GitHub / Local | local_path (Junctions: brain-aios/, second-brain-zorixel/) | — | 2026-07-14 |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
