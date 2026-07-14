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

