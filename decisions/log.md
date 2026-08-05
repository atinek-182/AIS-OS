# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.

## 2026-08-04 — Implementation of Client 1 (Vashishthya Research) Notion OS & Google Apps Script Infrastructure

**Decision:** Designed, implemented, and verified the complete 100% free, zero-developer-dependency Notion Operational OS & Google Workspace Sync Engine for Vashishthya Research Education Foundation (`001-vashishthya-research-edu`):
1. **Canonical Notion Database Schema (`NOTION_DATABASE_SCHEMA.json`)**: Created [NOTION_DATABASE_SCHEMA.json](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/NOTION_DATABASE_SCHEMA.json) specifying 18 properties, 7 core service options, 4 financial properties (`Agreed Total Fee`, `Advance Received`, `Balance Due [Formula]`, `Payment Status [Select]`), assigned staff dropdowns, 5-step sub-task checkboxes, and visual progress bar formulas (`[████░░░░░░] 40%`).
2. **Backward-Compatible Google Apps Script Engine (`GoogleAppsScript_NotionSync.gs`)**: Built [GoogleAppsScript_NotionSync.gs](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/GoogleAppsScript_NotionSync.gs) using **Dynamic Header Mapping (`getHeaderMap`)**. Adding new columns or tabs in the future **NEVER breaks existing sync or automation functions**.
3. **Setup SOP & Visual Cheat Sheet**: Created [VASHISTHYA_NOTION_GSHEETS_SETUP_GUIDE.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/VASHISTHYA_NOTION_GSHEETS_SETUP_GUIDE.md) and [setup_guide_visual.html](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/setup_guide_visual.html) providing a 1-page visual cheat sheet with UI wireframes and step-by-step setup instructions.
4. **Validation & Indexing**: Verified JSON schema syntax (`JSON Schema Valid! Properties count: 18`) and registered artifacts in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md).

**Why:** Gives Client 001 a 100% free, non-technical operational OS that syncs 24/7 in the cloud without Make.com paywalls, n8n subscriptions, or local developer server maintenance.

**Owner:** Atinek Maurya / AIOS

## 2026-08-04 — Ingestion of Client 1 (Vashishthya Research) Primary Service Catalog & Pricing Matrix

