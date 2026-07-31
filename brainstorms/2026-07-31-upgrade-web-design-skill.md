# Upgrade Web Design Skill (`website-design-engine`): Socratic Discovery & Brainstorm Notes
Date: 2026-07-31 · Goal: Upgrade and refine the Master Web Design Engine (`website-design-engine` skill and supporting frontend experience system) · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Upgrade Scope**: Selected **Option D: Comprehensive Master Upgrade (v3.0 Evolution)** with custom architectural constraints.
- **`website-design-engine` Status**: Successfully upgraded to v3.0 in `.agents/skills/website-design-engine/SKILL.md`.
- **`six-file-context-methodology` Status**: Successfully upgraded to v3.1 in `.agents/skills/six-file-context-methodology/SKILL.md`.
- **Layout & Wireframing Policy**: Removed automatic wireframe generation from pipeline. Wireframes and component layouts are explicitly specified via project context files using the **Six-File Context Methodology** (`six-file-context-methodology`).
- **Shader Library Integration & Protocol**: Standardized `radiant-shaders` (`https://radiant-shaders.com/gallery/`, `https://github.com/pbakaus/radiant`) as primary WebGL shader reference. Never auto-generate `.tsx` shader components blindly. Always ask user first if shader is needed and which one; user provides the HTML file from gallery in project `reference/`, and AI extracts code from that.
- **Reference Folder Priority Pipeline**: Enforced project-local `reference/` (or `references/`) directory inside every project as **#1 Priority Source of Truth** scanned at start of Phase 1.
- **Categorized Favorite Component Precedence**: Maintained category structure in `component-registry-index.json` (hero, nav, bento, cards, pricing, etc.) with `"favorite": true` tags so search CLI ranks favorite components first within each category.
- **Slow & Methodical Zero-Hurry Execution**: Made changes step-by-step, asking the user on any doubt.
- **Cross-Skill Handoff to Six-File Methodology**: Updated `six-file-context-methodology` skill files to enforce `reference/` folder creation and synced 4-level component priority chain.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **Website Design Engine v3.0**: Upgraded master web creation engine incorporating local `reference/` priority, Six-File layout control, user-provided HTML `radiant-shaders` extraction, and categorized favorite component precedence.
- **Local Reference Vault**: Project-level `reference/` folder containing user visual assets, recordings, HTML files, code snippets, and style references.
- **Categorized Favorite Index**: Tagged entries in `component-registry-index.json` prioritized per component category.

## Q&A Log
### Q1 — Scope & Architectural Vision
- **Asked**: What is the primary focus of this Web Design Skill upgrade?
- **Captured**: User selected Option D (Comprehensive Master Upgrade) with critical customizations:
  1. No automatic wireframes (driven by Six-File Context Methodology).
  2. Native integration of `radiant-shaders` (`https://github.com/pbakaus/radiant`).
  3. Mandatory project-local `reference/` folder as #1 Priority Source of Truth before checking the 300+ catalog.
  4. Precedence for user's favorite components.

### Q2 — Local Reference Parsing, Categorized Favorites & Radiant Shaders Protocol
- **Asked**: How to structure Local `reference/` parsing, Favorite Components tagging, and Radiant Shaders ingestion?
- **Captured**:
  1. **Area 1 (Local `reference/` Scanning)**: Automatically scan `reference/` at Phase 1 start. If `.png`/`.mp4` or `.md`/`.html`/`.tsx` exist, analyze them first before writing code.
  2. **Area 2 (Categorized Favorites)**: Add `"favorite": true` while preserving existing category structures (hero, bento, nav, etc.) in `component-registry-index.json`.
  3. **Area 3 (Radiant Shaders Interactive Protocol)**: Do NOT generate `.tsx` shader wrappers blindly. AI must ask user first if shader is needed and which one. User drops HTML file into `reference/`, and AI extracts shader code from that HTML file.
  4. **Pacing & Cross-Skill Sync**: Proceed slowly and methodically, asking on any doubt. Upon completing `website-design-engine` upgrade, propagate workflow updates into `six-file-context-methodology` skill files.

### Q3 — Execution Order & Approval
- **Asked**: Proceed step-by-step with Option A (update `website-design-engine/SKILL.md` first, inspect together, then update `six-file-context-methodology/SKILL.md`)?
- **Captured**: User selected Option A. Updated `website-design-engine/SKILL.md` to v3.0 and `six-file-context-methodology/SKILL.md` to v3.1 successfully.

## Open Flags & Deferred Decisions
- [x] Update `website-design-engine/SKILL.md` to v3.0.
- [x] Update `six-file-context-methodology/SKILL.md` to v3.1 to mandate `reference/` folder creation and sync component priority chain.
- [x] Update WORKSPACE_MAP.md if required.
