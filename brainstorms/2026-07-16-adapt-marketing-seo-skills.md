# Adapt Marketing and SEO-Audit Skills: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Adapt corey-haynes-marketing-skills and DanielAgrici-seo-audit-skills into custom, simple, and fast Antigravity skills.

## Summary / key decisions
- **Consolidation**: Do not pollute the main custom skills directory with 70+ separate files.
- **Workflow/Registry System**: Store all reference skills in a dedicated database or directory (e.g. `references/skills-library/`), and use a routing system/manager agent or single unified workflow skills to dynamically look up and apply these frameworks on demand.
- **Separate Router Skills**: Create exactly two active workspace skills: `marketing` (for copywriting, email, Instagram) and `seo-audit` (for technical audits, schema, pagespeed, GEO). Both will dynamically load rules from the library.
- **Preserve Executables**: Keep the Python scripts inside the library path (`d:\AI-OS\brain-aios\wiki\research\skills-library/claude-seo/scripts/`) so they can be run programmatically, rather than deleting them.
- **Performance**: Confirmed this approach avoids memory bloat, keeps the workspace clean, and optimizes prompt caching.
- **Triggers**: 
  - `marketing`: Triggers on copywriting, sales copy, landing pages, email copy, Instagram captions. Slash command: `/marketing`.
  - `seo-audit`: Triggers on technical SEO, schema, sitemaps, GEO/AEO tasks. Slash command: `/seo-audit`.

## Q&A log
### Q1 — Consolidation Strategy vs. Full Porting
- Asked: Should we install all 70+ separate skills or consolidate them into 2 project skills (`marketing` and `seo-audit`)?
- Captured: The user wants to avoid polluting the skills folder but wants a system that can access all ~45 copywriting/experiment skills and ~25 SEO sub-skills/agents. The system should dynamically call them on-demand via a background workflow/system rather than requiring manual invocations.

### Q2 — Dynamic Reference Library with Router Skill
- Asked: Do you approve of using a Dynamic Reference Library stored at `brain-aios/wiki/research/skills-library/` coupled with a single workspace router skill at `.agents/skills/marketing-seo-engine/`?
- Captured: The user approved the system. They also requested verifying whether removing Python and other executable files from the `claude-seo` repo would degrade the quality of the audits.

### Q3 — Preserving Python Executables vs. Purging Them
- Asked: Does keeping python executables in the library path degrade quality?
- Captured: The user approved keeping python executables in the static library. They asked whether this approach damages or boosts system performance.

### Q4 — System Performance Impact
- Asked: Does it damage or boost system performance?
- Captured: Explained that this boosts performance by avoiding startup lag, command collisions, and token bloat. The user approved.

### Q5 — Triggers and Command Namespace
- Asked: What should trigger the `marketing-seo-engine` skill?
- Captured: The user approved the proposed triggers: copywriting, sales copy, landing pages, email copy, Instagram captions, SEO, technical audits, schema, sitemaps, and GEO/AEO tasks.

### Q6 — Single vs. Separated Skills
- Asked: Does the router skill combine both or should we separate them?
- Captured: The user clarified whether the router skill would only be for marketing and not SEO. We decided to split it into two clean, separate router skills: `marketing` and `seo-audit` for clearer triggers and separate slash commands.

## Open flags (pending input)
