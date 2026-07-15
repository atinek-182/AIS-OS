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
