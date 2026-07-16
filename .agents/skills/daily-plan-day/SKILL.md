---
name: daily-plan-day
description: Use when the user wants to plan their day, start a morning routine, or generate a daily schedule.
---

## What This Skill Does

Automates the morning planning routine by pulling calendar events, checking priorities, reading current tasks, and formatting a structured daily schedule.

## Steps

1. Read current workspace priorities from [priorities.md](file:///d:/AI-OS/context/priorities.md) and tasks from the master task list [master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md).
2. Fetch today's calendar events using the personal Google Workspace CLI profile:
   ```powershell
   $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"; gws calendar events list --params '{"calendarId": "primary", "maxResults": 10}'
   ```
3. Synthesize this information and construct an hourly, realistic timeline for today. Prioritize:
   - ZORIXEL creator brand launch prep (Instagram content draft, assets).
   - Core AIOS workflow development.
   - Fixed calendar appointments.
4. Format the daily plan output as a clean table or timeline.
5. Prompt the user for adjustments or confirmation.
