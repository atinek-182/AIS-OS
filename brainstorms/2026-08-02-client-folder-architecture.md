# Client Vault & Directory Architecture: Discovery & Brainstorm Notes
Date: 2026-08-02 · Goal: Standardize bulletproof client folder structure & lifecycle management system for ZORIXEL AI Agency · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Client Vault Root**: `d:\AI-OS\clients\[ID]-[client-slug]\` (e.g., `clients/001-acme-corp/`).
- **Codebase Topology**: Code projects live as standalone git repos in `projects/Websites/` or `projects/Clients/`, linked via directory junctions into the client folder.
- **Client Handoff Packaging**: Hybrid approach (ZIP exports, Notion Client Portal, transfer of Git repos, and live Vercel/railway deployments).
- **Automation Skill**: We will compile a custom `/new-client` skill that programmatically scaffolds client directory structures and populates canonical markdown templates.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **Client Vault**: The root directory (`clients/[client-id-slug]/`) containing all artifacts, specs, code, and trackers for a specific ZORIXEL client.
- **Client Serial ID**: Standardized 3-digit numerical identifier (e.g. `001`, `002`) combined with client slug for chronological sorting.
- **Pre-Outreach Deep Research**: Cold audit phase (vulnerability extraction, business model analysis, competitor teardown) used to craft high-converting pitch hooks before contact.
- **Internal vs. Client-Facing Boundary**: Strict wall separating internal agency calculations, margin tables, and raw research from clean client handoff deliverables.

## Q&A Log
### Q1 — Folder Naming & Code Topology
- **Captured Decision**: Two-digit numeric prefixes (`01-`, `02-`, etc.) for phase folders. Code repos stored in `projects/` and linked via junctions.
- **Rationale**: Keeps file explorers sorted chronologically while isolating heavy git/node_modules from vault indexers.

### Q2 — Cold Acquisition & Multi-Phase Pipeline Shift
- **Captured Decision**: Client lifecycle is an 8-phase system with a two-stage gated rollout:
  - **Stage 1 (Lead / Audit Stage)**: Scaffolds `01-pre-outreach-audit/` and `02-proposal-and-agreement/`. Works for ALL acquisition channels (inbound website forms, email inquiries, referrals, outbound cold audits).
  - **Stage 2 (Accepted Stage)**: Unlocks `03-post-hire-onboarding/` through `08-retainer-and-tracker/` once the offer is accepted.
- **Rationale**: Keeps unclosed leads clean without wasting disk space or cluttering post-hire project spaces.

### Q3 — Sub-grouped Deliverables Structure
- **Captured Decision**: `06-client-deliverables/` sub-groups assets by component (e.g. `01-web-portal/`, `02-automation-workflow/`, `03-mcp-tools/`).
- **Rationale**: Isolates independent client deliverables for modular handoff.

### Q4 — Continuous Self-Improving Skill Engine
- **Captured Decision**: `/new-client` skill will include an embedded auto-evolution protocol that analyzes completed client sprints and automatically updates canonical templates, directory layouts, and SOPs post-sprint.
- **Rationale**: Ensures the AIOS constantly reduces operator overhead and improves agency automation after every client engagement.

## Final 8-Phase Gated Architecture Blueprint

```
clients/
└── [ID]-[client-slug]/
    ├── STAGE 1: LEAD & SALES GATED (Initial Scaffolding)
    │   ├── 01-pre-outreach-audit/        # Vulnerability map, lead source metadata, teardown notes
    │   └── 02-proposal-and-agreement/    # 3-Option Proposal, pricing calculations, contract & NDA
    │
    └── STAGE 2: ACCEPTED & BUILD GATED (Unlocked on Deal Acceptance)
        ├── 03-post-hire-onboarding/      # Credentials, internal SOPs, workflow teardowns, raw data
        ├── 04-architecture-and-specs/    # Agentic workflows, MCP specs, system architecture, UI specs
        ├── 05-development-and-build/     # Build sprint logs, prompt chains, VibeSec audit, code junction
        ├── 06-client-deliverables/       # Sub-grouped handoff packages (01-web-app/, 02-mcp/, etc.)
        ├── 07-training-and-offboarding/  # Training session notes, handover videos, sign-off certificate
        └── 08-retainer-and-tracker/      # Internal ROI log, monthly maintenance, upsell roadmap
```