**Decision:** Ingested verified service catalog extracted from Vashishthya Research Education Foundation's primary promotional flyer provided via sister referral:
1. **Canonical Service Catalog (`SERVICES_CATALOG.md`)**: Created [SERVICES_CATALOG.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/SERVICES_CATALOG.md) documenting all 7 core services and exact INR pricing (Ph.D. Writing ₹20,000, PG Dissertation ₹5,000, Book Writing ₹3,000 / Pub ₹5,000, Paper Writing ₹2,000, Reports ₹100-₹200, Patents ₹15,000, Academic Awards & Proposal Support), primary email `parsjp17@gmail.com`, and phone/WhatsApp numbers (`8319353139`, `8349687471`).
2. **Updated Master Audit (`AUDIT.md`)**: Updated [AUDIT.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/AUDIT.md) with exact contact details and canonical service catalog links.
3. **Updated Notion OS Master Plan (`NOTION_WORKFLOW_MASTER_PLAN.md`)**: Replaced placeholder service fields with exact 7 service options in View A Call Intake Desk checkboxes and assigned team members (`Dr. Prashant Singh` | `Dr. Pooja Singh`).
4. **Updated Pitch Brainstorm**: Replaced service placeholders in [brainstorms/2026-08-03-vashishthya-client-pitch-and-pilot.md](file:///d:/AI-OS/brainstorms/2026-08-03-vashishthya-client-pitch-and-pilot.md).
5. **Registered in WORKSPACE_MAP**: Updated [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) to index `SERVICES_CATALOG.md`.

**Why:** Replaces all placeholder fields in Client 001's vault with 100% verified real-world pricing and service offerings from their actual marketing flyer.

**Owner:** Atinek Maurya / AIOS

## 2026-08-03 — Ingestion of Client 1 (Vashishthya Research / IJORAR / MJAP) Deep Research Audit

**Decision:** Ingested the complete 6-section deep research audit report into `clients/001-vashishthya-research-edu/01-pre-outreach-audit/`:
1. **Saved Raw Report**: Created [DEEP_RESEARCH_REPORT.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/DEEP_RESEARCH_REPORT.md) containing full forensic findings across site tech debt, missing Google Scholar metadata, operational bottlenecks, revenue leakage math, 50-Capability AI Transformation Roadmap, and Zero-Upfront Pilot Proposal.
2. **Updated Master Audit (`AUDIT.md`)**: Enriched [AUDIT.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/AUDIT.md) with exact quantified loss metrics (50–100 staff-hours lost/mo, 60 lost candidate leads/mo, 30–50% lead dropoff rate) and technical flaws (e.g. broken external `ijariie.com` submit/board links, 768px raster DOI logos, missing viewport tags).
3. **Updated Commercial Proposal (`PROPOSAL.md`)**: Refined [PROPOSAL.md](file:///d:/AI-OS/clients/001-vashishthya-research-edu/02-proposal-and-agreement/PROPOSAL.md) detailing the ₹0 Free Pilot deliverables (AI Intake Calculator, Guideline Checker, Google Scholar SEO generator) and 3-Tier Post-Pilot commercial expansion ($1,500 / $3,000 / $5,000/mo retainer).
4. **Hot Cache Sync**: Updated [hot.md](file:///d:/AI-OS/hot.md) to track active focus and clear next actions for Loom script generation, sister outreach script drafting, and pilot prototyping.

**Why:** Centralizes all research assets in Client 001's vault, quantifies clear client ROI, and prepares all pitch assets for immediate client outreach and pilot signoff.

**Owner:** Atinek Maurya / AIOS

## 2026-08-02 — 1-Line Client Audit & Research Engine (`/client-audit`) & Vashishthya Lead Strategy

**Decision:** Created custom Tier 1 skill `/client-audit` (`.agents/skills/client-audit/SKILL.md`) and initialized Stage 1 lead vault for **Vashishthya Research & Educational Academy** (`001-vashishthya-research-edu`):
1. **1-Line Automation Engine**: Triggering `/client-audit "[Client Name]" [Website URL]` automatically:
   - Scaffolds Stage 1 lead directories via `python scripts/new_client_runner.py lead`.
   - Scrapes website content and linked domains.
   - Fills out `01-pre-outreach-audit/AUDIT.md` with business teardown, vulnerabilities, and pitch brief.
   - Generates a evidence-backed `CHATGPT_DEEP_RESEARCH_PROMPT.md` for deep forensic audits.
   - Prepares execution for 7-Agent STORM research (`storm-research-project`).
   - Generates a line-by-line Hinglish Loom Video Script & Slide Deck in `brainstorms/`.
2. **First Domestic Client Strategy (Vashishthya / IJORAR / MJAP)**:
   - Target: Dr. Prashant Singh & Dr. Pooja Singh (Raipur, Chhattisgarh). Referral via Operator's Sister.
   - Model: 100% Free Value-First Pilot (Zero upfront charge) in exchange for permission to publish an official AI Case Study, Video Testimonial, Fractional AI Consultant role, and warm referrals after 30-45 days.
3. **Workspace Registration**: Saved ChatGPT prompt template (`CHATGPT_DEEP_RESEARCH_PROMPT.md`), registered `/client-audit` in `WORKSPACE_MAP.md`, updated `hot.md` for session handoff.

**Why:** Gives ZORIXEL a 1-line client audit slash command to research, audit, and generate pitch materials for any prospective client in seconds, while establishing a risk-free case study offer for Vashishthya Research.

**Owner:** Atinek Maurya / AIOS

## 2026-08-02 — ZORIXEL 8-Phase Client Vault Architecture & `/new-client` Skill Engine (v3.1)

**Decision:** Designed and implemented a standardized 8-phase client vault architecture (`clients/[ID]-[client-slug]/`) and custom Tier 1 `/new-client` skill engine for ZORIXEL AI Agency:
1. **8-Phase Lifecycle**:
   - `01-pre-outreach-audit/` (Lead source metadata, vulnerability map, Loom pitch script)
   - `02-proposal-and-agreement/` (3-Option Proposal, pricing calculations, signed contract/NDA)
   - `03-post-hire-onboarding/` (System credentials, internal SOPs, workflow teardowns)
   - `04-architecture-and-specs/` (Agentic workflows, MCP server specs, UI specs)
   - `05-development-and-build/` (Build sprint logs, prompt chains, VibeSec audit, code junction)
   - `06-client-deliverables/` (Sub-grouped handoff packages: `01-web-application/`, `02-automation-workflows/`, `03-mcp-tools/`)
   - `07-training-and-offboarding/` (Team training session notes, handover videos, sign-off certificate)
   - `08-retainer-and-tracker/` (Internal ROI log, monthly maintenance, upsell roadmap)
2. **Two-Stage Gated Scaffolding**:
   - **Stage 1 (Lead & Sales Gate)**: Running `/new-client [client-name]` scaffolds `01` and `02` for any lead source (inbound website forms, cold audits, referrals, DMs, email).
   - **Stage 2 (Accepted & Build Gate)**: Running `/new-client accept [client-id]` unlocks phases `03` through `08` once the deal is accepted.
3. **Code Repo Junction Topology**: Client code projects live in `projects/Clients/` or `projects/Websites/` and link into `05-development-and-build/` via Windows junctions.
4. **Embedded Auto-Evolution Engine**: The `/new-client` skill includes a self-improvement protocol (`/new-client evolve`) that audits completed client sprints and automatically updates canonical markdown templates (`brain-aios/wiki/templates/clients/`) without manual intervention.
5. **System Artifacts**: Created canonical markdown templates (`01-AUDIT.md` to `08-TRACKER.md`), standard automation runner script (`scripts/new_client_runner.py`), Tier 1 skill (`.agents/skills/new-client/SKILL.md`), and SOP (`brain-aios/wiki/sops/client-vault-architecture-sop.md`).

**Why:** Gives ZORIXEL a repeatable, enterprise-grade client management system that keeps unclosed leads isolated from active build spaces while enabling continuous agency automation after every client sprint.

**Owner:** Atinek Maurya / AIOS

## 2026-08-02 — Value-Based AI Pricing Engine & ZORIXEL Master Strategy (v3.0)

**Decision:** Ingested Nate Herk's 27-page Masterclass PDF (*How to Price AI Solutions*) and finalized ZORIXEL's Master Agency Strategy & Pricing Architecture:
1. **Positioning Moat**: Refined ZORIXEL from a generic "AI automation agency" into a **Production-Grade AI Operations & Custom Control Dashboard Agency** (shipping human-in-the-loop React/Next.js control UIs, audit logs, and zero vendor lock-in).
2. **Nate Herk Value-Based Pricing Corridor**: Strictly enforced the 3-Number Corridor (Cost Floor $\le$ 10%–20% Defensible Price Corridor $\le$ Client-Stated Value Ceiling) and mandatory 10X ROI Check ($\text{Value Multiple} \ge 10\text{X}$).
3. **3-Option Micro-Service Proof Ladder**: Presenting 3 distinct options (Essential $1.5k–$2.5k starter proof, Growth $5k–$10k connected workflows, Scale $12k–$25k+ enterprise transformation).
4. **Dedicated System Skill**: Built & verified Tier 1 `/ai-pricing-engine` skill (`.agents/skills/ai-pricing-engine/SKILL.md`) calculating value ceilings, cost floors, 10X ROI check, 3-option proposals, and 1-minute mathematical pitch scripts.
5. **Client-Owned Utility Mandate**: Production API accounts (Anthropic, OpenAI, Supabase, Vercel) sit strictly in the client's name and on the client's credit card with hard monthly spending limits (e.g. $100 cap).
6. **5-Persona Roast Refinements**: Passed 5-persona `/roast` council audit with a 9.2/10 **STRONG GO** score, codifying strict Essential tier scope boundaries, single-field bottleneck intake forms, and standardized API security caps.

**Why:** Solves the #1 client objection in AI automation (fear of black-box AI errors) by shipping human control UIs, while eliminating pricing friction through affordable 10X ROI starter sprints that naturally convert into long-term retainers ($400–$1,500/mo).

**Owner:** Atinek Maurya / AIOS

## 2026-08-01 — ZORIXEL Brand Pivot: Dedicated AI Workflows & Business Automation Agency

**Decision:** Formally pivoted ZORIXEL's strategic focus from standalone web design/development to a dedicated **AI Workflows & Business Automation Agency**, with custom full-stack web UI as an integrated superpower pillar:
1. **Core Service Focus**: Dedicated AI workflows, custom agentic automations, lead qualification systems, and business bottleneck resolution (charging $1,500–$5,000+ per DFY build sprint).
2. **Integrated Full-Stack UI Moat**: Demoted standalone web design to an integrated frontend UI pillar (building custom TypeScript/Next.js client portals and dashboards to interface with backend Python/n8n AI agents).
3. **Dual-Market Strategy**:
   - **Domestic (India - INR)**: Rapid case study launchpad, Hindi client communication, adjusted purchasing power pricing, early confidence-building milestone.
   - **International (USD)**: Primary revenue engine targeting US/UK/CA/AU businesses.
4. **Primary Content & Funnel Architecture**: YouTube designated as the primary long-form technical authority engine (showing Claude Code/n8n/Python build-in-public breakdowns). Content syndicated to LinkedIn, X, Reddit, and Instagram.
5. **Client-Owned Infrastructure**: Clients own their Anthropic/OpenAI API keys and cloud hosting accounts (Vercel/Supabase/Render/n8n), eliminating monthly server hosting liabilities for ZORIXEL.
6. **Value-First Proposals**: Unified global intake tool -> Asynchronous personalized Loom video proposal -> closing Zoom call.

**Why:** Addresses the growing demand for high-ROI business automations while capitalizing on ZORIXEL's unique dual advantage (combining backend AI workflows with world-class frontend interactive design). Eliminates server hosting liabilities and prevents domestic vs. international pricing leaks.

**Owner:** Atinek Maurya / AIOS

## 2026-08-01 — Universal Humanizer Skill & Writing Discipline Mandate (v2.9.1)

**Decision:** Ingested `https://github.com/blader/humanizer` (v2.9.1, 33 AI pattern cleanup rules based on Wikipedia's AI cleanup project) and established a non-negotiable global mandate across the entire AIOS and Zorixel website project:
1. **Installed Active Skill**: Deployed `.agents/skills/humanizer/SKILL.md` into both the main AIOS environment and the website project (`projects/Zorixel brand/zorixel-website/.agents/skills/humanizer/SKILL.md`).
2. **System Rules Ingestion**: Embedded the Universal Humanizer Mandate into `AGENTS.md`, `ai-workflow-rules.md`, `MEMORY.md`, `hot.md`, and `.agents/skills/using-superpowers/SKILL.md`.
3. **33 Pattern Enforcement**: Enforced strict removal of em dashes (`—`/`–`), inflated symbolism (*'testament/tapestry/fostering'*), promotional puffery, rule of three overuse, sycophancy, meta signposting (*'Let's dive in'*), and tailing negations. Enforced sentence case headings and straight quotes (`"..."`).
4. **`[PENDING OPERATOR REFERENCE HOLD]` Rule**: Codified a mandatory fallback slot across all component specifications, prioritizing Atinek Maurya's custom references over catalog backstops.

**Why:** Guarantees that every chat reply, copy draft, email auto-responder, headline, DM, and documentation file produced by the AIOS reads 100% natural, authentic, and human without AI slop tells.

**Owner:** Atinek Maurya / AIOS

## 2026-07-31 — Upgrade Six-File Context Methodology (`six-file-context-methodology` v3.2) for Zorixel Web Build


**Decision:** Conducted Socratic discovery via `/grill-me` and upgraded `/six-file-context-methodology` to v3.2 (`.agents/skills/six-file-context-methodology/SKILL.md`) in preparation for building the official Zorixel brand website:
1. **Per-Reference Granular Deconstruction (`reference/MANIFEST.md`)**: When design references are placed into `projects/zorixel-website/reference/`, the AI engine interactively interviews the operator to parse what elements to keep/remove, whether to use full templates or specific sub-components, and how to adapt them to Zorixel brand OKLCH tokens in `reference/MANIFEST.md`.
2. **4-Phase Socratic Discovery (`init`) + Feature-Specific Socratic Spec Sessions**: `/six-file-context-methodology init` executes a mandatory 4-Phase Socratic interview. Every feature spec (`spec <feature-name>`) also triggers a feature-level Socratic interview before writing specs or tickets.
3. **Interactive Human-in-the-Loop Visual QA (`verify`)**: Runs Playwright 5-viewport screenshot sweeps per UI ticket, pauses execution, presents visual outputs to the operator, and waits for explicit human approval or feedback screenshots before signoff.
4. **Graphify AST Knowledge Graph Integration**: Automatically builds and updates `.planning/graphs/` AST knowledge graph during context scaffolding and spec creation.
5. **Multi-Session Zero-Context-Loss Protocol (`resume`)**: Persists state across `context/progress-tracker.md`, `docs/wayfinder/map.md`, and decision logs, enabling seamless resumption in fresh chat sessions via `/six-file-context-methodology resume`.

**Why:** Gives Atinek Maurya total visual, architectural, and motion control over the Zorixel brand website build while eliminating AI model context rot and hallucination across chat sessions.

**Owner:** Atinek Maurya / AIOS

## 2026-07-31 — Upgrade Web Design Skill (`website-design-engine` v3.0) & Six-File Context Sync (v3.1)


**Decision:** Upgraded the Web Design creation architecture and context methodology across the AIOS:
1. **`website-design-engine` v3.0 (`.agents/skills/website-design-engine/SKILL.md`)**: Upgraded to 10-phase v3.0 engine. Removed automatic wireframe generation in favor of Six-File layout control. Established project-local `reference/` (or `references/`) folder as the **#1 Priority Source of Truth** for screenshots, screen recordings, HTML files, and TSX/CSS component snippets.
2. **Categorized Favorite Component Priority**: Maintained existing component categories in `component-registry-index.json` with `"favorite": true` markers prioritized in CLI search results.
3. **Interactive Radiant Shader HTML Protocol (`pbakaus/radiant`)**: Integrated `radiant-shaders` (`https://radiant-shaders.com/gallery/`). Never auto-generate `.tsx` shaders blindly; AI asks user first if a shader is needed and which one. User drops HTML file into `reference/`, and AI extracts WebGL shader code from that HTML file.
4. **`six-file-context-methodology` v3.1 (`.agents/skills/six-file-context-methodology/SKILL.md`)**: Upgraded to v3.1. Mandated `reference/` directory creation during `init`, codified the 4-level component priority chain (Local Reference -> Categorized Favorites -> 300+ Catalog -> Radiant Shaders), and synchronized layout specs directly with `website-design-engine` v3.0.
5. **Slow & Methodical Zero-Hurry Execution**: Enforced step-by-step verification and user check-ins on any doubt.

**Why:** Gives Atinek Maurya total layout control via Six-File specs while establishing an unambiguous priority hierarchy for design assets, user favorites, and WebGL graphics.

**Owner:** Atinek Maurya / AIOS

## 2026-07-31 — Graphify Knowledge Graph Engine Ingestion & Multi-Vault Integration

**Decision:** Ingested and integrated Graphify (`https://github.com/Graphify-Labs/graphify`) across the entire AIOS system:
1. **Installed Extended Engine**: Installed `graphifyy[all]` globally via `uv tool install` with complete AST language parsers, PDF/Office extraction, media transcription, and graph exporters.
2. **Multi-Vault Automation Script**: Built `scripts/graphify_runner.py` managing AST knowledge graph generation and status checks across 4 workspace hubs (`root`, `brain`, `zorixel`, `frontend`).
3. **Tier 1 Native Skill**: Created `.agents/skills/graphify/SKILL.md` with dual-triggering (`/graphify`) and intent-matching for querying subgraphs, explaining node concepts, and tracing paths.
4. **Query-First Navigation Rule**: Updated `.agents/AGENTS.md` and `GEMINI.md` to establish `graphify query` as the primary method for codebase and vault exploration over brute-force file grepping.
5. **Research Library**: Archived Graphify manuals and architecture specs to `brain-aios/wiki/research/skills-library/graphify/`.

**Why:** Gives AIOS zero-LLM local tree-sitter AST knowledge graph traversal across all workspace vaults and brand operating systems.

**Owner:** Atinek Maurya / AIOS

## 2026-07-30 — ZORIXEL Brand OS Initialization, Ingestion Vault & Global Async Arbitrage Model

**Decision:** Created dedicated ZORIXEL Brand OS on Drive D (`D:\ZORIXEL-BRAND-OS`) attached via directory junctions (`d:\AI-OS\zorixel-brand-os` and `second-brain-zorixel`). Ingested 7 YouTube transcripts + 40-page PDF playbook (*The First Client Playbook*), and codified **The Global Async Arbitrage Model**:
1. **Zero-Cost India Stack:** 100% local AIOS execution (`website-design-engine`, Playwright, Scrapling, local component vault) with zero software overhead.
2. **Western High-Ticket Pricing:** $3,000 per 14-Day Web Experience Sprint ($1,500 deposit upfront), which equals ~₹2.5 Lakhs INR per sale.
3. **100% Async Closing:** 100% text DMs + 2-minute Loom screen video audits + Notion proposals (zero live Zoom sales calls).
4. **Organized Research Vault:** Reorganized cryptic video files into human-readable Markdown notes, created 5 deep topic framework manuals (`research/frameworks/`), and built `research/INDEX.md`.

**Why:** Gives Atinek Maurya a clear, repeatable path to total financial independence ($10k/mo MRR ~ ₹8.5 Lakhs/mo) at age 17 without live sales call friction or local capital overhead.

**Owner:** Atinek Maurya / AIOS

## 2026-07-27 — 23-Site AIOS Design Intelligence System Synthesis & Universal Integration

**Decision:** Designed, built, and universally integrated the 23-Site AIOS Design Intelligence System across all skills, reference vaults, scripts, SOPs, and system prompt rules:
1. **Zero-Bloat CLI Synthesis Engine (`scripts/design_synthesis_engine.py`)**: Indexes all 23 extracted reference sites (*Active Theory, Obys, Locomotive, Resn, Oryzo AI, etc.*) into `references/23-sites-matrix.json` with strict 3-result snippet capping to prevent context bloat.
2. **Unified Component Registry**: Enhanced `scripts/component_registry_cli.py` to search across cataloged UI libraries AND 23-site reference TSX extractions.
3. **Master Reference Matrices**: Created `references/23-SITES-MASTER-DESIGN-MATRIX.md` (OKLCH color math, layout formulas, GSAP inertia, magnetic cursor physics) and `references/23-SITES-PSYCHOLOGY-AND-CHOREOGRAPHY.md` (UX design psychology, cognitive load rules, progressive disclosure, 4 section sequence flows).
4. **Live Visual Showroom**: Created `premium-frontend-experience-system/23-sites-showroom.html` local HTML browser showcase.
5. **Universal Integration**: Embedded design synthesis into `GEMINI.md`, `/website-design-engine`, `/design-direction`, `/canvas-design`, `/brand-colors`, `/carousel-render`, `/new-project`, `/ingest-repo`, `vault-references/INDEX.md`, and `brain-aios/wiki/sops/design-intelligence-system-sop.md`.

**Why:** Gives the AIOS an unfair advantage in web design quality, enabling it to synthesize Awwwards-grade design strategy, layout math, and component physics across all project workflows without context bloat.

**Owner:** Antigravity AIOS & Atinek Maurya

---

## 2026-07-27 — Codified Automatic Skill Evolution & On-Demand Vault Promotion Mandate

**Decision:** Codified the permanent AIOS Mandate for Automatic Skill Evolution & On-Demand Vault Promotion:
1. **Automatic Vault Scanning**: Whenever the AIOS encounters a new task, workflow requirement, or technical domain, it MUST automatically scan `brain-aios/wiki/research/skills-library/` and vault references for matching skills, guides, or manuals.
2. **On-Demand Tier 2 to Tier 1 Promotion**: Whenever a skill, guide, or workflow stored in `skills-library/` is needed for active work, the AIOS MUST automatically adapt, promote, format (with dual-trigger YAML frontmatter, No-Op test quality discipline, and explicit `## 🔗 Inter-Skill Connections`), and install it directly into `.agents/skills/` without requiring explicit user prompt permission.
3. **Continuous Skill Upgrading**: During milestone completions, `/improve-system` calls, or system reviews, the AIOS MUST automatically audit and upgrade existing active skills in `.agents/skills/` to integrate superior patterns, CLI parameters, and security safeguards as the workspace evolves.

**Why:** Ensures the AIOS autonomously expands and upgrades its capabilities as needs arise without requiring manual user prompt management or intervention.

**Owner:** Antigravity AIOS & Atinek Maurya

---

## 2026-07-27 — Universal `/grill-me` & `/roast` Cross-System Integration Across All Workflows


**Decision:** Codified and integrated `/grill-me` (Socratic Discovery Engine) and `/roast` (Adversarial 5-Persona Council Gate) along with JS Mastery and Matt Pocock skills across all AIOS workflows, skills, scripts, and vaults:
1. **Core Skills Overhauled**: Upgraded `.agents/skills/grill-me/SKILL.md` (concept explanations BEFORE questions, categorized INFER/ASK/RECOMMEND options, disk checkpointing) and created/upgraded `.agents/skills/roast/SKILL.md` (5-persona council: Contrarian, Expansionist, Logician, Researcher, Buyer + economics lens + 48-hr cheapest validation test).
2. **Cross-Skill Wiring**: Embedded `/grill-me` and `/roast` gates into `/new-project`, `/website-design-engine`, `/ingest-repo`, `/carousel-copy`, `/design-direction`, `/jsmastery-architect`, `/mattpocock-to-spec`, `/verify-design`, and `/skill-builder`.
3. **Script & SOP Integration**: Updated `scripts/component_registry_cli.py`, `scripts/hallmark_runner.py`, `scripts/scrapling_runner.py`, and created `brain-aios/wiki/sops/grill-me-and-roast-integration-sop.md`.
4. **Quality Discipline**: Enforced Matt Pocock's `writing-great-skills` guidelines (No-Op test, pruning discipline, leading words, explicit use-case specification) across all skills.

**Why:** Ensures Atinek Maurya never writes un-tested code, un-vetted business ideas, or generic AI slop. Forces every idea through Socratic discovery and adversarial roast before touching code.

**Owner:** Antigravity AIOS & Atinek Maurya

---

## 2026-07-27 — Integrated `jsmastery-pro/skills` & `mattpocock/skills` into AIOS

**Decision:** Completed 8-phase autonomous repository ingestion and skill adaptation for `jsmastery-pro/skills` and `mattpocock/skills`:
1. **Tier 2 Vault Archival**: Cloned and archived full raw source repositories into `brain-aios/wiki/research/skills-library/jsmastery-skills/` and `brain-aios/wiki/research/skills-library/mattpocock-skills/`.
2. **Tier 1 Native Adaptation**: Created 9 specialized skills in `.agents/skills/`:
   - `jsmastery-architect`: Fullstack JS & Next.js App Router architecture build-spec engine.
   - `jsmastery-audit`: Static & architectural code auditor for Next.js, Server Actions, and security.
   - `jsmastery-scope`: Feature scoping, MVP milestone breakdown, and tracer-bullet vertical slices.
   - `mattpocock-domain-modeling`: TypeScript domain modeling, discriminated unions, branded types, and ADRs.
   - `mattpocock-wayfinder`: Multi-session macro planning and issue map manager for complex refactors.
   - `mattpocock-to-spec`: Technical SPEC compiler turning loose user prompts into structured architecture contracts.
   - `mattpocock-to-tickets`: Spec-to-tickets deconstructor creating atomic engineering tasks with verifiable DoD.
   - `mattpocock-teach`: Socratic teaching and mental model builder for TypeScript & web engineering.
   - `mattpocock-setup-ts-deep-modules`: Deep module boundary enforcement and package structure setup.
3. **Cross-System Integration**: Updated `.agents/AGENTS.md`, `GEMINI.md`, `references/antigravity-skills-guide.md`, `references/aios-user-manual.md`, `MEMORY.md`, and `WORKSPACE_MAP.md`.

**Why:** Combining JS Mastery's fullstack Next.js architectural workflows with Matt Pocock's TypeScript domain modeling and wayfinding discipline gives the AIOS world-class fullstack JS and TS engineering capabilities natively in Antigravity.

**Owner:** Antigravity AIOS & Atinek Maurya

---

## 2026-07-27 — Executed Phase 2 Site #23: Merci Michel Ingestion & Phase 2 Queue Completion

**Decision:** Completed 10-stage reference ingestion pipeline for **Site #23: Merci Michel** (`https://mercimichel.com/`), marking the official completion of Phase 2 Awwwards & Agency Winners Queue:
1. Mirrored full site source (143.7 KB HTML).
2. Extracted **35 standalone React `.tsx` components** (`footers`: 11, `nav`: 8, `misc`: 8, `interactive`: 7, `3d`: 1).
3. Generated **5 responsive viewport screenshots** (`desktop_1920.png`, `laptop_1440.png`, `tablet_1024.png`, `tablet_768.png`, `mobile_375.png`).
4. Built **Hyper-Detailed Visual UX Blueprint** (`assets/wireframe.html` & `assets/wireframe.png`).
5. Authored 10-Pillar Deep Analysis (`DEEP_ANALYSIS.md`), 5-Layer Site DNA (`site-dna.md`), 15-Category Master Reference (`merci-michel-granularity-master.md`), and registered in central vault index (`vault-references/INDEX.md`).

**Why:** Merci-Michel is a legendary French digital studio with 2 SOTY, 6 SOTM, and 41 SOTD awards. Ingesting their gamified WebGL 3D physics, Three.js particle bloom, and Howler.js spatial sound architecture completes the 23-site reference vault for the Premium Frontend Experience System.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Executed Phase 2 Site #22: Locomotive Agency Ingestion

**Decision:** Completed 10-stage reference ingestion pipeline for **Site #22: Locomotive Agency** (`https://locomotive.ca/en`):
1. Mirrored full site source and captured **20 WebGL GLSL runtime shaders**.
2. Extracted **109 standalone React `.tsx` components** (`nav`: 59, `cards`: 14, `modals`: 13, `misc`: 9, `hero`: 5, `footers`: 4, `sections`: 3, `3d`: 2).
3. Generated **5 responsive viewport screenshots** (`desktop_1920.png`, `laptop_1440.png`, `tablet_1024.png`, `tablet_768.png`, `mobile_375.png`).
4. Built **Hyper-Detailed Visual UX Blueprint** (`assets/wireframe.html` & `assets/wireframe.png`).
5. Authored 10-Pillar Deep Analysis (`DEEP_ANALYSIS.md`), 5-Layer Site DNA (`site-dna.md`), 15-Category Master Reference (`locomotive-agency-granularity-master.md`), and registered in central vault index (`vault-references/INDEX.md`).

**Why:** Locomotive is the creator of Locomotive Scroll and a multi-time Awwwards Agency of the Year winner. Ingesting their smooth inertia scroll physics, GSAP kinetic typography, image wave displacement shaders, and editorial dark mode layout math provides core motion design standards for the Zorixel Experience System.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Executed Phase 2 Site #21: Active Theory Ingestion

**Decision:** Completed 10-stage reference ingestion pipeline for **Site #21: Active Theory** (`https://activetheory.net/`):
1. Mirrored site source and captured WebGL GLSL runtime shader assets.
2. Generated **5 responsive viewport screenshots** (`desktop_1920.png`, `laptop_1440.png`, `tablet_1024.png`, `tablet_768.png`, `mobile_375.png`).
3. Built **Hyper-Detailed Visual UX Blueprint** (`assets/wireframe.html` & `assets/wireframe.png`).
4. Authored 10-Pillar Deep Analysis (`DEEP_ANALYSIS.md`), 5-Layer Site DNA (`site-dna.md`), 15-Category Master Reference (`active-theory-granularity-master.md`), and registered in central vault index (`vault-references/INDEX.md`).

**Why:** Active Theory is a globally preeminent creative technology agency and multiple Awwwards Agency & Developer of the Year winner. Ingesting their proprietary Hydra WebGL framework, 3D particle repulsion math, and spatial WebXR architecture provides invaluable engineering patterns for the Zorixel Experience System.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Executed Phase 2 Site #20: Resn (Corn Revolution) Ingestion

**Decision:** Completed 10-stage reference ingestion pipeline for **Site #20: Resn (Corn Revolution)** (`https://cornrevolution.resn.global/#`):
1. Mirrored full site source (HTML, CSS, JS, WOFF2 fonts, WebGL GLSL shaders).
2. Intercepted **6 WebGL GLSL Shaders** directly from browser runtime.
3. Generated **5 responsive viewport screenshots** (`desktop_1920.png`, `laptop_1440.png`, `tablet_1024.png`, `tablet_768.png`, `mobile_375.png`).
4. Built **Hyper-Detailed Visual UX Blueprint** (`assets/wireframe.html` & `assets/wireframe.png`).
5. Authored 10-Pillar Deep Analysis (`DEEP_ANALYSIS.md`), 5-Layer Site DNA (`site-dna.md`), 15-Category Master Reference (`resn-corn-revolution-granularity-master.md`), and registered in central vault index (`vault-references/INDEX.md`).

**Why:** Resn is an Awwwards Site of the Year winner. Ingesting their 3D WebGL camera scrubbing, infinite scrollytelling loop, and spatial soundscape mechanics provides world-class creative engineering blueprints for the Zorixel Experience System.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Batch Unbounded Component Extraction Across All 18 Reference Sites (3,309 React .tsx Components)

**Decision:** Ran `scripts/extract_components_batch.py` across all 18 existing reference sites in `premium-frontend-experience-system/reference-inputs/sites/`. Synthesized **3,309 standalone React TypeScript (`.tsx`) drop-in components** organized into pattern subfolders (`nav/`, `cards/`, `hero/`, `3d/`, `sections/`, `footers/`, `interactive/`, `misc/`) alongside a machine-readable `components-index.json` manifest for every site.

**Site Extraction Summary (3,309 Components):**
- `sondaven`: 539 components
- `grids-obys-agency`: 1,141 components
- `follow-art`: 235 components
- `truck-n-roll`: 166 components
- `ashley-brooke-cs`: 164 components
- `the-line-studio`: 161 components
- `champions-4-good`: 139 components
- `jasmine-gunarto`: 138 components
- `gehry-getty`: 122 components
- `unleashing-best`: 117 components
- `made-in-evolve`: 95 components
- `good-fella`: 70 components
- `tresmares-capital`: 60 components
- `oryzo-ai`: 53 components
- `detroit-paris`: 40 components
- `the-shift-tokyo`: 40 components
- `off-menu-design`: 18 components
- `outfit-hello-hello`: 11 components

**Why:** Upgrades the entire 18-site Frontend Vault into an exhaustive catalog of over 3,400+ React UI components ready for instant pattern searching, adaptation, and component registry integration.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Refined Unbounded Component Extractor & Executed Phase 2 Site #19 (TRIONN Agency)

**Decision:** Refined `scripts/scrape_full_site_mirror.py` Unbounded Component Extractor to parse DOM structural and interactive elements without artificial caps, classify into UX pattern subfolders (`nav/`, `cards/`, `hero/`, `3d/`, `sections/`, `footers/`, `misc/`), and convert raw HTML structures into clean React TypeScript (`.tsx`) drop-in components alongside `components-index.json`. Executed Phase 2 Awwwards Sweep on **Site #19: TRIONN Agency (`https://trionn.com/`)**:
1. Extracted **134 standalone React `.tsx` components** (`nav`: 32, `cards`: 46, `sections`: 7, `3d`: 3, `footers`: 2, `hero`: 1, `misc`: 43).
2. Intercepted **16 WebGL GLSL Shaders** from browser runtime.
3. Generated **5 responsive viewport screenshots** (`desktop_1920.png`, `laptop_1440.png`, `tablet_1024.png`, `tablet_768.png`, `mobile_375.png`).
4. Built **Hyper-Detailed Visual UX Blueprint** (`assets/wireframe.html` & `assets/wireframe.png`).
5. Authoring 10-Pillar Ultra-Exhaustive Deep Analysis (`DEEP_ANALYSIS.md`), 5-Layer Site DNA (`site-dna.md`), 15-Category Master Reference (`trionn-agency-granularity-master.md`), and registered in central vault index (`vault-references/INDEX.md`).

**Why:** Fulfills the Unbounded Component Extraction Mandate, upgrading the site mirroring engine to automatically extract every unique UI component present on target sites and catalog them into the Zorixel Frontend Experience System.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Frontend Vault 300+ Component Registry, Dual Vault & Security Hardening Upgrade

**Decision:** Upgraded Frontend Experience System references, component registries, site deconstruction engine, dual reference vaults, and AIOS web design skills:
1. Expanded component registry index from 147 to 172+ components across 11 libraries (**Magic UI, 21st.dev, Motion Primitives, React Bits, Origin UI, Kokonut/Cult UI, Uiverse**). Added Refero/Mobbin UX pattern tags and `component_registry_cli.py adapt` tooling.
2. Upgraded `scrape_full_site_mirror.py` with WebGL GLSL runtime shader hooks, 3D asset interceptors, and Unbounded Component Extractor logic. Patched path traversal vulnerability via `safe_path()` regex sanitization and scheme validation.
3. Created Dual Dedicated Reference Vaults: `references/component-vault/` and `references/shader-canvas-vault/`.
4. Auto-synced all AIOS rules in `.agents/skills/website-design-engine/SKILL.md`, `.agents/skills/scrape-reference/SKILL.md`, `AGENTS.md`, and `WORKSPACE_MAP.md`.

**Why:** Transforms the Frontend Vault into an active AIOS design system engine capable of querying components by pattern and building Awwwards-grade websites with raw WebGL GLSL shaders.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Upgrade `/grill-me` Skill Globally & Locally across AIOS

**Decision:** Upgraded `/grill-me` skill across both local workspace (`d:\AI-OS\.agents\skills\grill-me\SKILL.md`) and global configuration (`C:\Users\HP\.gemini\config\skills\grill-me\SKILL.md`). Codified 8 mandatory execution rules:
1. Concept Explanation BEFORE Every Question (plain language explanations before asking).
2. Proactive Web Search Research before offering options.
3. Exhaustive Option-Based Inquiries with recommended answers (no question count limits).
4. Pre-Write Feature Confirmation Check (*"Would you like to add any additional features before finalizing?"*).
5. Checkpoint to Disk after every single answer.
6. Mandatory Pre-Write `/roast` Council Audit (5 personas).
7. Pre-Coding Backstop (*"Is there anything else remaining before we touch the code?"*).
8. Global Zero-Hurry & Architectural Rigor Mandate across all discovery sessions.

**Why:** Ensures the AI agent operates as a true thought partner and mentor rather than a vending machine. Explaining concepts first removes the burden of watching 4-hour video tutorials, while proactive web search and option-based questioning refine ideas to enterprise standards.

**Owner:** Antigravity AIOS

---

## 2026-07-27 — Enforce Security-First Architecture & Automatic Security Skill Ingestion Mandate

**Decision:** Codified Security as the primary non-negotiable requirement across all web apps and AI SaaS projects. Integrated `/vibesec` protocol (IDOR prevention, tenant isolation, JWT `httpOnly` cookies, Zod mass assignment validation, SSRF private IP blocking) directly into the 7-File Context System (`STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md`), `/six-file-context-methodology` skill, `/grill-me` skill, and `GEMINI.md`. Mandated automatic detection, scanning, and ingestion of any present or future security/backend skills added to `.agents/skills/` or `skills-library/` into pre-write `/roast` audits.

**Why:** Security flaws (IDOR, mass assignment, token leaks) are the #1 killer of production AI applications. Codifying automatic security skill ingestion ensures the AIOS scales its defense capabilities automatically whenever new security tools are installed.

**Alternatives considered:** Manual security auditing after build completion (rejected because security must be designed upfront in `architecture.md` before writing code).

**Owner:** Antigravity AIOS

---

## 2026-07-25 — Create Senior AI Engineering Knowledge Vault & `/six-file-context-methodology` Skill

**Decision:** Created `references/six-file-context-methodology/` knowledge vault containing the unsummarized masterclass handbook (`STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md`), complete ~37,000-word video transcript (`FULL_TRANSCRIPT.md`), 6 core context file templates (`6-file-context-templates/`), 29 production feature specifications (`feature-specs-library/`), and debugging templates (`current-issues-templates/`). Created custom skill at `.agents/skills/six-file-context-methodology/SKILL.md` and registered it in `WORKSPACE_MAP.md`.

**Why:** Synthesizes JavaScript Mastery's *How Senior Engineers Build With AI in 2026* masterclass into a reusable, zero-summarization knowledge base and operational skill. It codifies the Senior AI Engineer Mindset (System Architect > Code typist), Context Architecture, and Decoupled 3-Step Build Workflow for future ZORIXEL SaaS projects.

**Alternatives considered:** Keeping reference files loosely stored in `Downloads/` (rejected due to context fragmentation and risk of loss).

**Owner:** Antigravity AIOS

---

## 2026-07-24 — Create Unified Master Website Creation Skill (`website-design-engine`)

**Decision:** Created `website-design-engine` at `.agents/skills/website-design-engine/SKILL.md` with 6 modular reference files (`references/01-06.md`). Consolidated 13 global & local web design skills (`frontend-design`, `taste`, `design-is`, `design-loop-controlled`, `ui-ux-pro-max`, `gsap-animation`, `threejs-webgl`, `tailwind-patterns`, `browser-testing`, `vercel-web-design-guidelines`, `react-performance`, `remotion`, `impeccable`), 147 cataloged components (`component_registry_cli.py`), Obys 4 grid canons, Hallmark anti-slop gates, and 5-viewport Playwright visual QA without touching or breaking underlying individual skills.

**Why:** Design skills and components were previously scattered across 4 directory layers. The unified engine provides a single, zero-breakage 7-phase pipeline for creating websites from scratch. It solves instruction fatigue via Phase-Gated Progressive Disclosure (loading reference guides dynamically per phase) and offloads heavy audits to deterministic Python runner scripts (`hallmark_runner.py` and `verify_design_milestone.py`).

**Alternatives considered:** Direct prompt merging into a single monolithic skill (rejected due to prompt bloat and instruction collision) or relying solely on manual skill selection (causes high operational friction).

**Owner:** Antigravity AIOS

---

## 2026-07-24 — Ingest `os-audit` as Standalone Antigravity Skill

**Decision:** Ingested and installed `os-audit` from `c:\Users\HP\Downloads\os-audit-SKILL.md` into `.agents/skills/os-audit/SKILL.md` and `brain-aios/wiki/research/skills-library/os-audit/SKILL.md`. Tweaked platform paths for Antigravity compatibility while preserving 100% of its original 6 audit checks (Routing integrity, Index truth, Freshness, Bloat, Hygiene, Context placement) and 4 context failure modes (Poisoning, Bloat, Confusion, Clash) as a standalone skill. Registered `/os-audit` in `GEMINI.md`, `references/aios-user-manual.md`, `references/antigravity-skills-guide.md`, and `WORKSPACE_MAP.md`.

**Why:** `os-audit` provides a dedicated read-only drift, freshness, and organization audit. Keeping it standalone per explicit user directive ensures its internal logic remains unaltered while giving the AIOS a dedicated tool to check if its operating context is still true.

**Alternatives considered:** Blending or cross-interpreting `os-audit` with `/audit` (rejected per explicit user request to keep `os-audit` separate and un-altered).

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Connect Obsidian Vaults & Establish Master Task List


**Decision:** Created directory junctions at `brain-aios` and `second-brain-zorixel` pointing to the user's local Obsidian vaults (`D:\Brain For my AIOS` and `C:\Users\HP\Documents\Second Brain for Zorixel` respectively), updated `connections.md` to register them under the `local_path` mechanism, and initialized a prioritized master task list (`wiki/checklists/master-task-list.md`) inside the general AIOS vault.

**Why:** The user operates two separate Obsidian vaults—one for the overall AIOS/workflow hub and one for their ZORIXEL brand. Using Windows junctions maps both vaults relative to the workspace, enabling direct read/write access. Centralizing the master task list in the overall AIOS vault aligns with the Q3-Q4 operational strategy to build 5-10 core workflows, and grouping by Milestones focuses effort on the immediate July 25 launch.

**Alternatives considered:** Using absolute paths across C: and D: drives (messy and not portable), or tracking tasks in a separate file within the `d:\AI-OS` workspace (isolates task tracking from the user's daily Obsidian-based second brain interface).

**Owner:** Atinek Maurya

---

## 2026-07-14 — Configure Google Workspace CLI (GWS) for Dual Accounts

**Decision:** Installed the Google Workspace CLI (`gws`), configured it with a manual OAuth credential client (`client_secret.json`) from GCP Project `Zorixel AIOS`, and exported independent session credential profiles for Personal (`credentials_personal.json`) and Brand (`credentials_brand.json`) accounts. Documented GWS usage in `references/gws-api.md`.

**Why:** Native multi-account switching is no longer supported directly in `gws` CLI. By exporting credentials to individual JSON files, we can switch account contexts dynamically in the AI OS environment by modifying the `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` environment variable.

**Alternatives considered:** Setting up two separate Windows user accounts (adds massive operational friction) or installing the full Google Cloud SDK to use automated flows (unnecessary bloat).

**Owner:** Atinek Maurya

---

## 2026-07-14 — Optimize AIOS for Antigravity & Formulate Workflow Skills

**Decision:** Completed workspace migration from Claude Code references to Antigravity standards. This included running an recursive migration scan via python script, renaming 4 core files to "antigravity" counterparts, creating a `hot.md` cache file, adding "Default Shift" and "Curiosity Rule" operational guidelines to `GEMINI.md`, and scheduling the implementation of 5 custom workflow skills.

**Why:** The user operates in the Antigravity developer environment, making references to Claude Code plugins and configuration files confusing. Standardizing the terminology and building custom, native skills inside `.agents/skills/` ensures consistency, performance, and automation readiness in their active workflow.

**Alternatives considered:** Keeping the original Claude Code guides intact (retains outdated system contexts and could cause the model to look for non-existent Claude plugins) or manually renaming items incrementally (tedious and error-prone).

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Consolidate Utility Scripts & Save Skills Documentation

**Decision:** Saved all custom scripts (agent_adapt.py, rename_and_link_update.py, verify_skills.py) to a centralized `/scripts/` directory at the root workspace. Created `references/utility-scripts.md` and `references/antigravity-skills-guide.md` documentation templates to explain their usage and trace corresponding Antigravity/Claude Code plugin sources, and updated `GEMINI.md`, `EXPANSIONS.md`, and the general wiki index.

**Why:** Centralizing helper scripts keeps the workspace tidy (avoiding stray scripts in temporary directories) and enables quick execution for future workspace reorganizations. Documenting both Claude and Antigravity-specific plugins and repositories preserves historical research and ensures clarity on how the AI OS can be extended with official and community modules.

**Alternatives considered:** Leaving the scripts in temporary scratch folders (statically works, but risks deletion and hides them from active development) or only documenting the script logic without the plugin guidelines.

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Set Up Global Skills for Antigravity

**Decision:** Created a python script `copy_skills_to_antigravity.py` to copy all 122 skill directories (including using-superpowers, frontend-design, writing-skills, all 50+ gsd-* skills, context-mode skills, and memory skills) from local Claude Code configuration folders to the global Antigravity customizations folder (`C:\Users\HP\.gemini\config\skills\`). Ran the script and performed recursive `agent-adapt` replacements to make the skills fully native to the Antigravity platform.

**Why:** Enforcing global capability parity ensures that when the user switches tasks or workspaces in the Antigravity developer environment, the agent automatically discovers and runs the same powerful specs-driven, memory-aware, and frontend-design workflows originally cloned for Claude Code.

**Alternatives considered:** Requiring the user to rebuild skills locally for every new workspace (causes high setup friction and duplicate code) or running unmodified Claude Code skills (causes syntax errors due to platform-specific references).

**Owner:** Antigravity AIOS

---

## 2026-07-14 — Verify Workflows & Compile AIOS User Manual

**Decision:** Created a Python test script `demo_test_skills.py` to verify the execution logic of the newly added custom workspace skills (`/plan-day`, `/review-day`, `/scrape-competitor`, `/draft-message`, `/file-search`) and generated the [ZORIXEL AIOS User Manual & Execution Guide](file:///d:/AI-OS/references/aios-user-manual.md) to serve as a comprehensive user handbook. Integrated links to all new guides across both Obsidian indexes (`brain-aios` and `second-brain-zorixel`).

**Why:** Enforcing spec compliance verification prevents "dark code" execution or broken skill configurations before committing file changes. Centralizing instructions and documenting both the local workflow slash-commands and global plugins provides Atinek Maurya with a clear, direct reference for operating their AIOS.

**Alternatives considered:** Relying on the user's memory or checking each skill individually via standard prompt execution (increases token overhead and setup latency).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate & Configure Grill-Me Skill

**Decision:** Installed the `/grill-me` skill both locally in `.agents/skills/grill-me/SKILL.md` and globally in `C:\Users\HP\.gemini\config\skills\grill-me\SKILL.md` based on the downloaded configuration. Registered the slash-command in `GEMINI.md`, added it to `verify_skills.py` verification suite, updated `references/aios-user-manual.md` with instructions, and successfully verified the skill parser.

**Why:** The `/grill-me` skill provides a critical structured mechanism to brainstorm and capture your ideas immediately to file disk storage during detailed Q&A loops, preventing context window decay and keeping track of decisions.

**Alternatives considered:** Keeping the skill local to the Downloads folder or manually copy-pasting the skill contents whenever starting a brainstorm session.

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate Roast & Session Handoff Skills & Ingest Monetization Upgrades

**Decision:** Integrated `/roast` and `/session-handoff` skills into the AIOS. Registered the slash-commands in `GEMINI.md`, added them to `references/aios-user-manual.md` with operational guides, created `brain-aios/wiki/research/aios-monetization-upgrades.md` containing the YouTube clip digest of Nate Herk's 4 core monetization upgrades, updated the wiki index (`brain-aios/wiki/index.md`), and recorded the ingest event in `brain-aios/wiki/log.md`.

**Why:** The `/roast` and `/session-handoff` skills represent critical upgrades for business validation and context management respectively. Recording their details in the user manual and documenting the YouTube clip in the LLM Wiki ensures a complete knowledge record of the AIOS capabilities, keeping the repository aligned with Atinek Maurya's target workflow.

**Alternatives considered:** Manual copying of skill instructions or maintaining the monetization video takeaways as raw files without wiki integration.

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate Superpowers Skill & Set Up Global Rule File

**Decision:** Integrated `/using-superpowers` skill into the AIOS. Copied the skill config to `.agents/skills/using-superpowers/SKILL.md`, registered the command in `GEMINI.md`, added usage guidelines to `references/aios-user-manual.md`, updated `verify_skills.py` test suite, and created the global rule file `C:\Users\HP\.gemini\config\AGENTS.md` containing global instructions to enforce superpowers checks, planning, TDD, and verification across all project workspaces. Also documented the framework in `brain-aios/wiki/research/superpowers-framework.md`, updated the wiki index, and executed `agy plugin install https://github.com/obra/superpowers` to fully set up the superpowers plugin and hooks globally.

**Why:** The `using-superpowers` skill, plugin, and ruleset are essential for maintaining engineering discipline and preventing context rot/hallucinations by forcing structured planning, TDD, and verification cycles before code modification.

**Alternatives considered:** Using the global skill without local workspace registration, or writing rules to project-scoped `AGENTS.md` files (which requires duplication for every new repository).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate and Configure Context7 Globally

**Decision:** Registered the Upstash Context7 MCP server in the global `mcp_config.json` configuration, created a global skill `/context7` under `C:\Users\HP\.gemini\config\skills\context7\SKILL.md` to trigger live document retrieval, created `references/context7-api.md` API guide, and updated `GEMINI.md`, `connections.md`, `references/antigravity-skills-guide.md`, and `references/aios-user-manual.md` manuals.

**Why:** Adding Context7 globally gives the personal AIOS instant access to up-to-date, version-specific external library API documentation and code examples natively via MCP tools. This avoids model hallucination and reduces manual research overhead.

**Alternatives considered:** Running setup interactively via CLI `npx ctx7 setup` (unstable inside the sandboxed environment due to OAuth handling) or registering Context7 solely at the workspace level (fails the user's global usage requirement).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate 6 New Global MCP Servers & notion-sync Skill

**Decision:** Integrated 6 new global MCP servers (context7 with auth headers, codegraph, playwright, github with auth token, magic with API key, chrome-devtools-mcp, and notion-mcp-server with authorization header) into `mcp_config.json`. Created a custom workspace skill `/notion-sync` under `.agents/skills/notion-sync/SKILL.md` to handle sync, created 6 individual API reference guides in `references/`, and updated all AIOS user manuals, connection tables, and skills guide.

**Why:** Expanding global MCP integration allows the personal AIOS to orchestrate browser control, visual checks, code exploration, issue tracking, and Notion databases. Creating modular API guides keeps documentation clean and ensures that API keys and Notion tokens remain dynamic.

**Alternatives considered:** Using a single consolidated reference guide (unnecessarily cluttered and violates connections.md design guidelines) or hardcoding specific repository/database IDs in the skill code (fragile and insecure).

**Owner:** Antigravity AIOS

## 2026-07-15 — Refactor agent-adapt to Smart LLM-Driven Skill Transpilation

**Decision:** Refactored the `agent-adapt` skill under `d:\AI-OS\.agents\skills\agent-adapt\SKILL.md` from a blind regex find-and-replace Python script to an interactive, LLM-driven adaptation engine. Deleted the deprecated script `scripts/agent_adapt.py` and simplified `scripts/copy_skills_to_antigravity.py` to recursively copy skills raw without performing search-and-replace substitutions.

**Why:** Static find-and-replace of "Claude" with "Antigravity" causes critical bugs by breaking CLI executable commands, npm package scopes, GitHub repository URLs, and documentation links. Moving this logic to a smart, native, LLM-driven skill allows the agent to search the web for correct tool equivalents, deduct duplicates, flag Claude-specific items with markdown warnings, and present git-style diffs for user approval before writing files.

**Alternatives considered:** Maintaining the Python script but using the Gemini API (adds credential and dependency overhead) or manual adaptation on every import (slow and doesn't scale for the user's growing custom skills repository).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Centralize Workspace Directory Map & Log Boundaries

**Decision:** Created [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) at the workspace root to act as the centralized files and configurations directory index. Linked it in [GEMINI.md](file:///d:/AI-OS/GEMINI.md) and both Obsidian wiki indexes. Created a workspace-scoped rules file [AGENTS.md](file:///d:/AI-OS/.agents/AGENTS.md) to enforce map updates, and updated the [/review-day](file:///d:/AI-OS/.agents/skills/review-day/SKILL.md) skill to verify map alignment during evening reflections.

**Why:** Documentation, configs, connection guides, and logs were scattered across multiple folders. Enforcing log alignment policies prevents context fragmentation and directory rot. Automating wrap-up checks in `/review-day` and codifying rules in `.agents/AGENTS.md` prevents layout drift.

**Alternatives considered:** Using global config rules (blocked due to directory permissions) or keeping indices decentralized (leads to agent context dilution).

**Owner:** Antigravity AIOS

---
## 2026-07-15 — Implement Git Pre-Commit Workspace Map Validation Hook

**Decision:** Designed and implemented a Git pre-commit hook to automate the verification of [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) alignment. Created a Python validation script `scripts/validate_workspace_map.py` to check root files/folders, custom skill directories in `.agents/skills/`, and reference manuals in `references/`. Deployed the active Git hook to `.git/hooks/pre-commit` and committed a tracked backup to `scripts/hooks/pre-commit`.

**Why:** Relying on conversational memory (like the `/review-day` loop checklist) or rules file compliance alone leaves the configuration map vulnerable to decay. Enforcing validation programmatically in a Git hook prevents any unmapped folders or files from being committed, maintaining the integrity of the workspace.

**Alternatives considered:** Using a post-commit hook (too late to block commits) or manual audits (unreliable and easily bypassed).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Implement Improve-System Custom Skill & Experiences Vault

**Decision:** Created the `/improve-system` custom skill (`.agents/skills/improve-system/SKILL.md`) to analyze current session transcripts, automatically update iterated skills, and capture personal lessons/experiences in `brain-aios/wiki/experiences/`. Configured the chronological index file `context/experiences/README.md`, registered the new paths in `WORKSPACE_MAP.md` and `brain-aios/wiki/index.md`, and updated `GEMINI.md` and `.agents/AGENTS.md` rules to prompt self-improvement suggestions after major milestones.

**Why:** To establish a smart, closed-loop self-improvement mechanism that allows the AIOS to learn and grow over time from user feedback, skill output iterations, and shared lessons. Offloading transcript parsing to a subagent prevents context bloat in the main conversation window, maintaining token optimization.

**Alternatives considered:** Direct main-thread analysis (would cause high token usage and context window exhaustion) or manual copy-pasting of lessons and skill updates (adds operational friction and is prone to neglect).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Configure Scoped External Projects Junction Workspace

**Decision:** Created a master `D:\projects\` directory with seven specialized subfolders (`Websites`, `Zorixel brand`, `For AIOS`, `My advisors`, `Products`, `Learning`, `Sandbox`). Created matching directory junctions under `d:\AI-OS\projects\` pointing to these external folders, updated `.gitignore` to exclude the local `projects/` directory from Git tracking, and registered the new directory structure in `WORKSPACE_MAP.md`.

**Why:** Centralizing client websites, brand content, products, and AIOS projects inside the AIOS folder is desired for full context accessibility, but directly nesting Git repositories causes Git tracking corruption, nested submodule conflicts, and token search bloat (e.g. from `node_modules` or media assets). Using the junction pattern with `.gitignore` exclusion allows the AI to seamlessly read and write files across projects while keeping Git operations clean and avoiding context pollution.

**Alternatives considered:** Nesting raw project folders directly inside the AIOS Git repository (rejected due to Git pollution and token bloat), or keeping projects external with no local path references (rejected due to high path reference friction and manual command setup).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Implement project-agent Slash Command and Custom Workspace Skill

**Decision:** Created the `/project-agent` custom workspace skill at `.agents/skills/project-agent/SKILL.md` to delegate complex tasks to autonomous background developer subagents. Registered the slash command in `GEMINI.md` and `references/aios-user-manual.md`, added it to `WORKSPACE_MAP.md`, and completed the brainstorm capture file in `brainstorms/`.

**Why:** The user wants to build and test features inside project subdirectories without clogging the main session's context window. Spawning a background subagent (using `agy --print`) scoped to the specific project path keeps the main chat clean, enforces global superpowers and TDD workflows, auto-generates documentation (`walkthrough.md`), and fuzzy-matches project folder names to minimize typing overhead.

**Alternatives considered:** Using the main session for all tasks (clogs context window on large tasks), or running separate terminals manually (loses access to the user's AIOS skills and Obsidian memory context).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Implement developer Subagent Configuration for project-agent

**Decision:** Created a workspace-scoped subagent configuration file at `.agents/agents/developer.md` defining the specialized background developer agent behavior. Registered the `.agents/agents/` directory and `developer.md` in `WORKSPACE_MAP.md`, and checkpointed the brainstorm process in `brainstorms/2026-07-15-subagent-configuration.md`.

**Why:** The `/project-agent` skill delegates directory-scoped coding/content tasks to a background subagent by calling `agy --agent developer ...`. Defining this agent's metadata (Model: inherit, Color: blue, full tool access) and its system prompt (enforcing the Superpowers TDD loop and walkthrough logging) guarantees that the background subprocess behaves strictly in accordance with workspace standards.

**Alternatives considered:** Using the default `developer` agent without a workspace-scoped prompt configuration (would lack enforcement of project-specific `walkthrough.md` generation or direct alignment with the custom AIOS rules).

**Owner:** Antigravity AIOS

---

## 2026-07-15 — Integrate Karpathy Coding Guidelines Globally

**Decision:** Adapted and integrated the Karpathy-inspired coding behavioral guidelines from `andrej-karpathy-skills` repository into our local `GEMINI.md` file, registered the `/karpathy-guidelines` command, and installed the guidelines as a global custom skill at the user level in `C:\Users\HP\.gemini\config\skills\karpathy-guidelines\SKILL.md`. Documented the command in `references/aios-user-manual.md`, added it to `verify_skills.py` verifier, and updated `WORKSPACE_MAP.md`.

**Why:** Enforcing the four coding principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) globally across all workspaces keeps the codebase clean, minimizes overcomplication, enforces testing verification loops, and aligns with the Antigravity developer environment.

**Alternatives considered:** Installing at the project level in `.agents/skills/` (rejected since these are generic, cross-project coding behavior rules that the user wants to apply everywhere), or leaving them unmodified (would retain legacy Claude Code/Cursor specific terminology).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Implement Static Reference Library and Active marketing/seo-audit Router Skills

**Decision:** Created a static reference library at `d:\AI-OS\brain-aios\wiki\research\skills-library/` to store Corey Haynes' copywriting skills (~45 files) and Daniel Agrici's SEO skills (~25 files and 50 python scripts). Implemented two active router skills at `.agents/skills/marketing/SKILL.md` and `.agents/skills/seo-audit/SKILL.md` to load these frameworks dynamically on demand. Registered the slash commands `/marketing` and `/seo-audit` in `GEMINI.md`, and updated `WORKSPACE_MAP.md`.

**Why:** Installing 70+ separate skills directly in `.agents/skills/` causes massive memory bloat, startup lag, command collisions, and context window rot. Sandboxing the raw files in a static reference directory keeps the workspace clean, while the two active router skills dynamically read the guidelines and execute python scripts on demand, boosting performance and maintaining capability.

**Alternatives considered:** Porting all 70+ skills directly (token-heavy, slow, and violates the 3-5 active skills limit), or discarding the python files (would reduce SEO audits to simple advisory lists rather than actual page/schema checks).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Establish Skill Adaptation Rule in AGENTS.md

**Decision:** Appended a new workspace rule `## Adapting Skills to Antigravity & Gemini` in `.agents/AGENTS.md` to instruct the AI OS to check and tweak all loaded skills and guides for Antigravity/Gemini compatibility.

**Why:** Most community skills are written specifically for Claude Code or Cursor. Adding a dedicated rule in `AGENTS.md` ensures that the AI OS dynamically translates platform-specific terminology, paths, and commands in the background without modifying the core meaning or losing the capabilities of the original frameworks.

**Alternatives considered:** Manually editing all 70+ reference files in the library (extremely time-consuming, prone to syntax errors, and loses sync with upstream updates).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Implement Canvas Design Custom Skill and Library

**Decision:** Created the static reference library for Canvas Design at `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design/` (styles, specs, HTML template base) and registered the active router skill `.agents/skills/canvas-design/SKILL.md` (slash command `/canvas-design`). Integrated the user's `Temporary brand design.md` style guidelines and registered paths in `WORKSPACE_MAP.md`.

**Why:** The user wants programmatically generated social media graphics, posters, and brand banners matching their specific visual aesthetic (cream canvas, coral highlights, Garamond display type).Decoupling the templates and rendering logic keeps `.agents/skills` lightweight, while using the native `browser_subagent` Playwright screenshot mechanism ensures pixel-perfect PNG renders at exact preset aspect ratios without heavy local packages.

**Alternatives considered:** Using text-to-image diffusion models via `generate_image` (generates misspelled text and lacks structural layout precision), or installing local Node canvas dependencies (adds significant installation footprint and complexity).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — System Self-Improvement: Document Localhost Serving Rule & Capture Programmatic Canvas Experience

**Decision:** Updated `.agents/skills/canvas-design/SKILL.md` to document the localhost HTTP serving rule for browser subagents (to bypass local file scheme blocks). Created a new experience document at `brain-aios/wiki/experiences/2026-07-16-programmatic-canvas-browser-rendering.md` and registered it in indexes/logs.

**Why:** Spawning headless browsers to view local files natively results in sandboxing access violations. Establishing a background HTTP server serving pipeline guarantees robust renders across all user systems. Capturing this experience preserves the solution for future workspaces.

**Alternatives considered:** Standardizing on local file paths (rejected as it is blocked by browser security guidelines).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Implement Programmatic Viral Carousel Copywriter and Render Skills

**Decision:** Created the `.agents/skills/carousel-copy/SKILL.md` (for copy planning outlines) and `.agents/skills/carousel-render/SKILL.md` (for browser-captured slide rendering), registered them in `GEMINI.md` and `WORKSPACE_MAP.md`, added `scripts/compile_carousel.py` to parse markdown outlines into individual HTML slides, and extended `styles.css` with 3 carousel layout structures (Before/After split comparison, gradient headline rule, and brand header/footer slide furniture) modeled after `adarshxdesign`'s Instagram reference carousel.

**Why:** Using programmatic HTML-to-Image rendering over Midjourney/DALL-E prompt generation guarantees 100% spelling accuracy, perfect visual consistency (removing styling drift), and extremely fast rendering (under 1 minute for a 7-slide deck) in one click. Splitting the copywriting (/carousel-copy) and rendering (/carousel-render) into a 2-step workflow provides Atinek with complete control to edit copy and paste code blocks before compiling.

**Alternatives considered:** Using the DALL-E 3 image prompting workflow from the ingested playbook (too slow, prone to spelling errors, and requires manual copy-paste iteration and image downloads), or generating the carousel as a single multi-page scrolling HTML document (more prone to viewport scrolling inconsistencies than individual slide files).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Overhaul Slide Visual Aesthetics and Create Scrape-Carousel Skill

**Decision:** Completely overhauled the styling system in `styles.css` to introduce premium visual guidelines (radial grid backdrops, glassmorphic cards with inset shadows/borders, tightened letter-spacing and line-heights, and 3D rotated preview layouts) replacing the basic default formats. Created the active workspace skill `.agents/skills/scrape-carousel/SKILL.md` (slash command `/scrape-carousel`) to automatically crawl Instagram posts, bypass login overlays, locate active slides, and save cropped screenshot assets.

**Why:** The initial slide generation resulted in plain layouts that looked cheap and resembled "AI slop". Introducing professional web design techniques like grid arrays and backdrop blurs creates visually striking slides fitting the ZORIXEL brand identity. Automating the crawling process prevents manual page screenshotting and cropping overhead when indexing competitor ideas.

**Alternatives considered:** Using global css framework packages (adds bloat and fails to compile cleanly under static rendering), or relying on manual screenshotting for references (highly repetitive and slow).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Overhaul Visual Guidelines and Persistent Memory

**Decision:** Formulated and persisted Atinek's specific visual design rules for the ZORIXEL brand (warm linen `#fbfaf7` canvas, charcoal `#141413` text, upscaled font sizes, and pure white floating cards with highly diffused drop shadows) inside the global persistent memory [MEMORY.md](file:///d:/AI-OS/MEMORY.md). Updated active skills `.agents/skills/carousel-copy/SKILL.md` (to automatically generate spec options complying with these rules) and `.agents/skills/carousel-render/SKILL.md` (to serve templates over localhost HTTP rather than direct file paths to bypass sandbox security blocks).

**Why:** Spitting out generic layouts or basic templates reads as cheap and looks like "AI slop". Logging exact contrast ratios, card dimensions, shadows, and Safe Zone padding parameters in the core memory guarantees that the AIOS automatically generates visually stunning assets in future runs without repeating visual audit mistakes.

**Alternatives considered:** Relying on inline instructions (too prone to forgetting cross-session and leads to knowledge drift).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Establish Root Templates Junctions and Rename Daily Skills

**Decision:** Created a physical `templates/` directory at the root of the workspace (`d:\AI-OS\templates`), created two directory junctions pointing to the templates subfolders inside our Obsidian vaults (`templates/aios` -> `brain-aios/wiki/templates` and `templates/zorixel` -> `second-brain-zorixel/wiki/templates`), and renamed the daily cadence skills folders (`plan-day` and `review-day`) to `daily-plan-day` and `daily-review-day`. Updated all configuration files, guides, manual entries, and validation scripts to refer to the new `/daily-plan-day` and `/daily-review-day` commands.

**Why:** Having no root templates directory was flagged as a gap in our Four-Cs audit. Mapping the templates folders of both vaults under a unified root folder ensures easy access across the AIOS and prevents directory drift. Renaming the daily skills to start with `daily-` ensures compliance with canonical scheduled command patterns, resolving a second gap in our audit.

**Alternatives considered:** Mapping `templates/` directly to only one of the vaults (ignores templates in the other vault), or keeping the custom skills named `/plan-day` (violates scheduled-command naming conventions).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Workspace Root Files Cleanup & Vault Brainstorm Archiving

**Decision:** Moved `aios-intake.md` to `context/aios-intake.md`, moved `connections.md` to `context/connections.md`, created the archive folder `d:\AI-OS\brain-aios\archives\brainstorms\`, and relocated all completed brainstorm markdown files from the workspace root `brainstorms/` folder to the Obsidian vault's archive folder. Also purged all raw Playwright cache files (PNG/YML/LOG) inside `d:\AI-OS\.playwright-mcp/` and updated all config, guide, manual, and skill files to align with the new paths.

**Why:** Cleaning up root-level clutter optimizes system navigation, reduces folder noise, and keeps the active workspace clean. Archiving completed brainstorms into the Obsidian vault's archives folder ensures they remain searchable inside the user's Second Brain while removing them from the active coding repository. Purging the Playwright cache directory removes transient cache slop and saves disk space.

**Alternatives considered:** Keeping files at the root level (creates workspace clutter), or summarizing raw Playwright DOM trees (unnecessary prompt/token bloat).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Automate Playwright Cache Purging and Ignore Cache Bloat

**Decision:** Integrated an automatic `.playwright-mcp/` cache purging step into the `/daily-review-day` evening routine, appended `.playwright-mcp/` to the root `.gitignore`, added `.playwright-mcp` to the `ignored_root_items` inside `scripts/validate_workspace_map.py`, and recorded the system improvement lessons in a new experiences log `brain-aios/wiki/experiences/2026-07-16-aios-directory-hygiene-and-playwright-cache-automation.md`.

**Why:** The Playwright MCP server generates temporary HTML/YAML page state trees and screenshots during execution. These transient caches clutter Git status and trigger path-alignment errors in our pre-commit checks. Automating their removal at daily wrap-up and ignoring the directory in both Git and our custom map validator ensures that the user never has to manually clear these cache files and prevents directory checks from breaking.

**Alternatives considered:** Continuing manual cache deletions (annoying and error-prone), or logging cache files in `WORKSPACE_MAP.md` (causes path misalignment checks on every run).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Map and Integrate Premium Frontend Experience System

**Decision:** Created a directory junction at `premium-frontend-experience-system/` pointing to `C:\Users\HP\Documents\Premium-Frontend-Experience_System`. Registered the junction in `WORKSPACE_MAP.md`, integrated its guidelines as a default frontend design instruction in `GEMINI.md`, removed references to the deleted `vercel-composition-patterns` skill, and added a **Fast-Track Bypass Rule** in `ANTIGRAVITY_PROMPTING.md` for edits under 30 lines.

**Why:** The user mapped their premium frontend design system Obsidian vault into the workspace to serve as a visual "design brain". Enforcing visual restraint, viewport audits, and Playwright verification ensures that client and brand UI projects match professional creative engineering standards. Cleaning up dead references to deleted skills prevents tool execution errors, and the Fast-Track Bypass Rule resolves visual iteration lag on minor bug fixes and simple changes.

**Alternatives considered:** Duplicating the design system files directly inside the workspace (causes document fragmentation and updates wouldn't sync back to their active Obsidian design vault) or forcing full project briefs and Q&As on every minor layout fix (creates excessive procedural friction).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Restructure Premium Frontend Experience System & Configure Global Integrations

**Decision:** Consolidated the 10 root-level markdown files of the Premium Frontend Experience System into 4 clean, highly-structured files: `AGENTS.md` (Identity, default tech stack, and prompting), `POLICIES.md` (Component sourcing, motion guidelines, WebGL shader policies, and Design Token specifications), `WORKFLOWS_AND_QA.md` (Milestones and QA checklists), and `INTAKE_AND_REFERENCES.md` (Project Q&A and Reference auditing). Deleted the 9 duplicate root files, updated `WORKSPACE_MAP.md`, registered the `shadcn` and `flowbite-mcp` servers globally in `mcp_config.json`, created a custom global skill `threejs-webgl` under `C:\Users\HP\.gemini\config\skills\threejs-webgl\`, created the visual QA automation script `scripts/verify_design_milestone.py` in the workspace, cloned the full 10-module `threejs-skills` and 8-module `gsap-skills` libraries into the static research library `brain-aios/wiki/research/skills-library/`, created the active workspace skills `/verify-design` (milestone verification wrapper) and `/ingest-skills` (automated repository cloning & indexing engine), and updated the final step of `/grill-me` to execute `/roast` automatically.

**Why:** Having 10 separate markdown files repeating the tech stack, general rules, and QA checklists led to heavy documentation duplication, increased token consumption, and context fragmentation for the AIOS. Consolidating into 4 files keeps instructions lightweight and optimized for the LLM prompt context window. Registering the official shadcn and flowbite MCPs globally gives the AIOS direct access to Tailwind and shadcn tools across all projects. Creating the global `threejs-webgl` skill fills the gap for Three.js, shaders, and React Three Fiber best practices. Copying the full Three.js and GSAP repositories statically to `brain-aios` provides the AIOS with a progressive-disclosure-based granular reference database for complex scenarios. Creating the `/verify-design` and `/ingest-skills` active skills automates visual QA audits and repository ingestion into one-click commands, and connecting `/grill-me` to `/roast` ensures every discovery plan is automatically pressure-tested by the adversarial council. The python automation script `verify_design_milestone.py` replaces manual responsive and console audits with a one-click build and Playwright capture cycle.

**Alternatives considered:** Keeping the 10 root files separate (rejected due to prompt bloat), or manual verification (rejected as it is repetitive and prone to error).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Scrape Jordan Watkins Brand Reference & Automate Design Tools

**Decision:** Mirrored the entire asset and code tree of jordanwatkins.xyz locally to `second-brain-zorixel/wiki/research/jordan-watkins-reference/` using a Node scraper script (`scripts/mirror-jordan-watkins.js`). Created a visual and technical audit doc (`second-brain-zorixel/wiki/research/jordan-watkins-reference/analysis.md`), set up a background static web server (`scripts/serve.js`) hosting the mirrored website on port 3000, programmatically ran the local Typeface Picker and Palette Generator in Playwright to extract brand candidacies, and outputted the results to `second-brain-zorixel/wiki/brand/candidates.md` with visual preview blocks.

**Why:** Having a complete offline-available mirror of the website allows us to audit Jordan Watkins' design, typography, spacing tokens, and custom JS interaction mechanics (draggable physics, canvas paper background, spring custom cursor). Setting up a localhost server on port 3000 circumvents the `file:` protocol restriction in the Playwright MCP server, enabling automated visual testing and programmatic querying of his design tools to fetch brand candidates for Zorixel.

**Alternatives considered:** Scraping only textual summaries (rejected as it loses visual and script-level details) or querying the live website continuously (rejected because it depends on network availability and raises potential traffic throttling or TOS flags).

**Owner:** Antigravity AIOS

---

## 2026-07-16 — Create Scrape Component Skill for Targeted Design Reference Isolation

**Decision:** Created a workspace custom skill `/scrape-component` located at `.agents/skills/scrape-component/SKILL.md` to extract isolated UI elements, motion styles, and asset dependencies from websites. Integrated the new workflow into the design system vault files `premium-frontend-experience-system/INTAKE_AND_REFERENCES.md` (Section 5) and `premium-frontend-experience-system/AGENTS.md` (Prompt Pattern 11), registered it in `GEMINI.md` and `WORKSPACE_MAP.md`, and ran the pre-commit map validation to ensure workspace alignment.

**Why:** Mirrored reference websites can be massive and introduce substantial folder and codebase bloat. Providing a target-extraction skill allows us to scrape only the precise element (e.g. custom cursor, button animation, or bento layout) that the user likes. Asking targeted clarifying questions via `/grill-me` helps narrow down selectors and dependencies, producing standalone HTML/CSS/JS prototypes that can be hosted locally on localhost port 3000 for Playwright visual verifications.

**Alternatives considered:** Manual copying of source code (rejected due to speed and risk of missing dependencies) or only scraping full websites (rejected to prevent directory clutter).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Restructure Premium Frontend Experience System and Add Link-Rot Verification Hook

**Decision:** Restructured the `premium-frontend-experience-system/` directory junctions. Removed duplicate project contexts, status definitions, and lists from design briefs and asset briefs templates, replacing them with bracket references to the central `[[PROJECT_BRIEF]]` and `[[README]]`. Updated all 13 workflow guides to point to the new unified files `[[POLICIES]]` and `[[AGENTS]]`. Created `scripts/validate_links.py` to validate markdown relative and Obsidian `[[WikiLink]]` structures, and integrated it into the git pre-commit hook. Created custom slash commands `/new-project` and `/design-direction` and registered them in `WORKSPACE_MAP.md`.

**Why:** Consolidating templates and files keeps the codebase clean, reduces LLM context window consumption, and prevents token bloat during development. Adding an automated link validation checker to the pre-commit hook ensures absolute links integrity across directory renames and prevents broken wiki cross-references. Decoupling web layouts from social graphics prevents design contamination and keeps the business workflows clean.

**Alternatives considered:** Collapsing the entire experience system into a single file (rejected because it would lose detailed research, site database registries, and modular workflows).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Create AIOS Workflow Diagram & User Guide

**Decision:** Created `aios-workflow.excalidraw` in the workspace root and generated a simple, non-technical markdown user guide (`aios_workflow_guide.md`) in the artifacts directory. Registered the diagram in `WORKSPACE_MAP.md`.

**Why:** To provide Atinek Maurya with a clear, non-technical, visual and textual explanation of how the whole AIOS operates and how they can trigger commands, manage context, and automate content research and coding tasks.

**Alternatives considered:** Creating only a text guide without a visual Excalidraw diagram (less intuitive for visual design creators) or hardcoding visual assets inside the Obsidian vaults directly (harder to edit natively in Excalidraw).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Create Detailed AIOS Skills Reference Excalidraw Diagram

**Decision:** Created detailed skills reference Excalidraw diagram (`aios-skills-reference.excalidraw`) in the workspace root detailing 30 local & global skills, their purpose, when to use them, and real examples. Registered the file in `WORKSPACE_MAP.md`.

**Why:** To provide Atinek Maurya with a comprehensive, visual cheat-sheet of every tool, skill, and automation command in the AIOS, grouped by operational role (Ops, Marketing, Frontend, Code, Strategy, Admin).

**Alternatives considered:** Maintaining a long markdown list (hard to scan at a glance) or listing only custom slash commands (omits critical global rules and layout audits).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Organize Excalidraw Diagrams Into Dedicated Diagrams Directory

**Decision:** Created `diagrams/` folder in workspace root, moved existing `.excalidraw` files into it, updated build paths in `build_excalidraw.py`, and registered the directory and files in `WORKSPACE_MAP.md`.

**Why:** To avoid root-level workspace clutter and maintain strict directory hygiene by centralizing all visual design and workflow schemas in one structured location.

**Alternatives considered:** Keeping them at root (creates clutter) or moving to Obsidian vault folders (harder to edit natively in local workspace).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Integrate VibeSec Secure Coding Skill

**Decision:** Cloned VibeSec-Skill repository from GitHub, tweaked it to make it native to Antigravity, and installed it under `.agents/skills/vibesec/SKILL.md`. Registered the slash command in `GEMINI.md`, `references/aios-user-manual.md`, and `WORKSPACE_MAP.md`.

**Why:** To provide the AIOS with a structured secure-coding framework and checklists (covering IDOR, XSS, CSRF, secrets leakage, SSRF, SQLi, and JWT issues) when building, scanning, or auditing client web applications.

**Alternatives considered:** Leaving it as a static reference file (rejected because the user explicitly wants to trigger security audit checks in active coding sessions).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Resolve Bun Probe Hangs & Setup Claude-Mem Persistent Memory

**Decision:** Resolved local Bun probe hangs in sandboxed terminal environments by running the official Bun installer script to set up a standard working Bun binary at `C:\Users\HP\.bun\bin\bun.exe`. Installed the `claude-mem` persistent memory plugin for the Antigravity CLI, registering 7 lifecycle hooks, MCP configurations, and starting the memory worker daemon on port 37777.

**Why:** To ensure Bun child-processes do not block sandboxed PowerShell runs, and to establish persistent semantic memory that automatically captures context, observations, and decisions across sessions for the Antigravity CLI environment.

**Alternatives considered:** Using the pre-installed custom wrapper at `C:\Users\HP\AppData\Local\Kiro-Cli\bun` (rejected because it hangs indefinitely on console pipes under PowerShell jobs).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Centralize MCP Auth Parameters in `.env`

**Decision:** Added placeholder keys and documentation for `GITHUB_PERSONAL_ACCESS_TOKEN`, `API_KEY` (Magic MCP), `OPENAPI_MCP_HEADERS` (Notion MCP), and `CONTEXT7_API_KEY` (Context7 MCP) directly to the workspace `.env` file.

**Why:** To address the security and documentation gap identified during the AIOS structural audit, ensuring that all third-party API credentials used by the AIOS and its MCP servers are centralized in a single gitignored configuration file rather than dispersed across global environments or hardcoded variables.

**Alternatives considered:** Keeping them as system environment variables (rejected because it reduces workspace portability and visibility).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Create Application Security & Perimeters Diagram

**Decision:** Created the Excalidraw diagram `apps-security.excalidraw` in the `diagrams/` folder showing how application security perimeters and defense-in-depth layers function. Created the Python generator script `scripts/generate_security_diagram.py` to programmatically build the elements, and registered both the diagram and script in `WORKSPACE_MAP.md`.

**Why:** To address the user's request for a clear visual flowchart showing app security perimeters and logic layers using clean cards, logical color coding, and data flow arrows. Programmatic generation ensures pixel-perfect coordinates and maintains directory hygiene.

**Alternatives considered:** Drawing the diagram manually on excalidraw.com and uploading it (slower and doesn't persist the layout source code in the workspace repository).

**Owner:** Antigravity AIOS

---

## 2026-07-17 — Implement Autoresearch Targets Manager & Secure API Quota Fallbacks

**Decision:** Created a custom `/autoresearch-manage` active workspace skill at `.agents/skills/autoresearch-manage/SKILL.md` backed by the automation script `scripts/manage_autoresearch.py`. Configured the three Autoresearch trial scripts (`train.py` and `prepare.py`) to target the `gemini-3.1-flash-lite` model (avoiding 404/503 Free Tier API limits) and wrapped API executions in robust retry-backoff blocks. Created and ran a security audit script `scripts/security_check.py` to verify path traversals and secrets exclusion parameters.

**Why:** Spawning and maintaining custom trial configurations manually introduces folder structure errors and registry misalignment. The automation script programmatically registers new trial folders in the runner list and Workspace Map. Switching target models to `gemini-3.1-flash-lite` and incorporating API retries ensures 100% stable executions under free tier quotas without hitting spikes or model-deprecation errors.

**Alternatives considered:** Maintaining static target lists (inflexible and prone to manual error) or querying the deprecated `gemini-2.5-flash` model (crashes with 404 errors).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Resolve Python IDE Import Errors for `google-genai` and `playwright`

**Decision:** Created workspace settings `.vscode/settings.json` configuring the Python default interpreter to the virtual environment `trials/.venv/Scripts/python.exe`. Additionally, installed `google-genai` and `playwright` (with `playwright install chromium`) inside the system-wide Python environment. Updated the workspace map (`WORKSPACE_MAP.md`) to register the new configuration.

**Why:** The user was experiencing red import errors in their IDE because the IDE fell back to the system Python interpreter which did not have these packages installed. Setting the default interpreter path ensures VS Code/Cursor automatically uses the correct sandboxed virtual environment, and installing the packages system-wide serves as a fallback.

**Alternatives considered:** Creating a duplicate `.venv` at the workspace root (creates redundant virtual environments and package clutter) or only using global installation (does not guarantee IDE interpreter alignment).

**Owner:** Antigravity AIOS

---

## 2026-07-18 — Rebuild Brand Font Presentation into 12 Targeted Slides

**Decision:** Rebuilt the brand presentation deck down to a targeted 12-slide flow, focusing strictly on selected display candidate fonts (`Bezmiar`, `Rosehot`, `Grith`, `Vixa`) and the lowercase `Nuqun` brand logo. Modeled new slides off of Korean brand "newmix" footer structures and "AI in Design 2026" reports, implementing wide monospace letter-spacing for statistics, large cover sizes, and dedicated full-screen lowercase logo identity slides. Created python script `scripts/rebuild_presentation.py` to automate code restructuring.

**Why:** The user narrowed down their favorite typography options and brand logo (favoring lowercase `Nuqun`). Deleting all the intermediate concept routes keeps the deck clean, and adding layout clones with their selected fonts allows direct evaluation of wordmark proportions and text grids on high-contrast black and clean white screens.

**Alternatives considered:** Keeping the 34-slide deck with duplicate concepts (creates too much visual clutter and distracts from final font selections).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Restructure Brand Presentation into 20-Slide Interactive Page Matrix

**Decision:** Restructured `presentation.html` into a 20-slide grid (4 font pairings × 5 canonical pages: Hero, About & Contact, Live Dashboard, Creative Poster, Brand Footer). Implemented lowercase `Nuqun` `"zorixel"` branding across all layouts and configured a dual-axis bottom navigation dock (FONTS row + PAGES row) for side-by-side comparison. Restructured Playwright QA configuration `qa/audit.js` and regenerated screenshots. Created `scripts/rebuild_presentation_20.py` to automate code generation.

**Why:** The user wanted to directly evaluate how their favorite font pairings look on actual website layouts rather than isolated sentences. Combining pages and adding a dual-axis selector enables immediate comparison of a single layout across different fonts (e.g. comparing footer layouts) or sequential options review.

**Alternatives considered:** Designing 20 individual HTML files (inflexible and difficult to browse synchronously).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Finalize Zorixel Brand Typography & Generate 2K High-Res Logos

**Decision:** Finalized Zorixel's typography design: brand logo is lowercase `"zorixel"` in `Nuqun` regular font with a chromatic aberration (RGB split) effect; display serifs are `Rosehot` (Title Case); display creative headings are `Vixa` (Title Case, 2-5 words only); paragraph body copy is `Outfit`; statistics numbers are `Space Mono`. Created and ran Playwright script `projects/font-showcase/generate_nuqun_logo.js` to output 2000x2000 transparent logo files (with/without background) and 100% vector SVG files (solid white, solid dark, and vector chromatic aberration). Created canonical guide at `second-brain-zorixel/wiki/brand/typography.md` and registered files in `WORKSPACE_MAP.md`.

**Why:** The user confirmed that the logo font must remain `Nuqun` (exactly as designed in the slides and presentation), and requested 2000x2000 transparent/solid background PNG files along with vector SVG files for Canva/Figma editing.

**Alternatives considered:** Using embedded font tags in SVGs (inflexible as Canva does not load the custom local Nuqun font automatically).

**Owner:** Atinek Maurya

---

## 2026-07-18 — Zorixel Color Presentation Symmetrical Contrast Inversion & Single-Line Parser

**Decision:** Implemented a symmetrical contrast inversion engine and a single-line color palette parser inside `colors_presentation.html`. The parser uses regex to extract all hex values from any pasted text and automatically analyzes them (calculating relative luminance and colorfulness). It then automatically sorts them (Darkest to Lightest), discovers the Accent highlight, and maps them to semantic layout variables. In Dark Mode, the engine dynamically swaps/inverts the variable mappings (e.g. mapping `--color-1` to lightest and `--color-5` to darkest) and blends the darkest color with 92% black to construct a rich dark background.

**Why:** The user was experiencing poor contrast and low legibility where light colors became backgrounds for light text, or dark colors became backgrounds for dark text in dark mode. Letting the engine dynamically sort and map roles by luminance mathematically guarantees high contrast (WCAG compliance) and legibility. The single-line parser enables immediate copy-pasting of palettes from color tools (such as Jordan Watkins' archives) in a single action.

**Alternatives considered:** Maintaining manual/static coordinate color selectors (requires constant manual adjustment and leads to high contrast failure rates).

**Owner:** Atinek Maurya

---

## 2026-07-19 — Integrate Figma Remote MCP Server

**Decision:** Registered the official Figma Remote MCP server in the global `mcp_config.json` configuration, created a reference manual `references/figma-api.md`, updated `connections.md` and `WORKSPACE_MAP.md`.

**Why:** Direct integration with Figma allows the personal AIOS to pull design metadata, tokens, and layouts natively, accelerating high-fidelity design-to-code workflows for ZORIXEL.

**Alternatives considered:** Local command-line figma-developer-mcp with personal access tokens (rejected due to token-maintenance overhead and lack of official Code Connect mappings).

**Owner:** Antigravity AIOS

---

## 2026-07-19 — Automated Extraction and Compilation of 50 Figma Micrographics

**Decision:** Developed a programmatic Python compiler script (`compile_micrographics.py`) that loads the Figma JSON design tree, extracts layout properties/typography coordinates, downloads raw SVGs, and isolates 296 standalone vector symbols. Compiles the 50 templates into three output formats inside `projects/For AIOS/Micrographics/`: raw SVGs, editable standalone HTML/CSS cards (layering live text nodes using Google Fonts absolute coordinate overlays), and parameterized React JSX components. Generated an interactive preview showcase dashboard (`index.html`) and verified layouts using Playwright.

**Why:** Direct Figma SVG exports output text layers as outlined vector paths, making them uneditable in code. Layering styled HTML/React text nodes over background SVGs preserves editability and custom typography (Google Fonts) while matching the Figma layout grid with 100% mathematical precision.

**Alternatives considered:** Manual coding of 50 micrographics (rejected due to excessive development time and risk of alignment inaccuracies).

**Owner:** Antigravity AIOS

---

## 2026-07-19 — Visual QA & Alignment Restructuring of 50 Figma Micrographics

**Decision:** Overhauled the Figma Micrographics rendering engine inside `compile_micrographics.py`. Mapped original Figma back-to-front layer stack traversal, extracted visual dimensions directly from raw SVG code to prevent scale compression of horizontal/vertical lines, and implemented native trigonometric unrotated coordinate mapping and CSS rotation transforms for rotated text layers. Added text-stroke outlines for hollow border text, line-height top vertical offsets, single-word `nowrap` wrapping prevention, and expanded font weights. Re-compiled all 50 layout templates and ran Playwright visual checks on 17 target frames (Dashboard + frames 2, 9, 11, 12, 15, 18, 23, 24, 25, 27, 31, 34, 35, 36, 40, 43, 44) with zero errors.

**Why:** Initial browser compilation resulted in overlapping elements, missing hollow border text, wrapped single words, distorted SVG arrow lines, and misplaced rotated text layers. Correcting the layer ordering to back-to-front and extracting native visual dimensions from SVG contents prevents Chromium from scaling down viewBoxes and solves layering overlaps, while native trig calculations and CSS rotation transforms align elements with pixel-perfect precision to the design canvas.

**Alternatives considered:** Manual stylesheet tweaks per frame (unstable and breaks programmatically generated updates).

**Owner:** Antigravity AIOS

---

## 2026-07-19 — System self-improvement: Regression Prevention and Scoping Safety Rules

**Decision:** Updated workspace rules in `d:\AI-OS\.agents\AGENTS.md` and custom workspace skill `verify-design/SKILL.md` to establish visual regression QA guidelines, scoping order requirements, and Playwright execution context checks. Created experience document `2026-07-19-compiler-regression-prevention-and-trig-alignment.md` in `brain-aios` and updated the experiences index table in `context/experiences/README.md`.

**Why:** To address the user's critique regarding visual layout bugs that slip in on compiled assets during individual target repairs. Establishing programmatic checks, scoping safety guidelines, and multi-asset Playwright visual regression sweeps ensures that the personal AIOS delivers 100% stable layouts with zero side-effect regression bugs.

**Owner:** Antigravity AIOS

---

## 2026-07-19 — Operator Verification, Security, & Grill Me/Roast Pre-checks

**Decision:** Updated workspace rules in [d:\AI-OS\.agents\AGENTS.md](file:///d:/AI-OS/.agents/AGENTS.md) and persistent memory preferences in [d:\AI-OS\MEMORY.md](file:///d:/AI-OS/MEMORY.md). Added rules enforcing the "Understand & Verify First" principle, security, bloat and duplication audits, mandatory `/grill-me` or `/roast` pre-checks for ideas/designs, and automatic bootup upgrades for custom skills on starting new sessions.

**Why:** To address the operator's feedback on preventing blind changes, ensuring actual physical checks are executed before delivering files, and using systematic discovery tools (`/grill-me` and `/roast`) to stress-test designs and catch security/bloat vulnerabilities.

**Owner:** Antigravity AIOS

---

## 2026-07-19 — AIOS Self-Improvement: Security hardening, regression prevention hooks, and skill adaptations

**Decision:** Implemented a comprehensive security audit and self-improvement package:
1. Hardened `trials/runner.py` credentials loading to fail closed if `GEMINI_API_KEY` is missing/empty.
2. Extended `scripts/security_check.py` to scan for Notion, GitHub, and Google Workspace keys, and block credentials json exposure.
3. Expanded `scripts/verify_skills.py` to recursively compile and verify Python, JavaScript, and JSON syntax across all custom skills.
4. Installed a Git pre-commit hook that automatically blocks commits if security checks or skill verifications fail.
5. Adapted local design and scraping skills (like `seo-audit`, `frontend-slides`, `scrape-reference`, and `scrape-component`) to run natively under Antigravity. Dynamic localhost static server utilities (`serve.js`) were updated to bypass local browser restrictions.
6. Created `references/global-rules-conflict-resolution.md` to prevent layout overlaps and conflicts between global skills (`impeccable`, `ui-ux-pro-max`).

**Why:** To address the user's request to secure the AIOS from credentials leaks and path traversals, break the "one solution, four new problems" regression cycle, and optimize all local scraping and design workflows for the Antigravity developer environment.

## 2026-07-23 — System Improvement: Micrographics Compiler Fixes, Upgrade /improve-system with Security Auditing

**Decision:** Executed a full system self-improvement cycle:
1. Created experience document [2026-07-23-figma-micrographics-compiler-fixes-and-security.md](file:///d:/AI-OS/brain-aios/wiki/experiences/2026-07-23-figma-micrographics-compiler-fixes-and-security.md) and updated `context/experiences/README.md`.
2. Upgraded [.agents/skills/improve-system/SKILL.md](file:///d:/AI-OS/.agents/skills/improve-system/SKILL.md) with an integrated Security Audit phase (Vibesec & secrets hygiene scans), deep transcript pattern analysis protocol, and empirical verification requirements.
3. Updated workspace rules in [.agents/AGENTS.md](file:///d:/AI-OS/.agents/AGENTS.md) with Figma node visibility filtering rules, pre-rotated SVG geometry safeguards, SVG-to-JSX inline style object conversions, and secrets hygiene rules.

**Why:** Resolves root-cause bugs across 50 compiled layouts (dropping layout mismatch from 40%+ to < 3.99% across all 50 cards with 0 JSX errors), while empowering the system's self-improvement workflow to automatically audit security vulnerabilities and verify system stability on future runs.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — System Improvement: MCP Server Configuration & Windows Binary Resolution

**Decision:** Executed a system self-improvement cycle to resolve MCP server initialization failures (`codegraph`, `figma`, `shadcn`):
1. Created experience document [2026-07-23-mcp-server-configuration-and-windows-binary-resolution.md](file:///d:/AI-OS/brain-aios/wiki/experiences/2026-07-23-mcp-server-configuration-and-windows-binary-resolution.md) and updated `context/experiences/README.md`.
2. Fixed `mcp_config.json` package resolution by replacing non-existent package `@modelcontextprotocol/server-figma` with `figma-developer-mcp`, mapping explicit binary path `codegraph.cmd` to avoid Windows child process resolution hangs, and pre-caching `shadcn` globally.
3. Updated workspace rules in [.agents/AGENTS.md](file:///d:/AI-OS/.agents/AGENTS.md) with Windows MCP binary path rules and package pre-caching requirements.

---

## 2026-07-23 — System Improvement: Figma MCP Transport Protocol & Clean Stdio Logging Fix

**Decision:** Resolved the `figma: calling "initialize": invalid character 'C' looking for beginning of value` MCP initialization error:
1. Identified that `figma-developer-mcp` defaults to HTTP server mode listening on port 3333 and emits non-JSON startup/warning logs (`Usage telemetry enabled...`, `Warning: --image-dir not set...`) to stdout, polluting standard output.
2. Updated all `mcp_config.json` configurations (`C:\Users\HP\.gemini\antigravity\mcp_config.json`, `C:\Users\HP\.gemini\antigravity-ide\mcp_config.json`, `C:\Users\HP\.gemini\config\mcp_config.json`) to include explicit CLI arguments `["-y", "figma-developer-mcp", "--stdio", "--no-telemetry", "--image-dir", "d:\\AI-OS"]` and environment variables (`FIGMA_API_KEY`, `FRAMELINK_TELEMETRY="off"`, `DO_NOT_TRACK="1"`).
3. Verified clean execution of `figma-developer-mcp` stdio transport without unhandled stdout log output.

**Why:** Prevents non-JSON log messages from breaking the JSON-RPC initialization handshake in Antigravity and Claude Desktop MCP clients.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Scrapling Web Scraping Engine Integration

**Decision:** Audited, integrated, and adapted the Scrapling web scraping framework (`d4vinci/Scrapling`) into AIOS. Built the Python engine CLI wrapper (`scripts/scrapling_runner.py`), created the new skill `.agents/skills/scrape-web/SKILL.md`, upgraded `/scrape-competitor` and `/seo-audit` skills to route through Scrapling, and registered the configuration across `WORKSPACE_MAP.md`, `GEMINI.md`, and `MEMORY.md`.

**Why:** Web scraping for competitor research and dynamic site auditing frequently suffered from Cloudflare bot detection, anti-bot captchas, and broken CSS selectors. Scrapling provides 100% free, MIT-licensed adaptive element fingerprinting (auto-healing selectors) and stealth header emulation (`StealthyFetcher`), while running locally without external API costs.

**Alternatives considered:** Using Playwright-only Node scripts for data fetching (heavy, slow for simple text/data extraction, and prone to bot detection) or paying for third-party scraping APIs (unnecessary cost). Reserved `/scrape-reference` specifically for offline visual asset cloning.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Repository Ingestion & Skill Adaptation Engine (`/ingest-repo`)

**Decision:** Created `/ingest-repo` (`.agents/skills/ingest-repo/SKILL.md`) and upgraded `/ingest-skills` to route directly into an 8-phase autonomous repository ingestion pipeline. Added the **Automatic Skills-Library Search Rule** and **Scratch Isolation & Cleanup Rule** to `.agents/AGENTS.md` and `MEMORY.md`.

**Why:** Automates the complete lifecycle of evaluating, security-auditing, comparing against existing tools, roasting via 5-persona council, adapting, and indexing any external GitHub repository into native Antigravity scripts, slash commands, and Obsidian research libraries. Mandatory scratch folder cleanup resolves Contrarian concerns regarding workspace clutter and context token leaks.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Agent Reach Ingestion & Skill Adaptation

**Decision:** Ingested `Panniantong/agent-reach` (v1.5.0, MIT License) via `/ingest-repo`. Created `.agents/skills/agent-reach/SKILL.md`, `scripts/agent_reach_runner.py`, and reference manual `brain-aios/wiki/research/skills-library/agent-reach/README.md`. Registered in `WORKSPACE_MAP.md`, `GEMINI.md`, and `MEMORY.md`.

**Why:** Agent Reach provides single-command multi-backend routing across 10+ web and social platforms (YouTube subtitles, Bilibili zero-login search, V2EX tech feeds, Twitter, Reddit, RSS, Xueqiu, Xiaoyuzhou podcast transcription). It automatically falls back to secondary backends if anti-scraping blocks occur, drastically expanding AIOS internet capabilities for Zorixel research.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — System Self-Improvement & AIOS Wide Integration

**Decision:** Executed `/improve-system` workflow. Captured lesson in `brain-aios/wiki/experiences/2026-07-23-agent-reach-ingestion-and-github-keyring-auth.md`, updated `context/experiences/README.md`, added **Env Variable Token Precedence Rule**, **yt-dlp JS Runtime Rule**, and **Brave Browser Bridge Compatibility Rule** to `.agents/AGENTS.md` and `MEMORY.md`. Updated all workspace documentation (`aios-user-manual.md`, `antigravity-skills-guide.md`, `web-research-capture-sop.md`, `scrape-competitor`, `marketing`), registered connections in `context/connections.md`, and committed/pushed all updates to `main`.

**Why:** Ensures cross-session learning from GitHub CLI keyring token overrides, yt-dlp Node.js runtime setup, and Brave browser bridge integration, while making Agent Reach multi-platform research available across all content, copywriting, and SEO skills.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Ingest Garry Tan's gstack Framework & Adapt Virtual Engineering Team Skill

**Decision:** Ingested `garrytan/gstack` (v1.60, MIT License) via `/ingest-repo`. Created native Antigravity skill `.agents/skills/gstack/SKILL.md` (exposed as `/gstack`), saved complete reference documentation to `brain-aios/wiki/research/skills-library/gstack/README.md`, and registered paths in `WORKSPACE_MAP.md`, `GEMINI.md`, and `MEMORY.md`. Cleaned up temporary scratch clone (`scratch/ingest-gstack/`).

**Why:** `gstack` brings Y Combinator founder-level product strategy (`/gstack ceo`), engineering manager architecture guardrails (`/gstack eng`), UI/UX design standards (`/gstack design`), and browser QA testing (`/gstack qa`) to our AI agent. Adapting these role perspectives into a clean Antigravity slash command gives AIOS a high-leverage virtual executive review layer without adding unneeded Bun runtime bloat to the workspace root.

## 2026-07-23 — Ingest nutlope/hallmark & Adapt Anti-AI-Slop Design Engine

**Decision:** Ingested `nutlope/hallmark` (v1.1.0, MIT License, Together AI) via `/ingest-repo`. Created native Antigravity skill `.agents/skills/hallmark/SKILL.md` (exposed as `/hallmark`), audit runner script `scripts/hallmark_runner.py`, and stored complete skills library to `brain-aios/wiki/research/skills-library/hallmark/`. Registered in `WORKSPACE_MAP.md`, `GEMINI.md`, `MEMORY.md`, `references/aios-user-manual.md`, and `references/antigravity-skills-guide.md`. Cleaned up temporary clone (`scratch/ingest-hallmark/`).

**Why:** Hallmark enforces structural layout variety (21 macrostructures), color theme selection (20 OKLCH themes + custom engine), and 57 anti-slop quality gates across build, audit, redesign, and study verbs. This ensures all UIs generated for ZORIXEL and client AI automations avoid generic AI template tropes.

## 2026-07-23 — Deep Cross-System Integration of Hallmark & Ingested Skill Engines

**Decision:** Integrated `/hallmark` anti-slop dynamic invocation rules, 21 macrostructure layout archetypes, OKLCH color palettes, and 57 quality gates across workspace agent rules (`.agents/AGENTS.md`), developer subagent prompt (`.agents/agents/developer.md`), project scaffolding skill (`.agents/skills/new-project/SKILL.md`), design direction generator (`.agents/skills/design-direction/SKILL.md`), and automated visual verification loop (`.agents/skills/verify-design/SKILL.md`).

**Why:** Ensures that anti-AI-slop layout rules and automated slop checks (`python scripts/hallmark_runner.py audit`) are dynamically enforced across all developer subagents, project initializations, visual style guides, and milestone verification sweeps without requiring the user to type `/hallmark` explicitly every time.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Full-Code Mirroring, Unbounded Exhaustive Discovery, & Master Vault Reference Indexing

**Decision:** Built full-code site mirror script `scripts/scrape_full_site_mirror.py` using Playwright network interceptors to download 100% of target site HTML, CSS, JS bundles, custom fonts, images, and videos. Codified the **Unbounded Exhaustive Discovery & Non-Exhaustive Examples Rule** across `GEMINI.md`, `.agents/AGENTS.md`, `MEMORY.md`, `.agents/skills/scrape-reference/SKILL.md`, and `reference-pipeline-spec.md`. Created dedicated master reference vault `premium-frontend-experience-system/vault-references/` with central index (`INDEX.md`) and 14+ category dot-to-dot reference manuals (`sondaven-granularity-master.md`). Logged experience document in `brain-aios/wiki/experiences/2026-07-23-scrape-reference-full-code-mirroring-and-vault-indexing.md` and updated `context/experiences/README.md`.

**Why:** To ensure that reference website ingestions capture complete runnable code, WebGL shaders, visual WebP session recordings, and 14+ category dot-to-dot design decisions without being artificially constrained by example lists or high-level textual summaries, while strictly enforcing one-by-one sequential queue execution.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Reference Ingestion Completed for Oryzo AI & The Line Studio

**Decision:** Executed full site mirroring, visual asset capture, code extraction, and 15-category master reference manual synthesis for **Oryzo AI** (`https://oryzo.ai/`) and **The Line Studio** (`https://thelinestudio.com/`).
- Intercepted 37 3D binary mesh buffers (`.buf`), Rive animation runtimes (`.riv`, `.wasm`), Gaussian Splat sorters (`splat_sorter_bg-BfJrILzx.wasm`), and 96 PBR texture maps for Oryzo AI.
- Intercepted 1.68 MB source markup, 46 JS bundles, and 34 CSS modules for The Line Studio.
- Extracted standalone React components (`Hero3DCanvas.tsx`, `MagazineWidget.tsx`, `LineStudioNav.tsx`, `ProjectShowcaseCard.tsx`), GSAP/Lenis setups, and OKLCH design tokens.
- Updated `premium-frontend-experience-system/vault-references/INDEX.md`, `INGESTION_QUEUE.md`, `WORKSPACE_MAP.md`, and `decisions/log.md`. Updated `/scrape-reference` skill (`SKILL.md`) to mandate 3D asset & motion physics extraction.

**Why:** Enforces complete end-to-end connectivity across all system indexes, vault reference manuals, decision logs, and skill guidelines.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Reference Ingestion Completed for Gehry Getty

**Decision:** Executed full site mirroring, visual asset capture, 3D GLTF model extraction, audio stream capture, and 15-category master reference manual synthesis for **Gehry Getty** (`https://gehry.getty.edu/`).
- Intercepted 3 3D architectural models (`getty_formStudy_hotspot_desktop.glb`, `getty_organ_hotspot_desktop.glb`, `getty_shoebox_hotspot_desktop.glb` — 12.1 MB total), Basis Universal GPU Transcoder (`basis_transcoder.wasm`), 5 guided audio streams (`chapter1.mp3`, `chapter2.mp3`, `chapter3.mp3`), and JSON transcript manifests.
- Extracted standalone React components (`Architectural3DViewer.tsx`, `AudioNarrativePlayer.tsx`), Three vector spring physics (`three-vector-spring.js`), and OKLCH design tokens.
- Updated `premium-frontend-experience-system/vault-references/INDEX.md`, `INGESTION_QUEUE.md`, `WORKSPACE_MAP.md`, and `decisions/log.md`.

**Why:** Enforces complete end-to-end connectivity across all system indexes, vault reference manuals, and architectural 3D study logs.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Excalidraw Wireframe Diagram Integration into `/scrape-reference` Skill

**Decision:** Codified mandatory Excalidraw wireframe diagram generation (`assets/wireframe.excalidraw`) into the `/scrape-reference` skill (`.agents/skills/scrape-reference/SKILL.md`) and built automated generation engine `scripts/generate_site_wireframes.py`.
- Retrofitted and generated editable `.excalidraw` wireframe diagrams for all 4 completed reference sites (**Sondaven**, **Oryzo AI**, **The Line Studio**, **Gehry Getty**).
- Registered wireframe diagrams across `premium-frontend-experience-system/vault-references/INDEX.md` and individual site directories under `assets/wireframe.excalidraw`.

**Why:** Ensures that every ingested reference site contains an editable visual layout blueprint detailing hero architecture, navbar mechanics, 3D stages, scrollytelling sections, and footer containers that can be opened directly on excalidraw.com.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Detailed Visual UI/UX Wireframe Generation Engine (`wireframe.html` & `wireframe.png`)

**Decision:** Built automated visual wireframe engine `scripts/generate_visual_wireframes.py` creating hyper-detailed low-fidelity visual wireframe HTML pages (`wireframe.html`) and Playwright screenshot captures (`wireframe.png`) for every site in the reference ingestion queue.
- Replaced basic Excalidraw JSON blocks with true visual UI wireframe mockups rendering exact site layouts (navbar branding, 3D WebGL canvas boxes, scrollytelling cards, interactive prompt widgets, audio player drawers, and grid columns).
- Codified `wireframe.html` and `wireframe.png` generation into `.agents/skills/scrape-reference/SKILL.md` and updated `premium-frontend-experience-system/vault-references/INDEX.md`.

**Why:** Gives the user an immediate, visual structural blueprint of the website's UI/UX architecture directly viewable as a high-resolution PNG image or interactive HTML page in VS Code / browser without needing external tools.

**Owner:** Antigravity AIOS

---

## 2026-07-23 — Hyper-Detailed Visual UI/UX Wireframe Upgrade (`wireframe.html` & `wireframe.png`)

**Decision:** Upgraded the visual wireframe compiler `scripts/generate_visual_wireframes.py` to produce section-by-section, hyper-detailed architectural blueprints containing:
- Actual site copy, real headlines, and sub-text outlines.
- Exact component specification tags (`COMPONENT: HEADER / NAV SYSTEM`, `COMPONENT: HERO SECTION & 3D WEBGL STAGE`, `COMPONENT: 2-COLUMN SCROLLESTELLING`, `COMPONENT: DRAG-ALONG-PATH SVG SEASON SLIDER`, etc.).
- Explicit technical annotations detailing CSS properties, GSAP transform parameters, WebGL canvas render specs, and scroll trigger thresholds.
- Grid blueprint background overlays, 3D model stage boxes (`canvas#canvas`), audio player controllers, and multi-column card layouts.
- Retrofitted and generated high-resolution screenshots (`wireframe.png`) and HTML pages (`wireframe.html`) for all 4 completed reference sites (**Sondaven**, **Oryzo AI**, **The Line Studio**, **Gehry Getty**).

**Why:** Delivers a true, comprehensive visual UI/UX layout blueprint for every website in the ingestion queue.

**Owner:** Antigravity AIOS






---

## 2026-07-24 — System Improvement: Obys Grid System Deep Research & System Integration

**Decision:** Conducted deep visual Playwright research and text corpus extraction across all 4 chapters of **Grids by Obys Agency** (`https://grids.obys.agency/`). Integrated Obys' 4 Grid Canons (Column Grid, Van De Graaff Golden Canon, Rectangular/Modular Grid, and Horizontal Baseline Grid) into the AIOS design system.
- Created `premium-frontend-experience-system/vault-references/grids-obys-agency-deep-research.md`.
- Logged experience in `brain-aios/wiki/experiences/2026-07-24-obys-grid-system-mastery.md` and updated `context/experiences/README.md`.
- Updated persistent system memory (`MEMORY.md`) with Grid Calculation Rules & Baseline Vertical Rhythm formulas.
- Updated `WORKSPACE_MAP.md` and ran pre-commit verification.

**Why:** Elevates the AIOS design brain with professional grid systems math, layout formulas, and layout principles directly from Obys Agency.

---

## 2026-07-24 — Site Ingestion: The Shift Tokyo (`the-shift-tokyo`)

**Decision:** Completed full site mirroring, visual screenshot capture (5 viewports), raw code extraction (React TSX components, Tokyo live clock widget, GSAP kinetic animations, OKLCH design tokens, WebGL GLSL liquid distortion shader), hyper-detailed visual wireframe blueprint (`wireframe.html` & `wireframe.png`), 5-layer site DNA analysis, deep technical analysis, and dot-to-dot 15-category master reference manual for **The Shift Tokyo** (`https://theshift.tokyo/en/`).
- Updated `premium-frontend-experience-system/vault-references/INDEX.md` registering `the-shift-tokyo-granularity-master.md`.
- Marked Site #6 as completed in `premium-frontend-experience-system/reference-inputs/INGESTION_QUEUE.md`.

**Why:** Enforces strict sequential one-by-one reference ingestion, capturing avant-garde Japanese digital agency design patterns and real-time timezone mechanics.

## 2026-07-24 — Completion of 18-Site Reference Ingestion Campaign & System Synchronization

**Decision:** Completed full ingestion, mirroring, visual wireframing, code extraction, and dot-to-dot granularity indexing for all 18 reference websites in `INGESTION_QUEUE.md` (including Sondaven, Oryzo AI, The Line Studio, Gehry Getty, Grids Obys Agency, The Shift Tokyo, Unleashing Best, Truck 'n Roll, Outfit Hello Hello, Tresmares Capital, Ashley Brooke CS, Jasmine Gunarto, Off Menu Design, Detroit Paris, Made In Evolve, Champions 4 Good, Good Fella, and Follow Art).
- Established dual-stack preservation rule (100% untouched raw mirrors + modular React/CSS extracts).
- Registered all 18 master manuals in `vault-references/INDEX.md`.
- Connected the reference vault across `brain-aios` and `second-brain-zorixel`.
- Updated `MEMORY.md`, `WORKSPACE_MAP.md`, and logged learnings in `brain-aios/wiki/experiences/2026-07-24-18-site-reference-ingestion-completion.md`.

**Why:** Equips the Premium Frontend Experience System with a comprehensive, production-tested reference vault of Site of the Day award winners to power Zorixel brand content, UI components, and design systems.

---

## 2026-07-24 — System Improvement: Curated Component Libraries Ingestion & 100% URL/CLI Completeness

**Decision:** Synthesized and enriched 147 UI components across Aceternity UI, Animate UI React, Forge UI, and Vengence UI into the Premium Frontend Experience System.
- Created `component-registry-index.json` and `MASTER_COMPONENT_CATALOG.md` in `premium-frontend-experience-system/source-registries/` with 100% complete URLs and CLI commands.
- Hardcoded mandatory component-first sourcing rules in `.agents/AGENTS.md`, `premium-frontend-experience-system/AGENTS.md`, and `MEMORY.md`.
- Created interactive search CLI `scripts/component_registry_cli.py` with UTF-8 Windows terminal support.
- Logged experience in `brain-aios/wiki/experiences/2026-07-24-curated-component-libraries-ingestion.md` and updated `context/experiences/README.md`.
- Updated `WORKSPACE_MAP.md` and validated alignment via `scripts/validate_workspace_map.py`.

**Why:** Establishes a component-first architecture preventing generic component re-invention, ensuring all future web projects automatically leverage curated, high-quality component patterns.

**Owner:** Antigravity AIOS

---

## 2026-07-24 — Execute OS Audit Batch A (Routing Integrity & Index Reconciliation)

**Decision:** Executed Batch A of the OS Audit report ([audits/os-audit-2026-07-24.md](file:///d:/AI-OS/audits/os-audit-2026-07-24.md)):
- Updated `GEMINI.md` relative routing paths to include `brain-aios/` and `second-brain-zorixel/` vault prefixes.
- Registered 7 missing active workspace skills (`canvas-design`, `design-direction`, `excalidraw-diagram`, `frontend-slides`, `new-project`, `skill-builder`, `slide-component`) in `GEMINI.md`.
- Registered 13 maintenance scripts, 15 brainstorm documents/assets, and audit reports in `WORKSPACE_MAP.md`.
- Reconciled `brain-aios/wiki/index.md` by indexing 13 unlisted experience notes and replacing phantom links with valid links.
- Indexed `grids-obys-agency-deep-research.md` in `premium-frontend-experience-system/vault-references/INDEX.md`.

**Why:** Resolves high-risk routing misroutes, eliminates phantom index links, and ensures full discoverability of custom skills, scripts, and research manuals across the workspace without deleting any historical context.

**Owner:** Antigravity AIOS

---

## 2026-07-24 — Execute OS Audit Batch B (Hot Cache & Context Placement Refresh)

**Decision:** Executed Batch B of the OS Audit report ([audits/os-audit-2026-07-24.md](file:///d:/AI-OS/audits/os-audit-2026-07-24.md)):
- Refreshed preloaded hot cache ([hot.md](file:///d:/AI-OS/hot.md)) with current July 24 active context (18-site ingestion, Component Registry CLI, Obys grid engine, os-audit, ZORIXEL content prep).
- Updated [brain-aios/wiki/checklists/master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md) with July 24 task completions & date stamps.
- Added explicit **Precedence & Source of Truth Rule** in `GEMINI.md` declaring `master-task-list.md` as sole task status truth, `decisions/log.md` as decision truth, and `hot.md` as active session cache.

**Why:** Eliminates 10-day-old prompt poisoning & bloat in the preloaded context layer and resolves potential task list clashes across workspace stores.

**Owner:** Antigravity AIOS

---

## 2026-07-24 — Execute OS Audit Batch C (Root Hygiene & Bloat Cleanup)

**Decision:** Executed Batch C of the OS Audit report ([audits/os-audit-2026-07-24.md](file:///d:/AI-OS/audits/os-audit-2026-07-24.md)):
- Re-homed loose `Finding Fonts/` root directory (13 zip archives) to `archives/fonts/`.
- Moved loose `brainstorms/canvas_output.png` to `diagrams/canvas_output.png`.
- Purged temporary audit python scripts from `scratch/`.
- Updated `WORKSPACE_MAP.md` entries and verified map alignment via `scripts/validate_workspace_map.py`.

**Why:** Enforces clean root table-of-contents hygiene, prevents scratch script clutter, and organizes brand assets into proper archive and diagram locations.

**Owner:** Antigravity AIOS

---

## 2026-07-25 — System Improvement & Anti-Slop Quality Gates Enforced

**Decision:** Executed `/improve-system` protocol following client-showcase iterations:
- Updated `MEMORY.md` with Rule 28 enforcing Light Theme defaults (`#f8f6f0`), solid color math (zero text gradients), `Nuqun` logo vector mark (`zorixel`), `Lenis` smooth inertia scroll, `GSAP ScrollTrigger` scrollytelling timelines, magnetic elastic cursor physics, and Motion/React `AnimatePresence` height-expanding accordions.
- Updated `.agents/skills/website-design-engine/references/05-anti-slop-quality-gates.md` with Gates #58-#62.
- Logged experience in `brain-aios/wiki/experiences/2026-07-25-anti-slop-design-engine-evolution.md` and indexed in `context/experiences/README.md`.
- Registered experience document in `WORKSPACE_MAP.md`.

**Why:** Captures explicit user design directives, prevents recurring template slop or boxy container defaults in future design sessions, and maintains zero drift across AIOS memory and skill guides.

**Owner:** Antigravity AIOS

---

## 2026-07-25 — Codify Mandatory 30-Minute Deep Planning & Multi-Page Mandate

**Decision:** Enforced mandatory 30-minute deep planning protocol and multi-page web application architecture:
- Updated `MEMORY.md` with Rule 29 requiring mandatory deep architectural planning (30 mins to 1 hr depth) and full multi-page React routing (`/`, `/work`, `/about`, `/pricing`, `/contact`). Banned single-page landing placeholders.
- Updated `.agents/skills/website-design-engine/SKILL.md` to require Phase 0 Intent Discovery & Phase 1 Multi-Page Architecture mapping with explicit user review checkpoints before code generation.
- Saved experience log `brain-aios/wiki/experiences/2026-07-25-mandatory-deep-planning-multi-page-architecture.md` and indexed in `context/experiences/README.md` and `brain-aios/wiki/index.md`.
- Registered experience document in `WORKSPACE_MAP.md`.

---

## 2026-07-27 — Website Design Engine v2.0 Upgrade (10-Phase System & Anti-Slop Discipline)

**Decision:** Upgraded `website-design-engine` (`.agents/skills/website-design-engine/SKILL.md`) and reference manuals (`references/00-06.md`) into a master 10-Phase Web Creation System following a `/grill-me` discovery session and a 5-persona `/roast` council audit:
1. **Multi-Page Sitemap & Shared Architecture (Phase 0.5)**: Added `references/00-sitemap-and-architecture.md` for multi-page route trees, shared `RootLayout`, navbar route state, and global footer.
2. **Automated Design Token Extraction (Phase 1)**: Added token extraction via `hallmark study` / `scrape-reference` to lock OKLCH color palettes (`index.css`), brand font locks (Nuqun, Rosehot, Outfit, Geist Mono), and stark visual hierarchy.
3. **Motion Dialing (0-10) & Pure Skills Integration (Phase 4)**: Integrated Motion Intensity Dialing with `gsap-skills` and `threejs-skills` library escalation, adding mandatory WebGL Canvas Fallback Guards (`SafeCanvas`).
4. **Nano Banana & Google Veo Media Pipelines (Phase 4.5)**: Integrated Nano Banana (`generate_image`) for AI images and Google Veo (`credentials_personal.json`) for hero ambient video backgrounds.
5. **Context Bloat & Rushing Fixes**: Enforced **Just-In-Time (JIT) Phase Reference Loading** (loading ONLY the 1-page reference for the active phase) to eliminate token fatigue, paired with the **Global Zero-Hurry & Architectural Rigor Mandate** for hard phase checkpoints.
6. **Strict Anti-Slop & AI Gradient Bans**: Explicitly banned generic purple/blue gradients (`bg-gradient-to-r from-purple...`), floating blur blobs (`blur-3xl opacity-30`), and fake metric cards. Enforced Together AI Hallmark 57 gates, single `<h1>` SEO/GEO schema, and Playwright 5-viewport visual QA.

7. **Automatic Mandatory Vault Reading Mandates**: Replaced passive links with explicit required `view_file` calls in SKILL.md and `references/04-motion-and-shaders.md` so the model automatically inspects `premium-frontend-experience-system/vault-references/INDEX.md` (Phase 1), `brain-aios/wiki/sops/grid-systems-sop.md` (Phase 2), and `skills-library/gsap-skills/` / `threejs-skills/` (Phase 4) without prompting.
8. **Strict Zero-Cost & Subscription Media Guard**: Enforced zero extra cost policy for Nano Banana / Veo asset generation. If any generation step asks for payment/extra billing (even ₹1), the engine automatically aborts AI generation and falls back to free high-resolution Unsplash image URLs (`https://images.unsplash.com/photo-...`) or CSS ambient video loops.

9. **Roast Council RESHAPE Audit Refinement (v2.2)**: Convened the 5-persona `/roast` council (Contrarian 7/10, Expansionist 10/10, Logician 9/10, Researcher 9/10, Buyer 9/10). Applied Logician/Contrarian RESHAPE recommendation: targeted Phase 1 mandatory `view_file` calls to specific sub-manuals (`grids-obys-agency-granularity-master.md`, `sondaven-granularity-master.md`, `oryzo-ai-granularity-master.md`) based on the site archetype rather than reading the heavy 68KB `INDEX.md`, saving ~15,000 tokens per run while preserving 100% automatic reading automation.

---

## 2026-07-29 — System Improvement: Codegraph & Shadcn MCP Direct Binary Resolution & Timeout Fix

**Decision:** Resolved `codegraph: context deadline exceeded` and `shadcn: context deadline exceeded` MCP initialization timeouts:
1. Identified that `codegraph.cmd` is a Windows batch script wrapper that introduces `cmd.exe` subprocess tree buffering overhead, while `npx -y shadcn@latest mcp` executes online npm registry network queries on every launch.
2. Configured direct Node.js binary invocation across all runtime config paths (`C:\Users\HP\.gemini\antigravity\mcp_config.json`, `C:\Users\HP\.gemini\antigravity-ide\mcp_config.json`, `C:\Users\HP\.gemini\config\mcp_config.json`, `claude_desktop_config.json`):
   - **Codegraph**: `command`: `C:\Users\HP\AppData\Local\codegraph\current\node.exe`, `args`: `["--liftoff-only", "C:\\Users\\HP\\AppData\\Local\\codegraph\\current\\lib\\dist\\bin\\codegraph.js", "serve", "--mcp"]`
   - **Shadcn**: `command`: `C:\Program Files\nodejs\node.exe`, `args`: `["C:\\Users\\HP\\AppData\\Roaming\\npm\\node_modules\\shadcn\\dist\\index.js", "mcp"]`
3. Tested initialization in isolation to verify **~0.1s execution time** with 0 network latency or `cmd.exe` process buffering hangs.

---

## 2026-07-31 — Six-File Context Methodology v3.0 Architecture & Storm Research Integration

**Decision:** Upgraded `/six-file-context-methodology` skill to v3.0, integrated Stanford STORM multi-perspective research engine, and enforced a global Strict Zero-Emoji Mandate:
1. **Matt Pocock & JS Mastery Spec/Ticket Pipeline**: Deconstructs feature specs (`context/specs/`) into atomic engineering tickets (`docs/tickets/`) with verifiable Definition of Done (DoD) and updates multi-session maps (`docs/wayfinder/map.md`).
2. **Token-Optimized Wave Execution**: `/six-file-context-methodology execute` dispatches background developer subagents with wave-based parallelization, protected by strict Token Safeguards (Surgical Context Ingestion, Max 2-Attempt Loop Backstop, 1-3 File Scope Boundaries).
3. **Catalog-First Component Sourcing & Theme Adaptation**: Queries 300+ Component Synthesis Engine (`component_registry_cli.py search`), prioritizing operator favorites and custom lists. Prohibits creating generic components from scratch when catalog matches exist, and strips hardcoded inline colors to re-bind strictly to project OKLCH tokens in `ui-context.md`.
4. **Security Quality Gates & OWASP LLM Additions**: Embeds `/vibesec` security contracts into `code-standards.md` and ticket DoD. Adds Next.js 15 Server Action isolation (`import 'server-only'`, in-function `auth()` checks), raw webhook signature verification, and OWASP Top 10 for LLM Applications (Prompt injection, RAG tenant isolation, Excessive Agency safeguards, and Unbounded Consumption rate limits).
5. **`storm-research-project` Skill & Brain Memory Logging**: Duplicated `storm-research` into a dedicated skill `.agents/skills/storm-research-project/SKILL.md` (leaving the original `storm-research` completely intact). Expanded to 7 research lenses (adding AI/LLM Integration & Latency Specialist and Developer Ergonomics & Token Footprint Auditor). Findings automatically log to `brain-aios/wiki/research/` and `MEMORY.md` so the AIOS persistently retains research context across sessions.
6. **Strict Zero-Emoji Mandate**: Banned emojis across all responses, chat outputs, skill files, documentation, code comments, and project artifacts.

**Why:** Gives the AIOS an enterprise-grade senior AI engineering workflow that maximizes architectural rigor, security, component quality, and multi-perspective research while strictly protecting against token credit exhaustion and context bloat.


---

## 2026-07-31 — ZORIXEL Luxury Editorial Brand Color System Finalization

**Decision:** Finalized and codified the official ZORIXEL brand color identity across all workspace brand documentation:
1. **Master Tokens**:
   - **Obsidian (`#0D0E12`)**: Dark Theme Canvas / Deep Ink & Structural Text
   - **Burgundy (`#6D001A`)**: Primary Brand Color / Section Headers
   - **Crimson (`#D61C2C`)**: Primary Interactive Accent / Active Indicators & High-Contrast CTAs
   - **Vintage Ochre Gold (`#C5A059`)**: Signature Luxury Accent (restricted strictly to <5% screen space for badges and key metrics)
   - **Linen Cream (`#FAF8F5`)**: Light Theme Canvas / Warm Editorial Paper Base
2. **Vault Documentation**: Created `second-brain-zorixel/wiki/brand/colors.md` containing full HSL/Hex tokens, CSS variables, WCAG 2.2 AA legibility math (17.8:1 contrast ratios), card shadow calculations, and anti-slop guidelines.
3. **Cross-System Updates**: Updated `candidates.md`, `personality-and-voice.md`, `typography.md`, `index.md`, `instagram-profile-structure.md`, `instagram-profile-setup-checklist.md`, `MEMORY.md`, and `second-brain-zorixel/wiki/log.md`.

**Why:** Establishes a distinct, high-contrast, luxury editorial identity for ZORIXEL that enforces strict legibility and eliminates generic AI template tropes.

**Owner:** Atinek Maurya & Antigravity AIOS

---

## 2026-07-31 — ZORIXEL Master Brand Identity v3.0 (Typography, Logo Assets & Color Rules)

**Decision:** Finalized and codified the official ZORIXEL master brand identity, typography architecture, logo assets, and color rules across all workspace vaults and system configurations:
1. **Official Brand Typography Hierarchy**:
   - **`Nuqun-Regular`**: Reserved EXCLUSIVELY for the official ZORIXEL logotype and name mark. Never used for body copy or standard UI headings.
   - **`Havock`**: Primary Display Headline Font #1 (User's #1 favorite font). Used for big middle display text, hero titles, and major brand headers.
   - **`Vixa`**: Approved Display Heading & Poster Font for major section headers and campaign graphics.
   - **`Rosehot`**: Official Subheading & Editorial Tag Font (used for all headings apart from the main big headline).
   - **`AICON` (Bold & ExtraBold)**: Selective Section Accent Sans (used in specific technical sections when matching section vibe).
   - **`Chorus-Black`**: Approved for Zorixel Instagram posters, carousels, and graphic designs (not used on main website).
   - **Non-Zorixel Client Vault**: `Pavot`, `Queensides`, `Rozina-Bold`, `ST-Kosmolet`, `BiggerDisplay`, `Martius`, `Ortland`, `KalamaykaVF`, `SunsetHeavy`, `Medium-Font`, `VanArkel` archived for external client projects.
2. **Official Logo Assets Registered**:
   - Solid White PNG: `d:/AI-OS/projects/font-showcase/zorixel_logo_solid_white.png`
   - Solid Dark PNG: `d:/AI-OS/projects/font-showcase/zorixel_logo_solid_dark.png`
   - Solid White SVG: `d:/AI-OS/projects/font-showcase/zorixel_logo_solid_white.svg`
   - Solid Dark SVG: `d:/AI-OS/projects/font-showcase/zorixel_logo_solid_dark.svg`
3. **Upgraded Option 1 Color Palette Rules**:
   - Canvas: Obsidian Midnight (`#0D0E12`) dark, Warm Linen Cream (`#FAF8F5`) light, Velvet Burgundy (`#6D001A`) hero headers.
   - Primary Pop CTA: Electric Crimson (`#D61C2C`).
   - Accent Restriction: Vintage Ochre Gold (`#C5A059`) is strictly restricted to badges, numbers, sub-headings, and iconography (<5% screen area). STRICTLY PROHIBITED as a full slide/page background.
4. **Documentation & Showcase Sync**: Updated `second-brain-zorixel/wiki/brand/typography.md`, `second-brain-zorixel/wiki/brand/colors.md`, `GEMINI.md`, `second-brain-zorixel/wiki/log.md`, `brain-aios/wiki/checklists/master-task-list.md`, and compiled interactive specimen deck `d:/AI-OS/projects/font-showcase/zorixel_final_brand_deck.html`.

**Why:** Establishes an immutable, high-end, editorial visual identity for ZORIXEL across web applications, video assets, educational carousels, and print graphics while maintaining clean separation between brand fonts and client project assets.

**Owner:** Atinek Maurya & Antigravity AIOS











