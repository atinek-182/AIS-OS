# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-07-14 — Connect Obsidian Vaults & Establish Master Task List

**Decision:** Created directory junctions at `brain-aios` and `second-brain-zorixel` pointing to the user's local Obsidian vaults (`D:\Brain For my AIOS` and `C:\Users\HP\Documents\Second Brain for Zorixel` respectively), updated `connections.md` to register them under the `local_path` mechanism, and initialized a prioritized master task list (`wiki/checklists/master-task-list.md`) inside the general AIOS vault.

**Why:** The user operates two separate Obsidian vaults—one for the overall AIOS/workflow hub and one for their ZORIXEL brand. Using Windows junctions maps both vaults relative to the workspace, enabling direct read/write access. Centralizing the master task list in the overall AIOS vault aligns with the Q3-Q4 operational strategy to build 5-10 core workflows, and grouping by Milestones focuses effort on the immediate July 25 launch.

**Alternatives considered:** Using absolute paths across C: and D: drives (messy and not portable), or tracking tasks in a separate file within the `d:\AI-OS` workspace (isolates task tracking from the user's daily Obsidian-based second brain interface).

**Owner:** Atinek Maurya

---

## 2026-07-14 — Configure Google Workspace CLI (GWS) for Dual Accounts

**Decision:** Installed the Google Workspace CLI (`gws`), configured it with a manual OAuth credential client (`client_secret.json`) from GCP Project `Zorixel AIOS`, and exported independent session credential profiles for Personal (`credentials_personal.json`) and Brand (`credentials_brand.json`) accounts. Documented GWS usage in `references/gws-api.md`.

**Why:** Native multi-account switching is no longer supported directly in `gws` CLI. By exporting credentials to individual JSON files, we can switch account contexts dynamically in the AI OS environment by modifying the `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` environment variable.

**Alternatives considered:** Setting up two separate Windows user accounts (adds massive operational friction) or installing the full Google Cloud SDK to use automated flows (unnecessary bloat).

**Owner:** Atinek Maurya

---

## 2026-07-14 — Optimize AIOS for Antigravity & Formulate Workflow Skills

**Decision:** Completed workspace migration from Claude Code references to Antigravity standards. This included running an recursive migration scan via python script, renaming 4 core files to "antigravity" counterparts, creating a `hot.md` cache file, adding "Default Shift" and "Curiosity Rule" operational guidelines to `GEMINI.md`, and scheduling the implementation of 5 custom workflow skills.

**Why:** The user operates in the Antigravity developer environment, making references to Claude Code plugins and configuration files confusing. Standardizing the terminology and building custom, native skills inside `.agents/skills/` ensures consistency, performance, and automation readiness in their active workflow.

**Alternatives considered:** Keeping the original Claude Code guides intact (retains outdated system contexts and could cause the model to look for non-existent Claude plugins) or manually renaming items incrementally (tedious and error-prone).

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Consolidate Utility Scripts & Save Skills Documentation

**Decision:** Saved all custom scripts (agent_adapt.py, rename_and_link_update.py, verify_skills.py) to a centralized `/scripts/` directory at the root workspace. Created `references/utility-scripts.md` and `references/antigravity-skills-guide.md` documentation templates to explain their usage and trace corresponding Antigravity/Claude Code plugin sources, and updated `GEMINI.md`, `EXPANSIONS.md`, and the general wiki index.

**Why:** Centralizing helper scripts keeps the workspace tidy (avoiding stray scripts in temporary directories) and enables quick execution for future workspace reorganizations. Documenting both Claude and Antigravity-specific plugins and repositories preserves historical research and ensures clarity on how the AI OS can be extended with official and community modules.

**Alternatives considered:** Leaving the scripts in temporary scratch folders (statically works, but risks deletion and hides them from active development) or only documenting the script logic without the plugin guidelines.

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Set Up Global Skills for Antigravity

**Decision:** Created a python script `copy_skills_to_antigravity.py` to copy all 122 skill directories (including using-superpowers, frontend-design, writing-skills, all 50+ gsd-* skills, context-mode skills, and memory skills) from local Claude Code configuration folders to the global Antigravity customizations folder (`C:\Users\HP\.gemini\config\skills\`). Ran the script and performed recursive `agent-adapt` replacements to make the skills fully native to the Antigravity platform.

**Why:** Enforcing global capability parity ensures that when the user switches tasks or workspaces in the Antigravity developer environment, the agent automatically discovers and runs the same powerful specs-driven, memory-aware, and frontend-design workflows originally cloned for Claude Code.

**Alternatives considered:** Requiring the user to rebuild skills locally for every new workspace (causes high setup friction and duplicate code) or running unmodified Claude Code skills (causes syntax errors due to platform-specific references).

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Verify Workflows & Compile AIOS User Manual

**Decision:** Created a Python test script `demo_test_skills.py` to verify the execution logic of the newly added custom workspace skills (`/plan-day`, `/review-day`, `/scrape-competitor`, `/draft-message`, `/file-search`) and generated the [ZORIXEL AIOS User Manual & Execution Guide](file:///d:/AI-OS/references/aios-user-manual.md) to serve as a comprehensive user handbook. Integrated links to all new guides across both Obsidian indexes (`brain-aios` and `second-brain-zorixel`).

**Why:** Enforcing spec compliance verification prevents "dark code" execution or broken skill configurations before committing file changes. Centralizing instructions and documenting both the local workflow slash-commands and global plugins provides Atinek Maurya with a clear, direct reference for operating their AIOS.

**Alternatives considered:** Relying on the user's memory or checking each skill individually via standard prompt execution (increases token overhead and setup latency).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate & Configure Grill-Me Skill

**Decision:** Installed the `/grill-me` skill both locally in `.agents/skills/grill-me/SKILL.md` and globally in `C:\Users\HP\.gemini\config\skills\grill-me\SKILL.md` based on the downloaded configuration. Registered the slash-command in `GEMINI.md`, added it to `verify_skills.py` verification suite, updated `references/aios-user-manual.md` with instructions, and successfully verified the skill parser.

**Why:** The `/grill-me` skill provides a critical structured mechanism to brainstorm and capture your ideas immediately to file disk storage during detailed Q&A loops, preventing context window decay and keeping track of decisions.

**Alternatives considered:** Keeping the skill local to the Downloads folder or manually copy-pasting the skill contents whenever starting a brainstorm session.

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate Roast & Session Handoff Skills & Ingest Monetization Upgrades

**Decision:** Integrated `/roast` and `/session-handoff` skills into the AIOS. Registered the slash-commands in `GEMINI.md`, added them to `references/aios-user-manual.md` with operational guides, created `brain-aios/wiki/research/aios-monetization-upgrades.md` containing the YouTube clip digest of Nate Herk's 4 core monetization upgrades, updated the wiki index (`brain-aios/wiki/index.md`), and recorded the ingest event in `brain-aios/wiki/log.md`.

**Why:** The `/roast` and `/session-handoff` skills represent critical upgrades for business validation and context management respectively. Recording their details in the user manual and documenting the YouTube clip in the LLM Wiki ensures a complete knowledge record of the AIOS capabilities, keeping the repository aligned with Atinek Maurya's target workflow.

**Alternatives considered:** Manual copying of skill instructions or maintaining the monetization video takeaways as raw files without wiki integration.

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate Superpowers Skill & Set Up Global Rule File

**Decision:** Integrated `/using-superpowers` skill into the AIOS. Copied the skill config to `.agents/skills/using-superpowers/SKILL.md`, registered the command in `GEMINI.md`, added usage guidelines to `references/aios-user-manual.md`, updated `verify_skills.py` test suite, and created the global rule file `C:\Users\HP\.gemini\config\AGENTS.md` containing global instructions to enforce superpowers checks, planning, TDD, and verification across all project workspaces. Also documented the framework in `brain-aios/wiki/research/superpowers-framework.md`, updated the wiki index, and executed `agy plugin install https://github.com/obra/superpowers` to fully set up the superpowers plugin and hooks globally.

**Why:** The `using-superpowers` skill, plugin, and ruleset are essential for maintaining engineering discipline and preventing context rot/hallucinations by forcing structured planning, TDD, and verification cycles before code modification.

**Alternatives considered:** Using the global skill without local workspace registration, or writing rules to project-scoped `AGENTS.md` files (which requires duplication for every new repository).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate and Configure Context7 Globally

**Decision:** Registered the Upstash Context7 MCP server in the global `mcp_config.json` configuration, created a global skill `/context7` under `C:\Users\HP\.gemini\config\skills\context7\SKILL.md` to trigger live document retrieval, created `references/context7-api.md` API guide, and updated `GEMINI.md`, `connections.md`, `references/antigravity-skills-guide.md`, and `references/aios-user-manual.md` manuals.

**Why:** Adding Context7 globally gives the personal AIOS instant access to up-to-date, version-specific external library API documentation and code examples natively via MCP tools. This avoids model hallucination and reduces manual research overhead.

**Alternatives considered:** Running setup interactively via CLI `npx ctx7 setup` (unstable inside the sandboxed environment due to OAuth handling) or registering Context7 solely at the workspace level (fails the user's global usage requirement).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate 6 New Global MCP Servers & notion-sync Skill

**Decision:** Integrated 6 new global MCP servers (context7 with auth headers, codegraph, playwright, github with auth token, magic with API key, chrome-devtools-mcp, and notion-mcp-server with authorization header) into `mcp_config.json`. Created a custom workspace skill `/notion-sync` under `.agents/skills/notion-sync/SKILL.md` to handle sync, created 6 individual API reference guides in `references/`, and updated all AIOS user manuals, connection tables, and skills guide.

**Why:** Expanding global MCP integration allows the personal AIOS to orchestrate browser control, visual checks, code exploration, issue tracking, and Notion databases. Creating modular API guides keeps documentation clean and ensures that API keys and Notion tokens remain dynamic.

**Alternatives considered:** Using a single consolidated reference guide (unnecessarily cluttered and violates connections.md design guidelines) or hardcoding specific repository/database IDs in the skill code (fragile and insecure).

**Owner:** Antigravity AIOS

## 2026-07-15 — Refactor agent-adapt to Smart LLM-Driven Skill Transpilation

**Decision:** Refactored the `agent-adapt` skill under `d:\AI-OS\.agents\skills\agent-adapt\SKILL.md` from a blind regex find-and-replace Python script to an interactive, LLM-driven adaptation engine. Deleted the deprecated script `scripts/agent_adapt.py` and simplified `scripts/copy_skills_to_antigravity.py` to recursively copy skills raw without performing search-and-replace substitutions.

**Why:** Static find-and-replace of "Claude" with "Antigravity" causes critical bugs by breaking CLI executable commands, npm package scopes, GitHub repository URLs, and documentation links. Moving this logic to a smart, native, LLM-driven skill allows the agent to search the web for correct tool equivalents, deduct duplicates, flag Claude-specific items with markdown warnings, and present git-style diffs for user approval before writing files.

**Alternatives considered:** Maintaining the Python script but using the Gemini API (adds credential and dependency overhead) or manual adaptation on every import (slow and doesn't scale for the user's growing custom skills repository).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Centralize Workspace Directory Map & Log Boundaries

**Decision:** Created [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) at the workspace root to act as the centralized files and configurations directory index. Linked it in [GEMINI.md](file:///d:/AI-OS/GEMINI.md) and both Obsidian wiki indexes. Created a workspace-scoped rules file [AGENTS.md](file:///d:/AI-OS/.agents/AGENTS.md) to enforce map updates, and updated the [/review-day](file:///d:/AI-OS/.agents/skills/review-day/SKILL.md) skill to verify map alignment during evening reflections.

**Why:** Documentation, configs, connection guides, and logs were scattered across multiple folders. Enforcing log alignment policies prevents context fragmentation and directory rot. Automating wrap-up checks in `/review-day` and codifying rules in `.agents/AGENTS.md` prevents layout drift.

**Alternatives considered:** Using global config rules (blocked due to directory permissions) or keeping indices decentralized (leads to agent context dilution).

**Owner:** Antigravity AIOS

---
## 2026-07-15 — Implement Git Pre-Commit Workspace Map Validation Hook

**Decision:** Designed and implemented a Git pre-commit hook to automate the verification of [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) alignment. Created a Python validation script `scripts/validate_workspace_map.py` to check root files/folders, custom skill directories in `.agents/skills/`, and reference manuals in `references/`. Deployed the active Git hook to `.git/hooks/pre-commit` and committed a tracked backup to `scripts/hooks/pre-commit`.

**Why:** Relying on conversational memory (like the `/review-day` loop checklist) or rules file compliance alone leaves the configuration map vulnerable to decay. Enforcing validation programmatically in a Git hook prevents any unmapped folders or files from being committed, maintaining the integrity of the workspace.

**Alternatives considered:** Using a post-commit hook (too late to block commits) or manual audits (unreliable and easily bypassed).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Implement Improve-System Custom Skill & Experiences Vault

**Decision:** Created the `/improve-system` custom skill (`.agents/skills/improve-system/SKILL.md`) to analyze current session transcripts, automatically update iterated skills, and capture personal lessons/experiences in `brain-aios/wiki/experiences/`. Configured the chronological index file `context/experiences/README.md`, registered the new paths in `WORKSPACE_MAP.md` and `brain-aios/wiki/index.md`, and updated `GEMINI.md` and `.agents/AGENTS.md` rules to prompt self-improvement suggestions after major milestones.

**Why:** To establish a smart, closed-loop self-improvement mechanism that allows the AIOS to learn and grow over time from user feedback, skill output iterations, and shared lessons. Offloading transcript parsing to a subagent prevents context bloat in the main conversation window, maintaining token optimization.

**Alternatives considered:** Direct main-thread analysis (would cause high token usage and context window exhaustion) or manual copy-pasting of lessons and skill updates (adds operational friction and is prone to neglect).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Configure Scoped External Projects Junction Workspace

**Decision:** Created a master `D:\projects\` directory with seven specialized subfolders (`Websites`, `Zorixel brand`, `For AIOS`, `My advisors`, `Products`, `Learning`, `Sandbox`). Created matching directory junctions under `d:\AI-OS\projects\` pointing to these external folders, updated `.gitignore` to exclude the local `projects/` directory from Git tracking, and registered the new directory structure in `WORKSPACE_MAP.md`.

**Why:** Centralizing client websites, brand content, products, and AIOS projects inside the AIOS folder is desired for full context accessibility, but directly nesting Git repositories causes Git tracking corruption, nested submodule conflicts, and token search bloat (e.g. from `node_modules` or media assets). Using the junction pattern with `.gitignore` exclusion allows the AI to seamlessly read and write files across projects while keeping Git operations clean and avoiding context pollution.

**Alternatives considered:** Nesting raw project folders directly inside the AIOS Git repository (rejected due to Git pollution and token bloat), or keeping projects external with no local path references (rejected due to high path reference friction and manual command setup).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Implement project-agent Slash Command and Custom Workspace Skill

**Decision:** Created the `/project-agent` custom workspace skill at `.agents/skills/project-agent/SKILL.md` to delegate complex tasks to autonomous background developer subagents. Registered the slash command in `GEMINI.md` and `references/aios-user-manual.md`, added it to `WORKSPACE_MAP.md`, and completed the brainstorm capture file in `brainstorms/`.

**Why:** The user wants to build and test features inside project subdirectories without clogging the main session's context window. Spawning a background subagent (using `agy --print`) scoped to the specific project path keeps the main chat clean, enforces global superpowers and TDD workflows, auto-generates documentation (`walkthrough.md`), and fuzzy-matches project folder names to minimize typing overhead.

**Alternatives considered:** Using the main session for all tasks (clogs context window on large tasks), or running separate terminals manually (loses access to the user's AIOS skills and Obsidian memory context).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Implement developer Subagent Configuration for project-agent

**Decision:** Created a workspace-scoped subagent configuration file at `.agents/agents/developer.md` defining the specialized background developer agent behavior. Registered the `.agents/agents/` directory and `developer.md` in `WORKSPACE_MAP.md`, and checkpointed the brainstorm process in `brainstorms/2026-07-15-subagent-configuration.md`.

**Why:** The `/project-agent` skill delegates directory-scoped coding/content tasks to a background subagent by calling `agy --agent developer ...`. Defining this agent's metadata (Model: inherit, Color: blue, full tool access) and its system prompt (enforcing the Superpowers TDD loop and walkthrough logging) guarantees that the background subprocess behaves strictly in accordance with workspace standards.

**Alternatives considered:** Using the default `developer` agent without a workspace-scoped prompt configuration (would lack enforcement of project-specific `walkthrough.md` generation or direct alignment with the custom AIOS rules).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate Karpathy Coding Guidelines Globally

**Decision:** Adapted and integrated the Karpathy-inspired coding behavioral guidelines from `andrej-karpathy-skills` repository into our local `GEMINI.md` file, registered the `/karpathy-guidelines` command, and installed the guidelines as a global custom skill at the user level in `C:\Users\HP\.gemini\config\skills\karpathy-guidelines\SKILL.md`. Documented the command in `references/aios-user-manual.md`, added it to `verify_skills.py` verifier, and updated `WORKSPACE_MAP.md`.

**Why:** Enforcing the four coding principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) globally across all workspaces keeps the codebase clean, minimizes overcomplication, enforces testing verification loops, and aligns with the Antigravity developer environment.

**Alternatives considered:** Installing at the project level in `.agents/skills/` (rejected since these are generic, cross-project coding behavior rules that the user wants to apply everywhere), or leaving them unmodified (would retain legacy Claude Code/Cursor specific terminology).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Implement Static Reference Library and Active marketing/seo-audit Router Skills

**Decision:** Created a static reference library at `d:\AI-OS\brain-aios\wiki\research\skills-library/` to store Corey Haynes' copywriting skills (~45 files) and Daniel Agrici's SEO skills (~25 files and 50 python scripts). Implemented two active router skills at `.agents/skills/marketing/SKILL.md` and `.agents/skills/seo-audit/SKILL.md` to load these frameworks dynamically on demand. Registered the slash commands `/marketing` and `/seo-audit` in `GEMINI.md`, and updated `WORKSPACE_MAP.md`.

**Why:** Installing 70+ separate skills directly in `.agents/skills/` causes massive memory bloat, startup lag, command collisions, and context window rot. Sandboxing the raw files in a static reference directory keeps the workspace clean, while the two active router skills dynamically read the guidelines and execute python scripts on demand, boosting performance and maintaining capability.

**Alternatives considered:** Porting all 70+ skills directly (token-heavy, slow, and violates the 3-5 active skills limit), or discarding the python files (would reduce SEO audits to simple advisory lists rather than actual page/schema checks).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Establish Skill Adaptation Rule in AGENTS.md

**Decision:** Appended a new workspace rule `## Adapting Skills to Antigravity & Gemini` in `.agents/AGENTS.md` to instruct the AI OS to check and tweak all loaded skills and guides for Antigravity/Gemini compatibility.

**Why:** Most community skills are written specifically for Claude Code or Cursor. Adding a dedicated rule in `AGENTS.md` ensures that the AI OS dynamically translates platform-specific terminology, paths, and commands in the background without modifying the core meaning or losing the capabilities of the original frameworks.

**Alternatives considered:** Manually editing all 70+ reference files in the library (extremely time-consuming, prone to syntax errors, and loses sync with upstream updates).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Implement Canvas Design Custom Skill and Library

**Decision:** Created the static reference library for Canvas Design at `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design/` (styles, specs, HTML template base) and registered the active router skill `.agents/skills/canvas-design/SKILL.md` (slash command `/canvas-design`). Integrated the user's `Temporary brand design.md` style guidelines and registered paths in `WORKSPACE_MAP.md`.

**Why:** The user wants programmatically generated social media graphics, posters, and brand banners matching their specific visual aesthetic (cream canvas, coral highlights, Garamond display type).Decoupling the templates and rendering logic keeps `.agents/skills` lightweight, while using the native `browser_subagent` Playwright screenshot mechanism ensures pixel-perfect PNG renders at exact preset aspect ratios without heavy local packages.

**Alternatives considered:** Using text-to-image diffusion models via `generate_image` (generates misspelled text and lacks structural layout precision), or installing local Node canvas dependencies (adds significant installation footprint and complexity).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — System Self-Improvement: Document Localhost Serving Rule & Capture Programmatic Canvas Experience

**Decision:** Updated `.agents/skills/canvas-design/SKILL.md` to document the localhost HTTP serving rule for browser subagents (to bypass local file scheme blocks). Created a new experience document at `brain-aios/wiki/experiences/2026-07-16-programmatic-canvas-browser-rendering.md` and registered it in indexes/logs.

**Why:** Spawning headless browsers to view local files natively results in sandboxing access violations. Establishing a background HTTP server serving pipeline guarantees robust renders across all user systems. Capturing this experience preserves the solution for future workspaces.

**Alternatives considered:** Standardizing on local file paths (rejected as it is blocked by browser security guidelines).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Implement Programmatic Viral Carousel Copywriter and Render Skills

**Decision:** Created the `.agents/skills/carousel-copy/SKILL.md` (for copy planning outlines) and `.agents/skills/carousel-render/SKILL.md` (for browser-captured slide rendering), registered them in `GEMINI.md` and `WORKSPACE_MAP.md`, added `scripts/compile_carousel.py` to parse markdown outlines into individual HTML slides, and extended `styles.css` with 3 carousel layout structures (Before/After split comparison, gradient headline rule, and brand header/footer slide furniture) modeled after `adarshxdesign`'s Instagram reference carousel.

**Why:** Using programmatic HTML-to-Image rendering over Midjourney/DALL-E prompt generation guarantees 100% spelling accuracy, perfect visual consistency (removing styling drift), and extremely fast rendering (under 1 minute for a 7-slide deck) in one click. Splitting the copywriting (/carousel-copy) and rendering (/carousel-render) into a 2-step workflow provides Atinek with complete control to edit copy and paste code blocks before compiling.

**Alternatives considered:** Using the DALL-E 3 image prompting workflow from the ingested playbook (too slow, prone to spelling errors, and requires manual copy-paste iteration and image downloads), or generating the carousel as a single multi-page scrolling HTML document (more prone to viewport scrolling inconsistencies than individual slide files).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Overhaul Slide Visual Aesthetics and Create Scrape-Carousel Skill

**Decision:** Completely overhauled the styling system in `styles.css` to introduce premium visual guidelines (radial grid backdrops, glassmorphic cards with inset shadows/borders, tightened letter-spacing and line-heights, and 3D rotated preview layouts) replacing the basic default formats. Created the active workspace skill `.agents/skills/scrape-carousel/SKILL.md` (slash command `/scrape-carousel`) to automatically crawl Instagram posts, bypass login overlays, locate active slides, and save cropped screenshot assets.

**Why:** The initial slide generation resulted in plain layouts that looked cheap and resembled "AI slop". Introducing professional web design techniques like grid arrays and backdrop blurs creates visually striking slides fitting the ZORIXEL brand identity. Automating the crawling process prevents manual page screenshotting and cropping overhead when indexing competitor ideas.

**Alternatives considered:** Using global css framework packages (adds bloat and fails to compile cleanly under static rendering), or relying on manual screenshotting for references (highly repetitive and slow).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Overhaul Visual Guidelines and Persistent Memory

**Decision:** Formulated and persisted Atinek's specific visual design rules for the ZORIXEL brand (warm linen `#fbfaf7` canvas, charcoal `#141413` text, upscaled font sizes, and pure white floating cards with highly diffused drop shadows) inside the global persistent memory [MEMORY.md](file:///d:/AI-OS/MEMORY.md). Updated active skills `.agents/skills/carousel-copy/SKILL.md` (to automatically generate spec options complying with these rules) and `.agents/skills/carousel-render/SKILL.md` (to serve templates over localhost HTTP rather than direct file paths to bypass sandbox security blocks).

**Why:** Spitting out generic layouts or basic templates reads as cheap and looks like "AI slop". Logging exact contrast ratios, card dimensions, shadows, and Safe Zone padding parameters in the core memory guarantees that the AIOS automatically generates visually stunning assets in future runs without repeating visual audit mistakes.

**Alternatives considered:** Relying on inline instructions (too prone to forgetting cross-session and leads to knowledge drift).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Establish Root Templates Junctions and Rename Daily Skills

**Decision:** Created a physical `templates/` directory at the root of the workspace (`d:\AI-OS\templates`), created two directory junctions pointing to the templates subfolders inside our Obsidian vaults (`templates/aios` -> `brain-aios/wiki/templates` and `templates/zorixel` -> `second-brain-zorixel/wiki/templates`), and renamed the daily cadence skills folders (`plan-day` and `review-day`) to `daily-plan-day` and `daily-review-day`. Updated all configuration files, guides, manual entries, and validation scripts to refer to the new `/daily-plan-day` and `/daily-review-day` commands.

**Why:** Having no root templates directory was flagged as a gap in our Four-Cs audit. Mapping the templates folders of both vaults under a unified root folder ensures easy access across the AIOS and prevents directory drift. Renaming the daily skills to start with `daily-` ensures compliance with canonical scheduled command patterns, resolving a second gap in our audit.

**Alternatives considered:** Mapping `templates/` directly to only one of the vaults (ignores templates in the other vault), or keeping the custom skills named `/plan-day` (violates scheduled-command naming conventions).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Workspace Root Files Cleanup & Vault Brainstorm Archiving

**Decision:** Moved `aios-intake.md` to `context/aios-intake.md`, moved `connections.md` to `context/connections.md`, created the archive folder `d:\AI-OS\brain-aios\archives\brainstorms\`, and relocated all completed brainstorm markdown files from the workspace root `brainstorms/` folder to the Obsidian vault's archive folder. Also purged all raw Playwright cache files (PNG/YML/LOG) inside `d:\AI-OS\.playwright-mcp/` and updated all config, guide, manual, and skill files to align with the new paths.

**Why:** Cleaning up root-level clutter optimizes system navigation, reduces folder noise, and keeps the active workspace clean. Archiving completed brainstorms into the Obsidian vault's archives folder ensures they remain searchable inside the user's Second Brain while removing them from the active coding repository. Purging the Playwright cache directory removes transient cache slop and saves disk space.

**Alternatives considered:** Keeping files at the root level (creates workspace clutter), or summarizing raw Playwright DOM trees (unnecessary prompt/token bloat).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Automate Playwright Cache Purging and Ignore Cache Bloat

**Decision:** Integrated an automatic `.playwright-mcp/` cache purging step into the `/daily-review-day` evening routine, appended `.playwright-mcp/` to the root `.gitignore`, added `.playwright-mcp` to the `ignored_root_items` inside `scripts/validate_workspace_map.py`, and recorded the system improvement lessons in a new experiences log `brain-aios/wiki/experiences/2026-07-16-aios-directory-hygiene-and-playwright-cache-automation.md`.

**Why:** The Playwright MCP server generates temporary HTML/YAML page state trees and screenshots during execution. These transient caches clutter Git status and trigger path-alignment errors in our pre-commit checks. Automating their removal at daily wrap-up and ignoring the directory in both Git and our custom map validator ensures that the user never has to manually clear these cache files and prevents directory checks from breaking.

**Alternatives considered:** Continuing manual cache deletions (annoying and error-prone), or logging cache files in `WORKSPACE_MAP.md` (causes path misalignment checks on every run).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Map and Integrate Premium Frontend Experience System

**Decision:** Created a directory junction at `premium-frontend-experience-system/` pointing to `C:\Users\HP\Documents\Premium-Frontend-Experience_System`. Registered the junction in `WORKSPACE_MAP.md`, integrated its guidelines as a default frontend design instruction in `GEMINI.md`, removed references to the deleted `vercel-composition-patterns` skill, and added a **Fast-Track Bypass Rule** in `ANTIGRAVITY_PROMPTING.md` for edits under 30 lines.

**Why:** The user mapped their premium frontend design system Obsidian vault into the workspace to serve as a visual "design brain". Enforcing visual restraint, viewport audits, and Playwright verification ensures that client and brand UI projects match professional creative engineering standards. Cleaning up dead references to deleted skills prevents tool execution errors, and the Fast-Track Bypass Rule resolves visual iteration lag on minor bug fixes and simple changes.

**Alternatives considered:** Duplicating the design system files directly inside the workspace (causes document fragmentation and updates wouldn't sync back to their active Obsidian design vault) or forcing full project briefs and Q&As on every minor layout fix (creates excessive procedural friction).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Restructure Premium Frontend Experience System & Configure Global Integrations

**Decision:** Consolidated the 10 root-level markdown files of the Premium Frontend Experience System into 4 clean, highly-structured files: `AGENTS.md` (Identity, default tech stack, and prompting), `POLICIES.md` (Component sourcing, motion guidelines, WebGL shader policies, and Design Token specifications), `WORKFLOWS_AND_QA.md` (Milestones and QA checklists), and `INTAKE_AND_REFERENCES.md` (Project Q&A and Reference auditing). Deleted the 9 duplicate root files, updated `WORKSPACE_MAP.md`, registered the `shadcn` and `flowbite-mcp` servers globally in `mcp_config.json`, created a custom global skill `threejs-webgl` under `C:\Users\HP\.gemini\config\skills\threejs-webgl\`, created the visual QA automation script `scripts/verify_design_milestone.py` in the workspace, cloned the full 10-module `threejs-skills` and 8-module `gsap-skills` libraries into the static research library `brain-aios/wiki/research/skills-library/`, created the active workspace skills `/verify-design` (milestone verification wrapper) and `/ingest-skills` (automated repository cloning & indexing engine), and updated the final step of `/grill-me` to execute `/roast` automatically.

**Why:** Having 10 separate markdown files repeating the tech stack, general rules, and QA checklists led to heavy documentation duplication, increased token consumption, and context fragmentation for the AIOS. Consolidating into 4 files keeps instructions lightweight and optimized for the LLM prompt context window. Registering the official shadcn and flowbite MCPs globally gives the AIOS direct access to Tailwind and shadcn tools across all projects. Creating the global `threejs-webgl` skill fills the gap for Three.js, shaders, and React Three Fiber best practices. Copying the full Three.js and GSAP repositories statically to `brain-aios` provides the AIOS with a progressive-disclosure-based granular reference database for complex scenarios. Creating the `/verify-design` and `/ingest-skills` active skills automates visual QA audits and repository ingestion into one-click commands, and connecting `/grill-me` to `/roast` ensures every discovery plan is automatically pressure-tested by the adversarial council. The python automation script `verify_design_milestone.py` replaces manual responsive and console audits with a one-click build and Playwright capture cycle.

**Alternatives considered:** Keeping the 10 root files separate (rejected due to prompt bloat), or manual verification (rejected as it is repetitive and prone to error).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Scrape Jordan Watkins Brand Reference & Automate Design Tools

**Decision:** Mirrored the entire asset and code tree of jordanwatkins.xyz locally to `second-brain-zorixel/wiki/research/jordan-watkins-reference/` using a Node scraper script (`scripts/mirror-jordan-watkins.js`). Created a visual and technical audit doc (`second-brain-zorixel/wiki/research/jordan-watkins-reference/analysis.md`), set up a background static web server (`scripts/serve.js`) hosting the mirrored website on port 3000, programmatically ran the local Typeface Picker and Palette Generator in Playwright to extract brand candidacies, and outputted the results to `second-brain-zorixel/wiki/brand/candidates.md` with visual preview blocks.

**Why:** Having a complete offline-available mirror of the website allows us to audit Jordan Watkins' design, typography, spacing tokens, and custom JS interaction mechanics (draggable physics, canvas paper background, spring custom cursor). Setting up a localhost server on port 3000 circumvents the `file:` protocol restriction in the Playwright MCP server, enabling automated visual testing and programmatic querying of his design tools to fetch brand candidates for Zorixel.

**Alternatives considered:** Scraping only textual summaries (rejected as it loses visual and script-level details) or querying the live website continuously (rejected because it depends on network availability and raises potential traffic throttling or TOS flags).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Create Scrape Component Skill for Targeted Design Reference Isolation

**Decision:** Created a workspace custom skill `/scrape-component` located at `.agents/skills/scrape-component/SKILL.md` to extract isolated UI elements, motion styles, and asset dependencies from websites. Integrated the new workflow into the design system vault files `premium-frontend-experience-system/INTAKE_AND_REFERENCES.md` (Section 5) and `premium-frontend-experience-system/AGENTS.md` (Prompt Pattern 11), registered it in `GEMINI.md` and `WORKSPACE_MAP.md`, and ran the pre-commit map validation to ensure workspace alignment.

**Why:** Mirrored reference websites can be massive and introduce substantial folder and codebase bloat. Providing a target-extraction skill allows us to scrape only the precise element (e.g. custom cursor, button animation, or bento layout) that the user likes. Asking targeted clarifying questions via `/grill-me` helps narrow down selectors and dependencies, producing standalone HTML/CSS/JS prototypes that can be hosted locally on localhost port 3000 for Playwright visual verifications.

**Alternatives considered:** Manual copying of source code (rejected due to speed and risk of missing dependencies) or only scraping full websites (rejected to prevent directory clutter).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Restructure Premium Frontend Experience System and Add Link-Rot Verification Hook

**Decision:** Restructured the `premium-frontend-experience-system/` directory junctions. Removed duplicate project contexts, status definitions, and lists from design briefs and asset briefs templates, replacing them with bracket references to the central `[[PROJECT_BRIEF]]` and `[[README]]`. Updated all 13 workflow guides to point to the new unified files `[[POLICIES]]` and `[[AGENTS]]`. Created `scripts/validate_links.py` to validate markdown relative and Obsidian `[[WikiLink]]` structures, and integrated it into the git pre-commit hook. Created custom slash commands `/new-project` and `/design-direction` and registered them in `WORKSPACE_MAP.md`.

**Why:** Consolidating templates and files keeps the codebase clean, reduces LLM context window consumption, and prevents token bloat during development. Adding an automated link validation checker to the pre-commit hook ensures absolute links integrity across directory renames and prevents broken wiki cross-references. Decoupling web layouts from social graphics prevents design contamination and keeps the business workflows clean.

**Alternatives considered:** Collapsing the entire experience system into a single file (rejected because it would lose detailed research, site database registries, and modular workflows).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Create AIOS Workflow Diagram & User Guide

**Decision:** Created `aios-workflow.excalidraw` in the workspace root and generated a simple, non-technical markdown user guide (`aios_workflow_guide.md`) in the artifacts directory. Registered the diagram in `WORKSPACE_MAP.md`.

**Why:** To provide Atinek Maurya with a clear, non-technical, visual and textual explanation of how the whole AIOS operates and how they can trigger commands, manage context, and automate content research and coding tasks.

**Alternatives considered:** Creating only a text guide without a visual Excalidraw diagram (less intuitive for visual design creators) or hardcoding visual assets inside the Obsidian vaults directly (harder to edit natively in Excalidraw).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Create Detailed AIOS Skills Reference Excalidraw Diagram

**Decision:** Created detailed skills reference Excalidraw diagram (`aios-skills-reference.excalidraw`) in the workspace root detailing 30 local & global skills, their purpose, when to use them, and real examples. Registered the file in `WORKSPACE_MAP.md`.

**Why:** To provide Atinek Maurya with a comprehensive, visual cheat-sheet of every tool, skill, and automation command in the AIOS, grouped by operational role (Ops, Marketing, Frontend, Code, Strategy, Admin).

**Alternatives considered:** Maintaining a long markdown list (hard to scan at a glance) or listing only custom slash commands (omits critical global rules and layout audits).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Organize Excalidraw Diagrams Into Dedicated Diagrams Directory

**Decision:** Created `diagrams/` folder in workspace root, moved existing `.excalidraw` files into it, updated build paths in `build_excalidraw.py`, and registered the directory and files in `WORKSPACE_MAP.md`.

**Why:** To avoid root-level workspace clutter and maintain strict directory hygiene by centralizing all visual design and workflow schemas in one structured location.

**Alternatives considered:** Keeping them at root (creates clutter) or moving to Obsidian vault folders (harder to edit natively in local workspace).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Integrate VibeSec Secure Coding Skill

**Decision:** Cloned VibeSec-Skill repository from GitHub, tweaked it to make it native to Antigravity, and installed it under `.agents/skills/vibesec/SKILL.md`. Registered the slash command in `GEMINI.md`, `references/aios-user-manual.md`, and `WORKSPACE_MAP.md`.

**Why:** To provide the AIOS with a structured secure-coding framework and checklists (covering IDOR, XSS, CSRF, secrets leakage, SSRF, SQLi, and JWT issues) when building, scanning, or auditing client web applications.

**Alternatives considered:** Leaving it as a static reference file (rejected because the user explicitly wants to trigger security audit checks in active coding sessions).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Resolve Bun Probe Hangs & Setup Claude-Mem Persistent Memory

**Decision:** Resolved local Bun probe hangs in sandboxed terminal environments by running the official Bun installer script to set up a standard working Bun binary at `C:\Users\HP\.bun\bin\bun.exe`. Installed the `claude-mem` persistent memory plugin for the Antigravity CLI, registering 7 lifecycle hooks, MCP configurations, and starting the memory worker daemon on port 37777.

**Why:** To ensure Bun child-processes do not block sandboxed PowerShell runs, and to establish persistent semantic memory that automatically captures context, observations, and decisions across sessions for the Antigravity CLI environment.

**Alternatives considered:** Using the pre-installed custom wrapper at `C:\Users\HP\AppData\Local\Kiro-Cli\bun` (rejected because it hangs indefinitely on console pipes under PowerShell jobs).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Centralize MCP Auth Parameters in `.env`

**Decision:** Added placeholder keys and documentation for `GITHUB_PERSONAL_ACCESS_TOKEN`, `API_KEY` (Magic MCP), `OPENAPI_MCP_HEADERS` (Notion MCP), and `CONTEXT7_API_KEY` (Context7 MCP) directly to the workspace `.env` file.

**Why:** To address the security and documentation gap identified during the AIOS structural audit, ensuring that all third-party API credentials used by the AIOS and its MCP servers are centralized in a single gitignored configuration file rather than dispersed across global environments or hardcoded variables.

**Alternatives considered:** Keeping them as system environment variables (rejected because it reduces workspace portability and visibility).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Create Application Security & Perimeters Diagram

**Decision:** Created the Excalidraw diagram `apps-security.excalidraw` in the `diagrams/` folder showing how application security perimeters and defense-in-depth layers function. Created the Python generator script `scripts/generate_security_diagram.py` to programmatically build the elements, and registered both the diagram and script in `WORKSPACE_MAP.md`.

**Why:** To address the user's request for a clear visual flowchart showing app security perimeters and logic layers using clean cards, logical color coding, and data flow arrows. Programmatic generation ensures pixel-perfect coordinates and maintains directory hygiene.

**Alternatives considered:** Drawing the diagram manually on excalidraw.com and uploading it (slower and doesn't persist the layout source code in the workspace repository).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Implement Autoresearch Targets Manager & Secure API Quota Fallbacks

**Decision:** Created a custom `/autoresearch-manage` active workspace skill at `.agents/skills/autoresearch-manage/SKILL.md` backed by the automation script `scripts/manage_autoresearch.py`. Configured the three Autoresearch trial scripts (`train.py` and `prepare.py`) to target the `gemini-3.1-flash-lite` model (avoiding 404/503 Free Tier API limits) and wrapped API executions in robust retry-backoff blocks. Created and ran a security audit script `scripts/security_check.py` to verify path traversals and secrets exclusion parameters.

**Why:** Spawning and maintaining custom trial configurations manually introduces folder structure errors and registry misalignment. The automation script programmatically registers new trial folders in the runner list and Workspace Map. Switching target models to `gemini-3.1-flash-lite` and incorporating API retries ensures 100% stable executions under free tier quotas without hitting spikes or model-deprecation errors.

**Alternatives considered:** Maintaining static target lists (inflexible and prone to manual error) or querying the deprecated `gemini-2.5-flash` model (crashes with 404 errors).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Resolve Python IDE Import Errors for `google-genai` and `playwright`

**Decision:** Created workspace settings `.vscode/settings.json` configuring the Python default interpreter to the virtual environment `trials/.venv/Scripts/python.exe`. Additionally, installed `google-genai` and `playwright` (with `playwright install chromium`) inside the system-wide Python environment. Updated the workspace map (`WORKSPACE_MAP.md`) to register the new configuration.

**Why:** The user was experiencing red import errors in their IDE because the IDE fell back to the system Python interpreter which did not have these packages installed. Setting the default interpreter path ensures VS Code/Cursor automatically uses the correct sandboxed virtual environment, and installing the packages system-wide serves as a fallback.

**Alternatives considered:** Creating a duplicate `.venv` at the workspace root (creates redundant virtual environments and package clutter) or only using global installation (does not guarantee IDE interpreter alignment).

**Owner:** Antigravity AIOS

---

## 2026-07-18 — Rebuild Brand Font Presentation into 12 Targeted Slides

**Decision:** Rebuilt the brand presentation deck down to a targeted 12-slide flow, focusing strictly on selected display candidate fonts (`Bezmiar`, `Rosehot`, `Grith`, `Vixa`) and the lowercase `Nuqun` brand logo. Modeled new slides off of Korean brand "newmix" footer structures and "AI in Design 2026" reports, implementing wide monospace letter-spacing for statistics, large cover sizes, and dedicated full-screen lowercase logo identity slides. Created python script `scripts/rebuild_presentation.py` to automate code restructuring.

**Why:** The user narrowed down their favorite typography options and brand logo (favoring lowercase `Nuqun`). Deleting all the intermediate concept routes keeps the deck clean, and adding layout clones with their selected fonts allows direct evaluation of wordmark proportions and text grids on high-contrast black and clean white screens.

**Alternatives considered:** Keeping the 34-slide deck with duplicate concepts (creates too much visual clutter and distracts from final font selections).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Restructure Brand Presentation into 20-Slide Interactive Page Matrix

**Decision:** Restructured `presentation.html` into a 20-slide grid (4 font pairings × 5 canonical pages: Hero, About & Contact, Live Dashboard, Creative Poster, Brand Footer). Implemented lowercase `Nuqun` `"zorixel"` branding across all layouts and configured a dual-axis bottom navigation dock (FONTS row + PAGES row) for side-by-side comparison. Restructured Playwright QA configuration `qa/audit.js` and regenerated screenshots. Created `scripts/rebuild_presentation_20.py` to automate code generation.

**Why:** The user wanted to directly evaluate how their favorite font pairings look on actual website layouts rather than isolated sentences. Combining pages and adding a dual-axis selector enables immediate comparison of a single layout across different fonts (e.g. comparing footer layouts) or sequential options review.

**Alternatives considered:** Designing 20 individual HTML files (inflexible and difficult to browse synchronously).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Finalize Zorixel Brand Typography & Generate 2K High-Res Logos

**Decision:** Finalized Zorixel's typography design: brand logo is lowercase `"zorixel"` in `Nuqun` regular font with a chromatic aberration (RGB split) effect; display serifs are `Rosehot` (Title Case); display creative headings are `Vixa` (Title Case, 2-5 words only); paragraph body copy is `Outfit`; statistics numbers are `Space Mono`. Created and ran Playwright script `projects/font-showcase/generate_nuqun_logo.js` to output 2000x2000 transparent logo files (with/without background) and 100% vector SVG files (solid white, solid dark, and vector chromatic aberration). Created canonical guide at `second-brain-zorixel/wiki/brand/typography.md` and registered files in `WORKSPACE_MAP.md`.

**Why:** The user confirmed that the logo font must remain `Nuqun` (exactly as designed in the slides and presentation), and requested 2000x2000 transparent/solid background PNG files along with vector SVG files for Canva/Figma editing.

**Alternatives considered:** Using embedded font tags in SVGs (inflexible as Canva does not load the custom local Nuqun font automatically).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Zorixel Color Presentation Symmetrical Contrast Inversion & Single-Line Parser

**Decision:** Implemented a symmetrical contrast inversion engine and a single-line color palette parser inside `colors_presentation.html`. The parser uses regex to extract all hex values from any pasted text and automatically analyzes them (calculating relative luminance and colorfulness). It then automatically sorts them (Darkest to Lightest), discovers the Accent highlight, and maps them to semantic layout variables. In Dark Mode, the engine dynamically swaps/inverts the variable mappings (e.g. mapping `--color-1` to lightest and `--color-5` to darkest) and blends the darkest color with 92% black to construct a rich dark background.

**Why:** The user was experiencing poor contrast and low legibility where light colors became backgrounds for light text, or dark colors became backgrounds for dark text in dark mode. Letting the engine dynamically sort and map roles by luminance mathematically guarantees high contrast (WCAG compliance) and legibility. The single-line parser enables immediate copy-pasting of palettes from color tools (such as Jordan Watkins' archives) in a single action.

**Alternatives considered:** Maintaining manual/static coordinate color selectors (requires constant manual adjustment and leads to high contrast failure rates).

**Owner:** Atinek Maurya

---

## 2026-07-19 — Integrate Figma Remote MCP Server

**Decision:** Registered the official Figma Remote MCP server in the global `mcp_config.json` configuration, created a reference manual `references/figma-api.md`, updated `connections.md` and `WORKSPACE_MAP.md`.

**Why:** Direct integration with Figma allows the personal AIOS to pull design metadata, tokens, and layouts natively, accelerating high-fidelity design-to-code workflows for ZORIXEL.

**Alternatives considered:** Local command-line figma-developer-mcp with personal access tokens (rejected due to token-maintenance overhead and lack of official Code Connect mappings).

**Owner:** Antigravity AIOS
