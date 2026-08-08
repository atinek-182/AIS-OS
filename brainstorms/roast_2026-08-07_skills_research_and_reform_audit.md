# Universal Roast Report: Skills Needing Research & Reform Audit
Date: 2026-08-07 · Operator: Atinek Maurya · Domain: strategy / code

[RECOMMENDED: Re-run with --deep for multi-turn attack & patch loop]

---

## 👥 Persona Council Audit: 65 Active Skills Research & Reform Sweep

### 1. Category A: Research & Multi-Agent Intelligence Skills
- **Skills Audited:** `storm-research`, `storm-research-project`, `agent-reach`
- **Contrarian Red-Team Finding:** `storm-research` still references an outdated 5-agent configuration, creating a conflict with the mandatory workspace rule requiring the 7-agent version of `storm-research-project` (Systems Architect, Vibesec Pen-Tester, DB/Scaling Specialist, Frontend UX Lead, Product Economist, AI/LLM Specialist, Developer Ergonomics Auditor).
- **Reform Priority:** High  
- **Actionable Reform Plan:** Deep research into 2026 multi-agent research paradigms (STORM / DeepResearch), deprecate standalone 5-agent calls, and enforce the 7-agent system across all deep research tasks.

---

### 2. Category B: Fullstack Web & TypeScript Architecture Skills
- **Skills Audited:** `jsmastery-architect`, `jsmastery-audit`, `jsmastery-scope`, `mattpocock-to-spec`
- **Contrarian Red-Team Finding:** Code examples in `jsmastery-architect` reference Next.js 14 sync params (`const { id } = params`), missing Next.js 15 App Router breaking changes where `params` and `searchParams` are Promises (`const { id } = await params`). Additionally, Tailwind v3 `@apply` patterns are present instead of Tailwind v4 CSS `@theme` directives.
- **Reform Priority:** High  
- **Actionable Reform Plan:** Conduct targeted docs query for Next.js 15 App Router Async APIs, React 19 Server Actions, and Tailwind CSS v4 syntax, updating `jsmastery-architect` and `mattpocock-to-spec` reference templates.

---

### 3. Category C: Ingestion & Repository Skill Engines
- **Skills Audited:** `ingest-repo`, `ingest-skills`, `skill-builder`
- **Contrarian Red-Team Finding:** `ingest-repo` clones external repositories into workspace temporary folders without strict scratch isolation (`scratch/ingest-[repo-name]/`) or mandatory post-ingestion cleanup commands, risking workspace git bloat and context leaks.
- **Reform Priority:** Medium  
- **Actionable Reform Plan:** Enforce strict scratch directory isolation and auto-deletion in `ingest-repo/SKILL.md`.

---

### 4. Category D: Business Automation & Pricing Engines
- **Skills Audited:** `zero-paywall-client-os`, `ai-pricing-engine`, `new-client`
- **Contrarian Red-Team Finding:** `ai-pricing-engine` lacks direct programmatic handoff to the newly upgraded 4-axis `/roast` risk matrix to validate client proposals against the Nate Herk 3-Number Corridor before delivering quotes.
- **Reform Priority:** Medium  
- **Actionable Reform Plan:** Connect `ai-pricing-engine` directly to `/roast --domain offer --save` to generate pre-proposal risk certificates.

---

### 5. Category E: Frontend UI & Quality Gate Systems
- **Skills Audited:** `website-design-engine`, `hallmark`, `verify-design`
- **Contrarian Red-Team Finding:** `website-design-engine` lacks explicit Playwright base64 font verification checks for local `.otf`/`.ttf` fonts, risking broken headline font fallbacks during Playwright visual QA audits on Windows.
- **Reform Priority:** Medium  
- **Actionable Reform Plan:** Update `verify-design` and `website-design-engine` with mandatory base64 font Data URI checks in temporary visual QA pages.

---

## ⚖️ THE VERDICT: RESHAPE
Confidence: High · Operator: Atinek Maurya · Domain: strategy / code

**The Call in One Line:** Prioritize structural reform for 5 core skill clusters (STORM Research, Fullstack Next.js 15 Architecture, Repo Ingestion, AI Pricing, and Frontend Font QA) to eliminate technical debt and stack staleness.

**Why:** While basic emoji cleaning was completed, underlying skill instruction files contain framework version drift (Next.js 14 vs 15) and agent count conflicts (5-agent vs 7-agent STORM). Reforming these 5 clusters guarantees state-of-the-art execution.

**Biggest Risk:** Using outdated Next.js 14 sync params or 5-agent STORM research templates in production builds.  
**Biggest Upside:** Standardizing all 65 skills on modern Next.js 15, React 19, 7-agent STORM research, and 4-axis `/roast` integration.

**Money & Velocity Read:** Phase-based reform sprint over 2-3 sessions, securing high-quality code generation for all future agency projects.

**4-Axis Risk Matrix:**
- Security / Failure Risk: 4/10
- Implementation Friction: 4/10
- Value & ROI: 9/10
- System Simplicity: 8/10

**Council Scores:** Contrarian 6/10 · Expansionist 9/10 · Logician 9/10 · Researcher 9/10 · Buyer 9/10

**The Cheapest 48-Hour Test:** Execute targeted updates on `storm-research` and `jsmastery-architect`, verifying Next.js 15 async params and 7-agent STORM research compliance.

---

## ROAST_REFINEMENT_SPEC
- [ ] Phase 1 (Research & Intelligence): Update `storm-research` and `storm-research-project` to enforce the 7-agent system strictly across all research tasks.
- [ ] Phase 2 (Fullstack Architecture): Upgrade `jsmastery-architect` and `mattpocock-to-spec` templates to Next.js 15 App Router Async Request APIs and Tailwind v4.
- [ ] Phase 3 (Repo Ingestion): Enforce `scratch/ingest-[repo-name]/` isolation and force-cleanup in `ingest-repo`.
- [ ] Phase 4 (Business Pricing): Integrate `/roast --domain offer --save` into `ai-pricing-engine`.
- [ ] Phase 5 (Frontend QA): Add Playwright base64 font Data URI checks to `verify-design`.
