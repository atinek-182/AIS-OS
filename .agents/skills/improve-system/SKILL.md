---
name: improve-system
description: Analyze the current session transcript to update skill instructions, save lessons, update memory, audit web/code security, and prune stale configurations.
argument-hint: "[optional focus or specific file]"
---

# System Self-Improvement & Security Audit Workflow

Use this skill when you finish a major milestone, significantly refine a custom skill, solve complex bugs, or run an end-of-session system enhancement. This skill extracts lessons, enforces empirical verification, performs security audits, updates persistent memory, and maintains workspace directory hygiene.

## Triggering Rules
- Proactively recommend invoking `/improve-system` at the end of a session where architectural iterations, bug workarounds, or custom skill updates occurred.
- Triggered when the user runs `/improve-system` or asks to "improve the system", "save lessons", "update memory", or "log this experience".

---

## Execution Workflow

### Step 1: Ingest Session Logs & Deep Transcript Pattern Analysis
1. Locate the active conversation's `transcript.jsonl` under:
   `C:/Users/HP/.gemini/antigravity-ide/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`
   (Substituting the active `Conversation ID` from your session metadata).
2. Scan the transcript backward to identify:
   - User corrections, explicit layout/design directives, and formatting feedback.
   - Script, compiler, or build tool failures (HTTP 429 rate limits, JSX syntax crashes, scoping errors).
   - Tool execution workarounds (Playwright permission blocks, Node dependency paths, local server fallbacks).

### Step 2: Integrated Security Audit (Vibesec & Secrets Hygiene)
Run a security check across all modified workspace files:
1. **Secrets Hygiene**:
   - Check for hardcoded API keys, OAuth tokens, or passwords in source files, scripts, or committed templates.
   - If secrets are found, flag them immediately, strip them from source code, and store them securely in environment variables or intake configs.
2. **Web & Code Security Audit (Vibesec Guidelines)**:
   - Check for unescaped user input rendering in HTML/JSX templates.
   - Verify CORS, CSP, and local HTTP server headers on scratch test servers.
   - Ensure safe shell command execution (no raw concatenated string injections).

### Step 3: Extract & Categorize System Insights
Categorize findings into four distinct system outputs:
1. **Developer Experience & Story**: High-leverage developer insights and architectural primitives (e.g. Figma node visibility rules, pre-rotated SVG geometry transforms, SVG-to-JSX inline style object conversions).
2. **Skill / System Refinements**: Proposed improvements for `.agents/skills/[skill-name]/SKILL.md` configurations or templates.
3. **Workspace Rules & Memory Updates**: Additions for `AGENTS.md` (coding/compiler rules) or `MEMORY.md` (user preferences & voice).
4. **Directory & Workspace Map Hygiene**: Registration of new utility scripts in `WORKSPACE_MAP.md` and pruning of obsolete scratch files.

### Step 4: Compile & Present System Improvement Proposal
Create a structured Markdown proposal containing:
- **Learnings & Security Findings**: Story summary, security posture, and guidelines established.
- **Proposed Skill Diffs**: Exact changes to `.agents/skills/` files.
- **Rules & Memory Diffs**: Proposed additions to `AGENTS.md` and `MEMORY.md`.
- **Pruning & Index Plan**: Files to create in `brain-aios/wiki/experiences/`, index in `context/experiences/README.md`, or register in `WORKSPACE_MAP.md`.

Wait for user approval before executing file writes.

### Step 5: Execute Approved Changes & Empirical Verification
Upon approval, execute the changes:
1. **Write Experience Document**:
   - Create `brain-aios/wiki/experiences/YYYY-MM-DD-[slug].md`.
   - Update `context/experiences/README.md` chronological index.
2. **Update Skills, Rules & Memory**:
   - Update target `.agents/skills/` files.
   - Update workspace rules in `AGENTS.md` and persistent memory in `MEMORY.md`.
3. **Log & Clean**:
   - Record architectural changes in `decisions/log.md` and Obsidian index in `brain-aios/wiki/log.md`.
   - Update `WORKSPACE_MAP.md`.
4. **Empirical Verification Check**:
   - Run verification scripts (Playwright screenshot comparisons, AST/lint validators, or test suites) to ensure 0 regressions.

---

## Experience Document Template

Files created in `brain-aios/wiki/experiences/` must follow this format:

```markdown
# [Title of the Experience]

## Lesson / Story
[A clear narrative paragraph explaining what happened, the root cause identified, and the technical solution executed.]

## System Guidelines & Security Rules Established
- **[Rule Name]:** [Concrete guideline to prevent this issue.]
- **[Security Rule Name]:** [Secrets hygiene or application security rule.]
```
