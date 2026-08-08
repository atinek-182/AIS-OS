# ZORIXEL AIOS Global Error Prevention & Execution Rules Registry

> **MANDATORY BOOTUP RULE FOR ALL AI AGENTS & CHAT SESSIONS:**  
> Every AI agent, subagent, and LLM chat session operating in `d:\AI-OS` MUST read and strictly enforce every rule in this document. Never bypass, ignore, or relax these safeguards.

---

## ⚡ SECTION 1: PERMANENT TERMINAL, API, SHELL & OS ERROR PREVENTION RULES

### Error Categorization Matrix & Execution Safeguards

| Rule ID | Category | Fatal Impact | Permanent Prevention Rule |
|---|---|---|---|
| **Rule 1.1** | **Shell & Execution** | High | **PowerShell Inline Code Isolation**: Never pass inline Python scripts containing double quotes, parens, or complex expressions inside PowerShell string parameters. ALWAYS write Python code to a `scratch/*.py` file using `write_to_file` and execute `python scratch/*.py`. |
| **Rule 1.2** | **Path & Binary** | High | **Windows Batch Executable Resolution**: Npm CLI binaries on Windows OS are `.cmd` batch files (`gws.cmd`). Python `subprocess.run(["gws", ...], shell=False)` causes `WinError 2`. ALWAYS resolve `shutil.which("<cmd>")` or invoke Node directly: `node C:\Users\HP\AppData\Roaming\npm\node_modules\@googleworkspace\cli\run.js`. |
| **Rule 1.3** | **CLI Wrapper** | Medium | **Multicall Bridge String Isolation**: Avoid inline shell variable chaining or complex multi-line semicolon scripts in raw `run_command` calls. Wrap multi-step environment or file operations inside standalone Python scripts. |
| **Rule 1.4** | **OAuth Auth** | High | **Pre-Flight OAuth Verification**: Google Workspace CLI refresh tokens expire after inactivity. ALWAYS execute `python scripts/aios_gws_health_check.py` to verify authentication state before running GWS batch automations. If `invalid_grant` occurs, trigger `node run.js auth login`. |
| **Rule 1.5** | **Argument Passing** | High | **Windows `cmd.exe` JSON Quote Safety**: Windows `cmd.exe` strips outer quotes when `shell=True` is used, corrupting stringified `--json` payloads. ALWAYS execute Node directly with `shell=False` passing Python `json.dumps(payload)` via `subprocess.run([...], shell=False)`. |
| **Rule 1.6** | **GCP Platform** | High | **GCP API Enablement Link Handling**: Newly initialized GCP projects have individual service APIs turned off by default. When an HTTP 403 `accessNotConfigured` or `has not been used` error occurs, intercept the response and present direct console enable URLs (e.g. `https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=zorixel-aios`). |
| **Rule 1.7** | **Encoding** | Low | **Windows Standard Output UTF-8 Encoding**: Windows console defaults to legacy ANSI codepage `cp1252`, causing `UnicodeEncodeError` when printing unicode symbols like `✓`. ALWAYS use standard ASCII tags (`[OK]`, `[SUCCESS]`, `[ERROR]`) in terminal output, add `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` at the top of Python CLI scripts, and set `PYTHONIOENCODING=utf-8` or `python -X utf8`. |
| **Rule 1.8** | **Formula Engine** | High | **Notion Formula 2.0 Browser Web API Ban**: Notion Formula 2.0 does NOT contain JavaScript browser Web APIs (`encodeURIComponent()`, `window`, `fetch`). ALWAYS pre-encode URL strings using `%20` (space) and `%0A` (newline) and replace spaces dynamically using `replaceAll(prop("Column"), " ", "%20")`. |
| **Rule 1.9** | **Formula Engine** | High | **Notion Formula 2.0 Defensive Null Guards**: Direct string concatenation or math on empty/null database properties crashes on blank rows. ALWAYS wrap every property reference in defensive `if(empty(prop("Column")), fallback, value)` guards. |
| **Rule 1.10** | **Web Endpoint** | Low | **Notion Developer Portal Endpoint Rules**: Notion updated developer dashboard routes from `/my-integrations` to `https://app.notion.com/developers/connections`. Use updated endpoints in all guides and link checks. |
| **Rule 1.11** | **API Protocol** | Low | **Notion Secret Key Prefix Dual Support**: Notion integration tokens support both legacy `secret_` and modern `ntn_` prefixes. Support both prefixes in validation scripts and documentation. |
| **Rule 1.12** | **Tool Parameter** | Medium | **Non-Artifact Path Metadata Rejection**: Passing `ArtifactMetadata` inside `write_to_file` calls for normal workspace paths outside `C:\Users\HP\.gemini\antigravity-ide\brain\<conv-id>` causes schema validation errors. ALWAYS omit `ArtifactMetadata` when writing project codebase files. |
| **Rule 1.13** | **Font Rendering** | High | **Headless Browser Base64 Font Enforcement**: Headless Playwright browsers cannot resolve local OS font paths (`file:///`) in temporary HTML files. ALWAYS inline `.otf` / `.ttf` files as Base64 Data URIs (`data:font/opentype;base64,...`) inside CSS `@font-face` blocks for 100% deterministic visual rendering. |
| **Rule 1.14** | **Typography Layout** | Medium | **Large Display Headline Line-Height Safety**: Headlines larger than `64px` in custom display typefaces (such as `Havock`) require explicit `line-height: 1.28` and minimum `margin-bottom: 28px` to prevent multi-line collision with subheadings. |
| **Rule 1.15** | **Media Ingestion** | Low | **User-Uploaded Image Extraction**: Images attached in chat by the operator are saved under `<appDataDir>\brain\<conv-id>\media__*.png`. ALWAYS inspect the brain directory and copy uploaded images to project visual asset folders before embedding in web pages. |
| **Rule 1.16** | **Multi-File Sync** | Medium | **Dual-Presentation File Mirroring**: When maintaining multiple presentation HTML files (e.g. `vashishthya_loom_presentation.html` and `notion_google_sync_presentation.html`), use a central python compiler script (`scripts/build_loom_presentation.py`) to compile both files simultaneously to prevent file drift. |
| **Rule 1.17** | **Graphic Geometry** | Medium | **SVG Stroke Bleed Prevention**: Never apply CSS or SVG `stroke` or `stroke-width` attributes to converted text path SVGs that contain inner counter holes ('o', 'e', 'a'). Enforce pure solid fills with `fill-rule="evenodd"`. |
| **Rule 1.18** | **Font Rendering** | High | **Native Base64 Font Logotype Standard**: For brand logotypes and text badges, prefer inline base64 `@font-face` web font rendering (`Nuqun-Regular.otf`) over converted static SVG path vectors to guarantee 100% vector accuracy and eliminate path coordinate corruptions. |
| **Rule 1.19** | **PDF Compilation** | Low | **Dark-Mode PDF Background Enforcement**: When compiling dark-mode PDFs using Playwright headless browser, ALWAYS set `print_background=True` in script options and assign dark background styles directly to `body` and root containers to eliminate white margin bleed. |
| **Rule 1.20** | **Process Execution** | High | **Windows Subprocess CLI Binary Resolution**: On Windows OS, CLI binaries resolved via `subprocess.run` MUST explicitly check `shutil.which` or invoke Node directly (`shell=False`) to prevent `WinError 2` file not found exceptions. |
| **Rule 1.21** | **Repository Ingestion** | Medium | **Scratch Isolation & Vault Bloat Prevention**: When ingesting external repositories, clone strictly inside `scratch/ingest-[repo-slug]/` and force-delete the scratch folder post-ingestion. NEVER dump full unpruned git repositories into `skills-library/` unless explicitly requested. |

