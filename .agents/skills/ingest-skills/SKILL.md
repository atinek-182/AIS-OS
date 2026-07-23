---
name: ingest-skills
description: "Upgraded alias & dynamic repository ingestion engine routing directly to /ingest-repo."
argument-hint: "[repo_url] [optional focus or instructions]"
---

# Ingest Community Skills & Repositories (Upgraded Engine & Dynamic Skill)

Use `/ingest-skills` (or invoke naturally via phrases like "ingest skills", "ingest repository", "adapt community skill", "clone and ingest repo") to trigger the upgraded **`/ingest-repo`** deep cross-system integration engine.

---

## The Upgraded Ingestion & Dynamic Adaptation Workflow

When invoked, execute the complete workflow documented in [d:\AI-OS\.agents\skills\ingest-repo\SKILL.md](file:///d:/AI-OS/.agents/skills/ingest-repo/SKILL.md):

1. **Discovery Capture & Setup (`/grill-me`)**: Create capture file at `brainstorms/{date}-ingest-[repo-slug].md`.
2. **Isolated Repository Clone (`scratch/ingest-[repo-slug]`)**: Clone shallow repo into isolated scratch folder.
3. **Web Research & Security Audit (Vibesec & Secret Hygiene)**: Verify 100% open-source license and secret safety.
4. **AIOS Workspace & Vault Comparative Analysis**: Compare against existing tools; flag older/inferior logic for deprecation and categorize features into Tier 1 (Active AIOS) and Tier 2 (Skills Library Vault).
5. **Adversarial Roast Council Gate (`/roast`)**: Run 5-persona evaluation (Contrarian, Expansionist, Logician, Researcher, Buyer) for a Judge verdict.
6. **Multi-Artifact Adaptation & Dual-Trigger Skill Generation**:
   - Build clean Python/Node runner scripts under `scripts/`.
   - Build skills with mandatory dual slash + natural language dynamic triggering capabilities in `.agents/skills/` and global config.
7. **Deep Cross-System Integration & Mandatory Workspace Documentation Sweep ("Add these skills usage everywhere needed")**:
   - Embed newly ingested features, dynamic rules, quality gates, and runner commands directly into all relevant existing workspace assets:
     - **System Rules**: Update `.agents/AGENTS.md` with explicit Dynamic Invocation Rules for the ingested skill.
     - **Developer Subagent**: Update `.agents/agents/developer.md` adding the new skill's engine and quality checks to the lead developer prompt.
     - **Existing Skills**: Integrate the new skill into relevant workflow skills in `.agents/skills/` (e.g., `new-project`, `design-direction`, `verify-design`, `carousel-copy`, etc.).
     - **SOPs & Playbooks**: Update matching operational playbooks in `brain-aios/wiki/sops/` and `second-brain-zorixel/`.
     - **Script & Function Replacement**: Replace older, inferior functions or scripts with the newly ingested engine.
   - Update ALL handbooks: `references/aios-user-manual.md`, `references/antigravity-skills-guide.md`, `GEMINI.md`, `MEMORY.md`, `WORKSPACE_MAP.md`, `decisions/log.md`, `brain-aios/wiki/log.md`, `brain-aios/wiki/index.md`, `second-brain-zorixel/wiki/index.md`.
8. **Empirical Verification, Scratch Cleanup & Self-Improvement**: Force-delete scratch folder, run `python scripts/validate_workspace_map.py`, and run unit/runner tests.
