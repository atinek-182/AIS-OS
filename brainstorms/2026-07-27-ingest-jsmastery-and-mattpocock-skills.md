# Discovery Capture: Ingestion of `jsmastery-pro/skills` & `mattpocock/skills`

**Date**: 2026-07-27
**Repos Ingested**:
1. `jsmastery-pro/skills` (https://github.com/jsmastery-pro/skills)
2. `mattpocock/skills` (https://github.com/mattpocock/skills)

## Overview & Objectives
The user requested integrating skills from both JavaScript Mastery Pro and Matt Pocock into Atinek Maurya's AIOS (`AI-OS`) in the best way possible.

## Core Strategy
1. **Tier 2 Archival**: Ingest complete raw repos into `brain-aios/wiki/research/skills-library/jsmastery-skills/` and `brain-aios/wiki/research/skills-library/mattpocock-skills/` for persistent indexing and offline access.
2. **Tier 1 Direct AIOS Adaptation**:
   - Synthesize and adapt high-leverage unique skills directly into `.agents/skills/`:
     - `jsmastery-architect`: Full-stack JavaScript / Next.js architecture guidelines.
     - `jsmastery-audit`: JS Mastery full-stack code auditor.
     - `mattpocock-domain-modeling`: TypeScript domain modeling & advanced type-driven design.
     - `mattpocock-wayfinder`: Codebase navigation, entrypoint discovery, and boundary mapping.
     - `mattpocock-to-spec`: Technical SPEC writer converting fuzzy intent into structured architecture contracts.
     - `mattpocock-to-tickets`: Decomposing specs into atomic, task-oriented engineering tickets.
     - `mattpocock-teach`: Socratic teaching and mental model builder for TS & web engineering.
     - `mattpocock-setup-ts-deep-modules`: Deep module boundary enforcement and package structure.
   - Upgrade existing AIOS skills (`grill-me`, `roast`, `gstack`, `systematic-debugging`, `test-driven-development`) with superior patterns found in Matt Pocock and JS Mastery skills (e.g. docs-backed grilling, TS-driven error diagnosis).
3. **Platform Adaptation**: Convert all Claude Code specific CLI commands/paths (`.claude/`, `claude`, `npx skills`) into native Antigravity triggers, slash commands (`/jsmastery-architect`, `/mattpocock-domain-modeling`, etc.), and dynamic intent rules in `.agents/AGENTS.md`.
4. **Security Audit**: Ensure license compliance (MIT), check key hygiene, verify no unsafe RCE or unauthenticated network calls.
5. **System Integration**: Update `references/antigravity-skills-guide.md`, `references/aios-user-manual.md`, `GEMINI.md`, `MEMORY.md`, `WORKSPACE_MAP.md`, `decisions/log.md`, `brain-aios/wiki/log.md`, and `brain-aios/wiki/index.md`.
