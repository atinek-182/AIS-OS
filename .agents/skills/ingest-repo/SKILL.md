---
name: ingest-repo
description: "Autonomous 8-phase repository ingestion, security audit, comparative analysis, roast council, deep cross-system integration, and dual slash/dynamic skill adaptation engine."
argument-hint: "[repo_url] [optional focus or instructions]"
---

# Repository Ingestion & Deep Skill Adaptation Engine (`/ingest-repo`)

Use this skill whenever the user provides a GitHub repository link or asks to "ingest this repo", "adapt this repository", "analyze repo for AIOS", or runs `/ingest-repo [repo_url]` (or `/ingest-skills [repo_url]`).

---

## The 8-Phase Ingestion & Deep System Integration Workflow

### Phase 1: Discovery Capture & Setup (`/grill-me` loop)
1. Determine repository name from URL (e.g. `https://github.com/user/repo-slug` -> `repo-slug`).
2. Create discovery capture file at `brainstorms/{date}-ingest-{repo-slug}.md`.
3. If specific user intent/focus is ambiguous, ask targeted, single-topic clarifying questions with recommended answers. Checkpoint every response to the capture file.

### Phase 2: Isolated Repository Clone & Structural Analysis
1. **Isolated Scratch Directory**: Create temporary directory `scratch/ingest-{repo-slug}/`.
2. Clone repository into `scratch/ingest-{repo-slug}/` (Clear process environment tokens `$env:GITHUB_TOKEN=$null` if needed):
   ```powershell
   git clone --depth 1 [repo_url] scratch/ingest-{repo-slug}
   ```
3. Inspect repository structure:
   - Identify primary language, frameworks, dependencies, CLI entry points, and licenses.
   - Scan for existing skills (`skills/`), rules (`rules/`, `.cursorrules`), or scripts (`scripts/`).

### Phase 3: Web Research & Security Audit (Vibesec & Supply Chain)
1. **Web Research**:
   - Run `search_web` to discover real-world community use cases, production implementations, performance benchmarks, and user feedback.
2. **Security Audit**:
   - Verify License (Must be 100% free and open-source for personal/commercial gain, e.g. MIT, Apache 2.0, BSD).
   - Check secret hygiene: Ensure no hardcoded tokens/keys are committed.
   - Audit network calls & execution safety: Check for unverified remote code execution or internal SSRF risks.

### Phase 4: AIOS Workspace & Vault Comparison Analysis
1. Search AIOS directories (`.agents/skills/`, `scripts/`, `brain-aios/`, `second-brain-zorixel/`, `premium-frontend-experience-system/`) for existing features or overlapping tools.
2. Perform comparative analysis:
   - **Feature Superiority & Legacy Deprecation**: Is the new repo's engine cleaner, faster, or more resilient than an existing AIOS implementation? If superior, flag the older function/script for replacement.
   - **Two-Tier Categorization**:
     - **Tier 1 (Immediate AIOS Adaptation)**: High-leverage features for active goals -> build active scripts (`scripts/`), slash command skills (`.agents/skills/`), and workspace rules immediately.
     - **Tier 2 (Future Vault Reference)**: Specs, manuals, and future-potential guides -> store in `brain-aios/wiki/research/skills-library/{repo-slug}/` for automatic retrieval.

### Phase 5: Adversarial Roast Council Gate (`/roast`)
1. **Convene the 5-Persona Roast Council in Parallel**:
   - **Contrarian (Red Team)**: Attacks workspace pollution, token leaks, security vulnerabilities, and fatal flaws.
   - **Expansionist (Bull)**: Identifies 10x upside, adjacent workflows, and unmentioned revenue/automation leverage.
   - **Logician (First Principles)**: Verifies first-principles code logic and whether the architecture is simpler than existing AIOS code.
   - **Researcher (Evidence)**: Brings web evidence, real-world benchmarks, and community consensus.
   - **Buyer / Developer**: Roleplays as Atinek Maurya testing if this speeds up daily workflow or adds unnecessary overhead.
2. **Synthesize Judge Verdict (GO / RESHAPE / KILL)**:
   - Address and resolve **EVERY SINGLE OBJECTION** raised by the Contrarian and council before producing code.
   - Outline the cheapest 48-hour validation test if RESHAPE.

### Phase 6: Multi-Artifact Adaptation & Dual-Trigger Skill Generation
1. **Runner Scripts**: Create or adapt clean Python/Node scripts in `scripts/` (e.g., `scripts/{repo-slug}_runner.py`).
2. **Dual-Trigger Skills**: Create custom slash command skills in `.agents/skills/{skill-slug}/SKILL.md`.
   - **Mandatory Dual-Triggering Standard**: Ensure YAML frontmatter `description` includes natural language trigger phrases so the skill can be invoked **both via explicit `/` slash commands AND dynamically** when performing matching user tasks.
3. **Platform Adaptation**: Dynamically adapt all Claude/Cursor platform-specific references to native Antigravity standards.
4. **Reference Library**: Copy full manuals and guides to `brain-aios/wiki/research/skills-library/{repo-slug}/`.

### Phase 7: Deep Cross-System Integration & Mandatory Workspace Documentation Update
1. **Deep System Integration**:
   - Embed the new features/skills into existing workspace skills (`.agents/skills/`), developer subagents (`.agents/agents/developer.md`), scripts (`scripts/`), SOPs (`brain-aios/wiki/sops/`), and automations.
   - Replace older, inferior functions or scripts with the newly ingested engine.
2. **Mandatory Documentation Sweep Across ALL Handbooks & Vaults**:
   - **User Manual**: Update `references/aios-user-manual.md` with full skill usage, slash command args, and dynamic natural language triggers.
   - **Skills Guide**: Update `references/antigravity-skills-guide.md` registering repo URLs, local paths, and trigger behaviors.
   - **Operator Prompt**: Update `GEMINI.md` skills list and operator instructions.
   - **Persistent Memory**: Update `MEMORY.md` with operational rules, auto-search guidelines, and architecture patterns.
   - **Workspace Map**: Update `WORKSPACE_MAP.md` registering scripts, skills, and vault research directories.
   - **Logs & Indexes**: Update `decisions/log.md`, `brain-aios/wiki/log.md`, `brain-aios/wiki/index.md`, and `second-brain-zorixel/wiki/index.md`.
   - **Experiences**: Update `context/experiences/README.md` if an experience document was generated.

### Phase 8: Empirical Verification, Cleanup & Self-Improvement
1. **Mandatory Scratch Cleanup**: Force-delete temporary folder `scratch/ingest-{repo-slug}/` to prevent workspace pollution and token leaks.
2. **Map Validation**: Run `python scripts/validate_workspace_map.py` to confirm 0 map drift.
3. **Automated Unit Testing**: Execute unit tests or runner verifiers to confirm 100% pass rate.
4. **System Self-Improvement**: Suggest running `/improve-system` to persist learnings.
