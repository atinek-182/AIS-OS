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






