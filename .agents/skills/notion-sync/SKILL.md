---
name: notion-sync
description: Use when you need to sync local decisions, content calendars, or task lists to Notion databases or pages.
---

## What This Skill Does

Enables the AIOS to sync decision logs, checklists, or competitor research details directly to a remote Notion workspace.

## Steps

1. If no data to sync is provided, scan `decisions/log.md`, `brain-aios/wiki/log.md`, or the active brainstorm capture for recent entries.
2. Read target Notion Database ID or Parent Page ID from the environment configuration or prompt arguments.
3. Formulate the database property JSON structure matching the database's schema (e.g. Title, Date, Text content).
4. Use the `notion-mcp-server:API-post-page` tool to push the new page, or `API-patch-page` to update properties.
5. Confirm successful sync with the user.
