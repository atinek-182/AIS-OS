---
name: client-audit
description: Autonomous 1-Line Client Outreach Audit & Research Engine for ZORIXEL. Automatically scaffolds client vaults, scrapes target websites, populates vulnerability audits, generates forensic research prompts, synthesizes 7-agent STORM reports, generates Mobile Loom Cheat Sheets, and builds Notion Operational OS master plans inside client vaults in one line.
argument-hint: '[Client Name] [Website URL] [optional: lead channel / context notes]'
---

# ZORIXEL 1-Line Client Audit & Research Engine (`/client-audit`)

## Overview & Tri-Mode Execution

This skill automates Stage 1 client lead discovery, web scraping, vulnerability auditing, forensic research prompt generation, 7-agent STORM research, Mobile Loom Cheat Sheet creation, Notion Operational OS blueprinting, and 5-persona `/roast` validation in **one single command**.

Invokable via:
- **Slash Command**: `/client-audit "[Client Name]" [Website URL] [optional notes]`
- **Dynamic Intent**: Triggered automatically when the user shares a new client URL or asks to audit a prospect.
- **Programmatic Inter-Skill Calling**: Programmatically invokable by `/new-client`, `/new-project`, and `/ingest-repo`.

---

## Generic 1-Line Execution Pipeline

When invoked with any client (e.g. `/client-audit "[Client Name]" [Website URL] [context]`):

### Step 1: Client Vault Scaffolding & Placement Mandate
- Runs `python scripts/new_client_runner.py lead "[Client Name]"`.
- All generated pitch scripts, cheat sheets, blueprints, and audit documents MUST be stored strictly inside the designated client vault directory: `clients/[ID]-[slug]/01-pre-outreach-audit/` (never in generic root or `brainstorms/` folders).

### Step 2: Autonomous Web Scrape & Technical Inspection
- Scrapes the target website and linked sub-pages using Scrapling / `scrape_web`.
- Evaluates:
  - Technical Debt & Page Load Performance (unminified assets, heavy raster images, missing viewport tags).
  - Web UI & Link Integrity (broken anchor links, 500/404 errors, un-rendered widgets).
  - SEO & Structured Data (missing meta tags, missing Schema.org JSON-LD, missing Google Scholar tags for academic sites).
  - Lead Intake Friction: Detects if prospects intake via phone calls, web forms, or chat apps.

### Step 3: Pre-Outreach Vulnerability Audit (`AUDIT.md`)
- Fills out `clients/[ID]-[slug]/01-pre-outreach-audit/AUDIT.md` with:
  - Lead acquisition channel metadata (Warm Referral, Cold Outbound, Inbound).
  - Core business model & revenue drivers.
  - Quantified wasted time & revenue leakage estimates (staff hours lost/mo, candidate dropoff rate).
  - 50-Capability AI Transformation Roadmap customized for the client's industry niche.

### Step 4: Forensic Deep Research Prompt Generation
- Creates `01-pre-outreach-audit/CHATGPT_DEEP_RESEARCH_PROMPT.md` pre-populated with target URLs, leadership info, technical teardown criteria, and a 50-capability AI automation roadmap request.

### Step 5: Notion Operational OS Blueprinting (`NOTION_WORKFLOW_MASTER_PLAN.md`)
- Analyzes the founder's intake habit (Phone Calls vs Web Forms):
  - For **Phone Call Intake**: Designs a 30-second Notion Call Intake Form + Employee Task Dispatcher + Auto-Progress Bars.
  - For **Web Form / Chat Intake**: Designs an Automated Web Screening Widget + CRM Auto-Sync Workflow.
- Includes clean `[PLACEHOLDER: Pending Client/Lead Specific Inputs]` tags for service offerings and team roles.

### Step 6: Mobile-Optimized Loom Cheat Sheet (`LOOM_MOBILE_CHEAT_SHEET.md`)
- Generates a concise bullet cheat sheet formatted for phone screen viewing during video recording:
  - **Stage 1: Respectful Hook**: Warm greeting, acquisition channel reference, ₹0 free pilot guarantee.
  - **Stage 2: Operational Friction Callout**: Highlighting mental burden (paper notes, manual verbal handoffs, repeated staff follow-ups).
  - **Stage 3: Live Solution Demo**: Demonstrating the Notion Intake Tool or Web Screening Widget.
  - **Stage 4: Website & Indexing Gaps**: Live screen share showing broken links and missing meta tags.
  - **Stage 5: Low-Friction Call to Action**: Inviting the lead to a 30-minute Zoom strategy call (Zero Upfront Charge Guarantee).

### Step 7: 5-Persona Adversarial Roast Audit (`/roast`)
- Programmatically runs the 5-persona `/roast` council (Contrarian, Expansionist, Logician, Researcher, Buyer) on the operational architecture and appends the GO / RESHAPE / KILL verdict directly into `NOTION_WORKFLOW_MASTER_PLAN.md`.

### Step 8: 7-Agent STORM Research Synthesis (`storm-research-project`)
- Executes the 7-lens expert council (Systems Architect, Vibesec Security Pen-Tester, DB/Scaling Specialist, Frontend UX Lead, Product Economist, AI Specialist, Developer Ergonomics Auditor).
- Saves the interactive briefing report to `storm-reports/[client-slug]-briefing.html` adhering strictly to ZORIXEL Master Brand Identity v3.0 (Obsidian Midnight, Velvet Burgundy, Crimson CTA, zero gradients, zero glassmorphism).

---

## Inter-Skill Connections
- **Lead Scaffolding**: Calls `/new-client`.
- **Adversarial Audit**: Calls `/roast`.
- **Deep Research**: Calls `/storm-research-project`.
- **Pricing Engine**: Feeds into `/ai-pricing-engine` for proposals.
- **Quality Gates**: Integrated with `/hallmark` and `/vibesec`.

---

## Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

