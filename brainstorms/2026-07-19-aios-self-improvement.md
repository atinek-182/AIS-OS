# AIOS Security and Skill Self-Improvement: Brainstorm / Discovery Notes
Date: 2026-07-19 · Goal: Perform security auditing and improve all custom skills in the local directory.

## Summary / key decisions
- **API Credentials Security:** Secure GEMINI_API_KEY, GITHUB_PERSONAL_ACCESS_TOKEN, `gws` tokens, and Notion keys across code, logs, and git commits.
- **Command & Script Executions Security:** Lock down `runner.py`, `manage_autoresearch.py`, and hooks against command injection and path traversal.
- **Data Isolation:** Enforce strict boundaries between personal (`brain-aios/`) and brand (`second-brain-zorixel/`) Obsidian vaults.
- **Reliability (No Regression Cycle):** Break the cycle of introducing new bugs/regressions when fixing a single issue. Implement strict pre-flight validation and testing.
- **Design & Scraping Focus:** Focus AIOS capabilities on premium design aesthetics, scraping competitor references, and visual slide rendering.

## Q&A log
### Q1 — Security & Vulnerability Scope
- Asked: What specific security boundaries or vulnerability concerns are you most worried about?
- Captured:
  - Secure API keys (Gemini, Github, gws, Notion) from leaks.
  - Mitigate command injection & path traversal in runner/manage scripts and hooks.
  - Strict vault separation (personal vs. brand).
  - Solve the "one fix, four new problems" regression cycle.
- Flags: None

### Q2 — Legacy Adaptation & Verification Hook
- Asked: How should we adapt Claude-specific skills (like `claude-seo` and `frontend-slides`) and set up regression prevention?
- Captured:
  - For `claude-seo`, we will read the documents/scripts and adapt them to run under Antigravity. We will also update references to point to adapted paths (e.g. rename `claude-seo` to `seo-audit-reference` and update files to use Antigravity / Gemini standards).
  - For regression prevention, we will build a comprehensive verification suite and expand the git pre-commit hook to run it along with the security check.
- Flags: None

### Q3 — Design & Scraping Skill Gaps
- Asked: When you run the design and scraping skills, what are the most common mistakes or regressions that occur?
- Captured:
  - Visual Auditing: Headless browser tests fail to render fonts properly due to local path blocks. Must enforce base64 font encoding and 5-viewport automated verification.
  - Scraping & Local Hosting: Bypass Playwright `file://` permissions by auto-generating a localhost Node static server (`serve.js`).
  - Dependency Paths: Ensure scripts resolve packages (like Playwright) relative to their containing folders, avoiding CWD Reference/Module errors.
- Flags: None

### Q4 — Completeness & Conflict Resolution
- Asked: Are there other files, design patterns, or vault items we should audit? Should we sync global or local skills?
- Captured:
  - Focus first on the local workspace skills (`d:\AI-OS\.agents\skills\`).
  - Read global skills like `impeccable` and `ui-ux-pro-max` to resolve any conflicts, creating system rules instead of direct modifications.
  - Review files across different vaults to clean up irrelevant or conflicting information.
  - Prioritize checking past transcripts/mistakes to refine the AIOS behavior.
- Flags: None

## Open flags (pending input)
- None (All discovery questions resolved)

