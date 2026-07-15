# Project Agent: Brainstorm / Discovery Notes (Option 3 Reshape)
Date: 2026-07-15 · Goal: Design a custom skill `/project-agent` to delegate complex coding tasks to background subagents scoped to specific project junctions.

## Summary / key decisions
* **Core Philosophy (Option 3):** For regular interactive work, the user speaks directly to the main AIOS session, which edits files inside `projects/` junctions. For complex, long-running, or self-contained tasks, the user uses `/project-agent` to delegate the work to a background subagent.
* **Skill Name:** `project-agent`
* **Slash Command:** `/project-agent` (registered in `GEMINI.md`)
* **Trigger:** `/project-agent [project-path] "[task description]"` or when delegating project features.
* **Working Directory Scoping:** The subagent's working directory (`Cwd`) is automatically mapped to `d:\AI-OS\projects\[project-path]`.
* **Lead Developer Role:** The subagent is instructed to act as the autonomous lead developer for that specific project, managing its own implementation plans, tests, and documentation.
* **Auto-Documentation & Testing:** The subagent must run tests and write/update project-specific documentation (e.g. `walkthrough.md` or `README.md`) before finishing.
* **Progress Tracking & Final Summary:** Subagents run as background tasks. On completion, the subagent writes a `walkthrough.md` to the project directory and notifies the main agent, which prints a high-level summary with file links.
* **Full Process Superpowers Integration:** The subagent must follow the global AIOS workflow rules (planning, TDD, and automated verification) using the `superpowers` skill set.
* **Project Directory Auto-Resolution:** The skill resolves the project name fuzzy matching to any subfolder under `projects/` (e.g. `Websites/`, `Zorixel brand/`, etc.), falling back to a selection list if ambiguous.

## Q&A log
### Q1 — Background Progress and Completion Reporting
* **Asked:** Since the subagent runs in the background, how should it report its progress and final results?
* **Captured:**
  * User accepted the **Progress Tracking & Final Summary** behavior.
  * Subagents run asynchronously in the background.
  * Writes a `walkthrough.md` in the project folder upon completion, then triggers a parent notification.
  * Main agent outputs a concise, high-level summary with file links.
* **Flags:** None.

### Q2 — Subagent Capabilities & Superpowers Access
* **Asked:** When the background subagent is running inside the project folder, what process workflows and tools should it use?
* **Captured:**
  * User accepted the **Full Process Superpowers Integration** behavior.
  * Subagents must follow global planning (via `make-plan`/`brainstorming`), TDD, and verification standards.
* **Flags:** None.

### Q3 — Project Directory Path Auto-Resolution
* **Asked:** To minimize typing, how should the skill find the project directory when you invoke it?
* **Captured:**
  * User accepted the **Fuzzy Folder Matching** behavior.
  * Auto-resolves a simple folder name (e.g., `my-site`) to its nested location inside `projects/`.
* **Flags:** None.

## Open flags (pending input)
