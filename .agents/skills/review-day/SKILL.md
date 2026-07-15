---
name: review-day
description: Use when the user wants to review their day, complete an evening reflection, or run the daily wrap-up routine.
---

## What This Skill Does

Automates the evening reflection routine. It gathers completed tasks, audits manual overhead to surface automation candidates, updates the master task list, and captures time saved.

## Steps

1. Ask the user the following reflection questions:
   - *What tasks did we complete today?*
   - *What did you do manually that felt repetitive or took 3+ times?*
   - *How much time was saved by using our AIOS workflows today?*
2. Once the user responds:
   - Update task completions in [master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md) by marking completed items as `[x]`.
   - Append a summary of today's activities to [log.md](file:///d:/AI-OS/brain-aios/wiki/log.md).
   - Audit the workspace files and git status. If any new folders, junctions, or configurations were created today, ensure they are registered in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md).
   - If manual repetitive tasks were identified, write them as candidates in [hot.md](file:///d:/AI-OS/hot.md) or suggest planning them in the next `/level-up` run.

3. Report the daily summary back to the user with a confirmation of task updates.
