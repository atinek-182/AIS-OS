# Skill Workflow Evolver: Brainstorm / Discovery Notes
Date: 2026-08-08 · Goal: Design and build a new native Tier 1 skill (`skill-workflow-evolver`) that automatically scans workspace skills, detects newly added skills/capabilities, maps them into domain pipelines, generates new workflow playbooks, updates master scenario maps, runs /roast audits, and runs pre-flight health checks.

## Summary / Key Decisions
- **Selected Architecture Focus:** Option A — Native Tier 1 Skill (`.agents/skills/skill-workflow-evolver/SKILL.md`) + Automated Python Runner Script (`scripts/skill_workflow_evolver_runner.py`).
- **Core Directive:** Make the skill hyper-detailed, production-grade, and self-upgradable every time new skills or capabilities are installed.
- **Key Capability Pillars:**
  1. AST & YAML Metadata Scanner (`scripts/skill_workflow_evolver_runner.py`).
  2. Domain Classifier & Pipeline Router (Slotting skills into Agency, Fullstack, UI/UX, Debug, or Research).
  3. Playbook & Workflow Generator (Updating `brainstorms/2026-08-08-skill-workflows-and-scenario-mapping.md`).
  4. Adversarial `/roast` Council Audit Gate (Stress-testing new playbooks).
  5. Pre-Flight Health Sweep & Rule Sync (`verify_skills.py` & `test_skill_workflows_health.py`).

---

## Q&A Log

### Q1 — Skill Implementation & Automation Structure
- **Asked:** How should we implement and structure the new `skill-workflow-evolver` skill?
- **Captured Decision:** User selected **Option A (Native Tier 1 Skill + Automated Python Runner Script)** with explicit instructions to make it hyper-detailed, robust, and self-upgradable every time a new skill is added.
- **Flags:** Python runner script `scripts/skill_workflow_evolver_runner.py` queued for immediate creation.

---

## Open Flags (Pending Operator Input)
- **Q2 Topic:** 5-Phase Self-Upgrading Execution Loop & Runner Script Feature Specification.
