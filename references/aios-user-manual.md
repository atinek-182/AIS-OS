# ZORIXEL AIOS User Manual & Execution Guide

Welcome to the central operational manual for your personal AI Operating System (AIOS). This handbook contains instructions on how to trigger and use the custom workspace skills and global plugins set up in your environment.

---

## 🛠️ Part 1: Custom Workspace Skills

These skills reside in `.agents/skills/` and can be triggered in conversation by typing their slash commands or requesting them in natural language.

### 1. `/daily-plan-day` (Daily Morning Loop)
- **Purpose:** Starts your morning. Pulls tasks, priorities, and Google Calendar events, fanning them into a structured hourly schedule.
- **How to Use:**
  - Type `/daily-plan-day` in your terminal.
  - The AIOS will query [priorities.md](file:///d:/AI-OS/context/priorities.md), [master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md), and pull GCal events using the `gws` CLI under your Personal profile.
  - It outputs a tabular daily calendar and asks for confirmation.

### 2. `/daily-review-day` (Daily Evening Loop)
- **Purpose:** Concludes your workday. Prompts you for completed tasks, audits manual repetitive overhead, and updates checklist files.
- **How to Use:**
  - Type `/daily-review-day` at the end of the day.
  - Provide a list of completed items, manual tasks done 3+ times, and estimated time saved.
  - The AIOS will update [master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md) to mark items completed and append notes to the log.

### 3. `/scrape-competitor` (Competitor Scraper Ingest)
- **Purpose:** Automates ingestion of competitor reels/posts research into your Zorixel Second Brain.
- **How to Use:**
  - Type `/scrape-competitor` or `/scrape-competitor [url/topic]`.
  - Open Instagram, run the `rtrvr.ai` extension, and copy the scraped data fields (hook, CTA, transcript, offering).
  - Paste the raw data into the chat. The AIOS parses it, groups it under content pillars, and saves a markdown file to `second-brain-zorixel/wiki/research/`.

### 4. `/draft-message` (On-Brand DM & Email Copywriter)
- **Purpose:** Drafts variations for emails, DMs, or comments matching the ZORIXEL voice guidelines.
- **How to Use:**
  - Type `/draft-message` or `/draft-message [recipient & intent]`.
  - The AIOS reads the voice instructions in `second-brain-zorixel/wiki/brand/personality-and-voice.md` and generates 3 casual, energetic variations.
  - Choose one to copy, or instruct the AIOS to base64-encode and create a draft in Gmail using the `gws` CLI.

### 5. `/file-search` (Multi-Vault Keyword Retrieval)
- **Purpose:** Fast keyword and phrase finder across both Obsidian vaults.
- **How to Use:**
  - Type `/file-search [query]` (e.g. `/file-search GSAP`).
  - The AIOS scans both `brain-aios/` and `second-brain-zorixel/` folders, displaying matching lines with clickable `file:///` links.

### 6. `/agent-adapt` (Claude-to-Antigravity Migration Orchestrator)
- **Purpose:** Standardizes, installs, and cleans up plugins and configuration files to transition the AIOS setup from Claude to native Antigravity rules.
- **How to Use:**
  - Type `/agent-adapt`.
  - The AIOS searches for Antigravity native equivalents of requested plugins, replaces Claude patterns, cleans up local configuration traces, and runs verification tests under the Antigravity developer environment.

### 7. `/grill-me` (Brainstorm & Discovery Interviewer)
- **Purpose:** Stress-tests plans, interviews you relentlessly on designs/concepts, and checkpoints every answer to a brainstorm file so no context is lost.
- **How to Use:**
  - Type `/grill-me` or say "grill me".
  - The AIOS creates a capture file in `brainstorms/` and asks targeted, single questions, providing recommended answers and updating the file on disk after every response.

### 8. `/roast` (Adversarial Idea Council)
- **Purpose:** Stress-tests business ideas or operational plans through five independent adversarial personas and a Judge, outputting a GO / RESHAPE / KILL decision and the cheapest 48-hour validation test.
- **How to Use:**
  - Type `/roast` or `/roast [your business idea]`.
  - Answer 3-4 simple questions from the AIOS regarding the concept, target audience, edge, and runway constraints.
  - The council (Contrarian, Expansionist, Logician, Researcher, Buyer) will evaluate the idea in parallel. The Judge will deliver a finalized recommendation and a 48-hour test guide.

### 9. `/session-handoff` (Zero-Loss Context Preservation)
- **Purpose:** Generates a structured, chat-only context summary of decisions, modifications, and running state, enabling you to `/clear` the context window and resume with a fresh session without starting from scratch.
- **How to Use:**
  - Type `/session-handoff` or say "session handoff" before clearing the session context.
  - Copy the generated summary.
  - Run the `/clear` command to purge the context window.
  - Paste the summary in the fresh session to restore context.

### 10. `/using-superpowers` (Superpowers Workflow Enforcer)
- **Purpose:** Establishes the rule requiring the AIOS to scan the workspace and invoke applicable skills before responding or acting, preventing ad-hoc edits, buggy code, and context rot.
- **How to Use:**
  - Type `/using-superpowers` when starting a conversation or task.
  - The AIOS is required to check for active/relevant skills (like `brainstorming`, `make-plan`, `systematic-debugging`) and invoke them first, stating "Using [skill] to [purpose]".

### 11. `/context7` (Live Documentation Fetcher)
- **Purpose:** Pulls version-specific, live API documentation and code examples from official sources into your workspace prompt to eliminate hallucinations.
- **How to Use:**
  - Type `/context7 [library/query]` or say "use context7 to look up [library]".
  - The AIOS resolves the library ID and retrieves the latest relevant documentation snippet using the Context7 MCP server.

### 12. `/notion-sync` (Notion Database Sync)
- **Purpose:** Synchronizes workspace decisions, checklists, logs, or competitor research details directly to remote Notion pages or databases.
- **How to Use:**
  - Type `/notion-sync` or say "sync my decision log to Notion".
  - The AIOS formats properties (e.g. Title, Date, Content) and updates the remote Notion workspace via MCP.

### 13. `/project-agent` (Scoped Project Developer Agent)
- **Purpose:** Spawns a background developer subagent scoped to a specific project directory under `projects/` (fuzzy-matched from the path name) to build features, run tests, and write code autonomously while keeping the main context clean.
- **How to Use:**
  - Type `/project-agent [project-name] "[task description]"` (e.g., `/project-agent my-site "Create contact page and link it"`).
  - The AIOS resolves the target project folder, sets up credentials, and dispatches an autonomous background developer agent.
  - Upon completion, the subagent writes a `walkthrough.md` to the project folder, and the main session outputs a summary of changes and test results.

### 14. `/karpathy-guidelines` (Coding Guidelines Enforcer)
- **Purpose:** Enforces Karpathy-inspired coding behavioral guidelines (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) to eliminate LLM coding mistakes, overengineering, and bloated or off-target edits.
- **How to Use:**
  - Type `/karpathy-guidelines` or ask the AIOS to apply the Karpathy guidelines to your programming tasks.

### 15. `/agent-reach` (Multi-Platform Internet Capability Engine)
- **Purpose:** Grants single-command internet search, reading, and diagnostic access across 10+ social & web platforms (YouTube subtitles, Bilibili zero-login search, V2EX tech feeds, GitHub, Reddit, RSS, Twitter/X, Exa AI Web Search).
- **How to Use:**
  - Type `/agent-reach` or `/agent-reach doctor` to run health checks on active platform channels.
  - Ask the AIOS to query YouTube transcripts, Bilibili tech trends, Reddit threads, V2EX discussions, or perform semantic web searches.
  - The AIOS will load rules to state assumptions explicitly, push back on overcomplication, ensure changes are strictly focused and surgical, and define verifiable, testable success criteria before modifying code.

### 15. `/verify-design` (Visual & Technical QA Audit)
- **Purpose:** Automatically compiles the project, starts a local server, and launches Playwright to take screenshots at 5 responsive viewports while checking the console log for errors.
- **How to Use:**
  - Type `/verify-design` or `/verify-design [project_dir]`.
  - The AIOS builds the target project, hosts it, and runs the visual audit, printing console warnings and outputting links to the captured layout screenshots.

### 16. `/ingest-skills` (Community Skill Ingester)
- **Purpose:** Automatically clones a community skill or reference manual repository from GitHub, copies its modules into the Obsidian wiki skills library, registers the paths, and indexes them in logs.
- **How to Use:**
  - Type `/ingest-skills [repo_url]`.
  - The AIOS clones the repository to scratch, extracts markdown guides, registers the new directories, indexes the library in `wiki/index.md`, and logs the event.

### 17. `/vibesec` (Secure Coding Guide & Vulnerability Scan Audit)
- **Purpose:** Checks web application codebase against OWASP security standards, validating access controls (IDOR/Mass Assignment), client-side vulnerabilities (XSS/CSRF/Secrets leakage), and server-side request issues (SSRF/XXE/SQLi).
- **How to Use:**
  - Type `/vibesec` when working on web application backends or reviewing code security.
  - The AIOS will audit the active routes, database interactions, and headers against the security checklist and recommend mitigations.

---




## ⚙️ Part 2: Global Plugins

These plugins are installed globally inside your Antigravity environment and run automatically to optimize reasoning, memory, and context.

### 1. Superpowers (`superpowers`)
- **Enforced Rule:** Enforces plan-first, TDD, and code reviews.
- **How it works:** When you assign a development goal, it will automatically prompt you with research findings, request approval on an `implementation_plan.md`, write tests, and run quality checks before declaring task completion.

### 2. Context Mode (`context-mode`)
- **Enforced Rule:** Routes CLI log outputs and Playwright HTML files through an isolated compressing sandbox to avoid token bloat.
- **Commands:**
  - Type `/contextmode:ctx-stats` to view the percentage of tokens saved during the session.
  - Run `/context-mode:ctx-doctor` to run diagnostics on local cache indexes.

### 3. Memory & Decisions (`antigravity-mem`)
- **Enforced Rule:** Intercepts project modifications and logs them locally in a SQLite database. On session startup, it auto-restores files and remembers what was decided.
- **Commands:**
  - Type `/mem-search` to query vector memory of past session actions and fixes.

### 4. Get Shit Done (GSD)
- **Enforced Rule:** Coordinates parallel sub-agents to divide-and-conquer heavy software tasks.
- **Commands:**
  - Type `/gsd-help` to list commands.
  - Run `npx get-shit-done-cc --antigravity` or use `/gsd-progress` to triage active projects.

### 5. Front-End Design (`frontend-design`)
- **Enforced Rule:** Automatically applies styling rules (harmony color palettes, Outfit/Inter fonts, micro-interactions, responsive sizing) so that HTML mockups look premium and custom-coded.

### 6. Context7 Documentation (`context7`)
- **Enforced Rule:** Connects your agent dynamically to Upstash's live documentation database to verify APIs and avoid writing hallucinated/outdated code.
- **Commands:**
  - Automatically queries docs via `resolve-library-id` and `query-docs` MCP tools during coding workflows.
  - Fallback command: `npx ctx7 query <library-id> "<query>"`

### 7. Codegraph (`codegraph`)
- **Enforced Rule:** Automatically queries and maps codebase relations to expose AST context to the agent during code exploration.

### 8. Playwright Browser Driver (`playwright`)
- **Enforced Rule:** Drives a headless Chromium browser instance for visual checks and responsive layout validations.

### 9. GitHub API Access (`github`)
- **Enforced Rule:** Coordinates issue creations, PR submissions, and repository tracking natively via model context.

### 10. Magic Sourcing (`magic`)
- **Enforced Rule:** Instantly queries Tailwind CSS component inspirations and brand logos.

### 11. Chrome DevTools (`chrome-devtools-mcp`)
- **Enforced Rule:** Inspects active browser console logs, executes Lighthouse audits, and captures viewport screenshots.

### 12. Notion Workspace (`notion-mcp-server`)
- **Enforced Rule:** Reads and writes to your remote Notion database boards, calendars, and spreadsheets.



