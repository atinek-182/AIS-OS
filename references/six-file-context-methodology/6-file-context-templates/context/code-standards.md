---
title: Code Standards
domain: architecture
summary: '- [Principle — e.g. Keep modules small and single-purpose] - [Principle — e.g. Fix root causes, do not layer workarounds]'
critical_directives:
- '[Rule — e.g. Strict mode is required throughout the project]'
- '[Rule — e.g. Validate unknown external input at system'
- '[Rule — e.g. Use CSS custom property tokens — no'
- '[Rule — e.g. Follow the border radius scale defined'
section_outline:
- Code Standards
- General
- TypeScript
- '[Framework — e.g. Next.js]'
- Styling
read_triggers:
- When working on architecture in references/six-file-context-methodology/6-file-context-templates/context/code-standards.md
- When reading context for Code Standards
tags:
- architecture
- code-standards
updated: '2026-08-08'
---

# Code Standards

## General

- [Principle — e.g. Keep modules small and single-purpose]
- [Principle — e.g. Fix root causes, do not layer workarounds]
- [Principle — e.g. Do not mix unrelated concerns in one
  component or route]

## TypeScript

- [Rule — e.g. Strict mode is required throughout the project]
- [Rule — e.g. Avoid any — use explicit interfaces or narrowly
  scoped types]
- [Rule — e.g. Validate unknown external input at system
  boundaries before trusting it]

## [Framework — e.g. Next.js]

- [Convention — e.g. Default to server components]
- [Convention — e.g. Add use client only when browser
  interactivity requires it]
- [Convention — e.g. Keep route handlers focused on a
  single responsibility]

## Styling

- [Rule — e.g. Use CSS custom property tokens — no
  hardcoded hex values]
- [Rule — e.g. Follow the border radius scale defined
  in ui-context.md]

## API Routes

- [Rule — e.g. Validate and parse request input before
  any logic runs]
- [Rule — e.g. Enforce auth and ownership before any mutation]
- [Rule — e.g. Return consistent, predictable response shapes]

## Data and Storage

- [Rule — e.g. Metadata belongs in the database]
- [Rule — e.g. Large generated content belongs in file
  or blob storage]
- [Rule — e.g. Do not store large content directly in
  the database]

## File Organization

- `[folder]/` — [What belongs here]
- `[folder]/` — [What belongs here]
- `[folder]/` — [What belongs here]
- `[folder]/` — [What belongs here]s
