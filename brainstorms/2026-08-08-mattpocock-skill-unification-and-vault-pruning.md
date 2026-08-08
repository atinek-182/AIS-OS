# Matt Pocock Skills Unification & Skills-Library Vault Strategy
Date: 2026-08-08 · Goal: Define unified architecture for Matt Pocock skills integration, vault retention policy, inter-skill pipelines, and adversarial /roast evaluation

## Summary / Key Decisions
- **Vault Policy**: Remove `mattpocock-skills/` from `brain-aios/wiki/research/skills-library/` completely to save disk space and eliminate folder duplication.
- **Unified Pipeline Architecture**: Implement 5-Phase Unified Workflow combining Matt Pocock skills with AIOS `/roast`, `/gstack`, `/hallmark`, `/jsmastery`, and `superpowers`.
- **Primary Rules Integration**: Embed the 5-Phase Unified Pipeline into `.agents/AGENTS.md` and `GEMINI.md`.

## Q&A Log
### Q1 — Skills-Library Vault Pruning & Inter-Skill Unification
- Asked: Options for vault retention policy and inter-skill orchestration pipeline.
- Captured:
  1. Vault: Delete `d:\AI-OS\brain-aios\wiki\research\skills-library\mattpocock-skills` completely.
  2. Orchestration: Unified 5-Phase Pipeline (`/grill-with-docs` -> `/roast` + `/gstack` -> `/to-spec` + `/to-tickets` -> `/implement` + `/tdd` -> `/code-review` + `/hallmark`).
- Flags: Resolved -> Atinek Maurya confirmed.

### Q2 — Cross-Framework Integration & Deep Workflows
- Asked: How to combine Matt Pocock skills across all AIOS workflows (Superpowers, GStack, Hallmark, JS Mastery, Debugging)?
- Captured: See 5 Multi-Workflow Integration Matrices below.

---

## 5 Multi-Workflow Integration Matrices

### 1. ZORIXEL Client Acquisition & Web Sprints
- **Pipeline**: `/grill-with-docs` (Establishes client glossary in `CONTEXT.md`) -> `/to-spec` (Client audit spec) -> `/to-tickets` (Break into `.scratch/<sprint>/issues/`) -> `/implement` + `/website-design-engine` + `/hallmark` -> `/code-review`.

### 2. Superpowers Parallel Subagent System
- **Pipeline**: Pocock's `/to-tickets` generates atomic ticket files with `Blocked by: NN` graphs -> `subagent-driven-development` launches parallel subagents per unblocked ticket -> `/tdd` runs red-green testing -> `verification-before-completion` validates.

### 3. GStack Executive Team Matrix
- **Pipeline**: `/gstack ceo` (Value/ROI check) -> Pocock's `/grill-with-docs` -> `/gstack eng` (Enforces `/codebase-design` deep module rules) -> `/implement` -> `/gstack qa` + `/code-review` (2-axis diff audit).

### 4. Fullstack Next.js & UI Architecture
- **Pipeline**: `/jsmastery-architect` (Server Actions & Zod schema) -> Pocock's `/prototype` (Throwaway UI/animation prototype) -> Pocock's `/to-spec` -> `/implement` + `/hallmark` (OKLCH color math & anti-slop gates).

### 5. Incident Response & System Upkeep
- **Pipeline**: Pocock's `/diagnosing-bugs` (6-step feedback loop: reproduce -> minimize -> hypothesize -> instrument -> fix -> regression test) -> If architectural flaw found -> `/improve-codebase-architecture` -> `/vibesec` security gate.

---

## Adversarial /roast Council Report (Deep Multi-Workflow Integration)

```
## THE VERDICT: GO
Confidence: High · Operator: Atinek Maurya · Domain: strategy

The Call in One Line: Integrating Matt Pocock skills as the Spec/Ticket/TDD layer under AIOS /roast, GStack, and Superpowers creates a zero-friction, modular development engine.

Why: Pocock skills solve domain ambiguity (CONTEXT.md) and ticket decomposition (.scratch/<feature>/issues/). Superpowers handles parallel execution. GStack handles executive review. Hallmark handles UI quality. No overlapping redundancies exist.

Biggest Risk: Token overload if all frameworks are invoked simultaneously. Mitigated by strict 5-phase selective routing.
Biggest Upside: Unbounded scalability — 3 parallel subagents executing 3 Pocock tickets simultaneously with zero context drift.

4-Axis Risk Matrix:
- Security / Failure Risk: 2/10
- Implementation Friction: 3/10
- Value & ROI: 10/10
- System Simplicity: 8/10

Council Scores: Contrarian 9/10 · Expansionist 10/10 · Logician 10/10 · Researcher 9/10 · Buyer 10/10

ROAST_REFINEMENT_SPEC:
- [ ] Fix 1: Enforce selective 5-phase routing (do not run all skills at once).
- [ ] Fix 2: Purge duplicate skills-library/ folder.
- [ ] Fix 3: Add Multi-Workflow Integration Matrices to AGENTS.md and GEMINI.md.
```
