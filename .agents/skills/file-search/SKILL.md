---
name: file-search
description: Use when the user wants to search for a file, find information across vaults, or retrieve documents by keyword.
argument-hint: [search query]
---

## What This Skill Does

Enables high-performance keyword search across both local Obsidian vaults (the AIOS general vault and the Zorixel brand second brain vault), presenting clickable links and contextual matching snippets.

## Steps

1. If no query is provided in `$ARGUMENTS`, ask the user what keyword or phrase they want to find.
2. Run a recursive search across the following directories:
   - [brain-aios/](file:///d:/AI-OS/brain-aios/)
   - [second-brain-zorixel/](file:///d:/AI-OS/second-brain-zorixel/)
   Exclude `.git`, `.obsidian`, and binary files.
3. For each match found:
   - Format the filename as a clickable link: `[basename](file:///d:/AI-OS/...)`.
   - Include the line number and a snippet of the matching content.
4. Output the search results grouped by vault.