---

## 🎯 SECTION 2: USER INSTRUCTION-TO-DELIVERY FIRST-TRY POLICIES

To eliminate delivery iterations and ensure AIOS succeeds on the FIRST attempt:

1. **Flyer & Media Intake Policy**: When given raw promotional images, flyers, or text briefs, immediately parse and structured-write the content into `01-research-and-audits/SERVICES_CATALOG.md` before designing systems or user UI.
2. **Client SaaS Cost Policy**: Default all non-tech founder client deliverables to Client-Owned Google Apps Script + Notion Native Engine (100% zero subscription fees). Never introduce Make.com or n8n monthly subscriptions unless explicitly ordered.
3. **Google Apps Script Live Sync Policy**: When syncing Notion databases to Google Sheets via Apps Script, ALWAYS use dynamic runtime header mapping (`getHeaderMap(sheet)`) so column reordering or additions in Google Sheets never break the script.
4. **Setup Documentation Standard**: Every technical handoff MUST deliver both a Markdown SOP (`.md`) in `03-pitch-and-loom-guides/` and an Interactive HTML Setup Dashboard (`.html`) in `04-visual-assets-and-previews/` with copyable code blocks (`user-select: all`).
5. **Notion AI Prompt Standard**: Provide a single, copyable Notion AI Master Prompt alongside manual property schema tables so operators can build databases in 1 click.
6. **WhatsApp Formula Standard**: All auto-generated WhatsApp click links MUST use pre-encoded `%20` / `%0A` formatting, dynamic regex phone sanitization `replaceAll(prop("Phone"), "[^0-9]", "")`, and defensive `if(empty(...))` wrappers for name, status, and financial balances.
7. **Google Workspace Provisioning Standard**: Run all `gws` CLI operations via direct Node execution (`shell=False`) in Python scripts to guarantee 100% deterministic sheet creation, tab formatting, and permission sharing.
8. **Web Article Ingestion & Defuddle Standard**: When ingesting web articles, technical blog posts, or documentation into AIOS research vaults or LLM context, use `npx defuddle parse <source> --markdown --frontmatter` to strip DOM clutter, preserve code blocks and math formulas, and prepend structured YAML metadata.
9. **YouTube Transcript & Media Extraction Standard**: Always default to local `yt-dlp` (via `python scripts/youtube_skills_runner.py transcript --url <URL>`) for 100% free, zero-token transcript extraction. Cascade automatically to TranscriptAPI (`TRANSCRIPT_API_KEY`) as a secondary fallback if cloud IP blocks or anti-bot restrictions occur.
10. **Composio SaaS Integration & Zero-Fee Boundary Standard**: Default to native zero-fee tools (`gws`, `gh`, Notion MCP) for Google Workspace, GitHub, and Notion. Use `/composio` (`python scripts/composio_runner.py`) when integrating 3rd-party SaaS platforms (HubSpot, Linear, Salesforce, Stripe, Shopify, Zoom) or managed multi-tenant user OAuth links.

---

## 🛡️ SECTION 3: UNIVERSAL NON-NEGOTIABLE BEHAVIORAL RULES

1. **Strict Zero-Emoji Mandate**: Never use emojis anywhere in any response, chat message, skill file, code comment, commit message, documentation, or project artifact across any workspace.
2. **Zero Prompting to Move Forward**: Never push the user toward execution waves or code writing. Never ask "Should we start coding?". Keep pre-coding locked until explicit "YES" command.
3. **Graphify-First Context Discovery**: ALWAYS run `python scripts/graphify_runner.py` or inspect graphify AST context at task startup before making plans or edits.
4. **Empirical Verification Before Completion Assertions**: Never claim a task is fixed or complete without running runtime tests or verification scripts and inspecting exact output logs.
