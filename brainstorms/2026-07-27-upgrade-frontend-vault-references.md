# Upgrade Frontend Vault References: Brainstorm / Discovery Notes
Date: 2026-07-27 · Goal: Upgrade, expand, and structure design references, component registries, UI patterns, granularity masters, dedicated reference vaults, and AIOS skill integration in the Frontend Experience System.

## Summary / key decisions
- **Roadmap Sequence**: 3-Phase Execution + 2 Dedicated Vaults + AIOS Skill Integration:
  1. **Phase 1: High-Signal UI Pattern & Component Registry Expansion** (300+ components indexed across 11 sources + Refero/Mobbin pattern taxonomy + `component_registry_cli.py adapt` CLI tool).
  2. **Phase 2: Deconstruction Engine Upgrade & Awwwards Agency Granularity Masters Sweep** (GLSL shader hooks, GSAP timeline parser, 3D asset interceptor, automated wireframe compiler, and Unbounded Component Extractor).
  3. **Phase 3: Dual Dedicated Vault Architecture**:
     - **Structured Component Vault** (`premium-frontend-experience-system/references/component-vault/`): Structured folder hierarchy (`navigation/`, `heroes/`, `cards/`, `scrollytelling/`, `forms/`, `footers/`, `modals/`, `3d-widgets/`).
     - **Dedicated Shader & Canvas Physics Vault** (`premium-frontend-experience-system/references/shader-canvas-vault/`).
  4. **AIOS & Web Design Skill Auto-Sync**: Update `.agents/skills/website-design-engine/SKILL.md`, `/scrape-reference`, `/design-direction`, `AGENTS.md`, and `WORKSPACE_MAP.md` so all AIOS skills query, reference, and build with these expanded component & shader vaults automatically.

## Q&A log

### Q1 — Primary Upgrade Roadmap Focus
- **Asked**: Which core pillar do you want to prioritize first for upgrading the Frontend Vault references?
- **Captured**: Execute Phase 1 (Component Registries & UI Patterns) first, followed by Phase 2 (Granularity Masters Sweep), then Phase 3 (Shader & Canvas Physics Vault). Conduct exhaustive Q&A for each phase.
- **Flags**: None.

### Q2 — Component Registry & Taxonomy Architecture
- **Asked**: How should we structure the component registry expansion in `premium-frontend-experience-system/source-registries/`?
- **Captured**: Option 1 — Full Registry Expansion + UX Pattern Taxonomy (Refero/Mobbin buckets) + CLI Auto-Adapter tooling.
- **Flags**: None.

### Q3 — Candidate Source Selection (Phase 1)
- **Asked**: Which of these sources should we officially add to our Component Registry Index and Master Catalog?
- **Captured**: Option 1 — Add ALL 7 candidate sources: Magic UI, 21st.dev, Motion Primitives, React Bits, Origin UI, Kokonut UI / Cult UI, and Uiverse.
- **Flags**: Phase 1 specifications confirmed.

### Q4 — Phase 2 Granularity Targets & Deconstruct Upgrade Sequence
- **Asked**: Which target award-winning sites should we deconstruct in our Phase 2 Granularity Masters Sweep?
- **Captured**: Option 1 selected (TRIONN Agency, Resn, Active Theory, Locomotive, Merci Michel, Bruno Simon). User requested upgrading the site deconstruct engine and `/scrape-reference` skill FIRST before running the sweep.
- **Flags**: None.

### Q5 — Deconstruction Engine Upgrade & Unbounded Component Extraction Rule
- **Asked**: Which enhancements should we build into the upgraded `/scrape-reference` and `scrape_full_site_mirror.py` engine?
- **Captured**: Option 1 (Full Engine Upgrade: GLSL shader hooks, GSAP parser, 3D asset interceptor, automated wireframe compiler). User specifically clarified: **Do NOT limit component extraction to 5 components — upgrade the extractor so EVERY unique and great component on the target site is extracted into `code-extracts/components/` as drop-in React + TypeScript (`.tsx`) code.**
- **Flags**: Phase 2 specifications confirmed.

### Q6 — Dedicated Shader & Canvas Physics Vault Architecture (Phase 3)
- **Asked**: How should we structure and populate the Phase 3 Shader & Canvas Physics Vault?
- **Captured**: Option 1 — Full 4-Module Shader Vault (GLSL Catalog + R3F Drei Wrappers + Scroll/Cursor Physics + WebGPU/TSL Guide) under `references/shader-canvas-vault/`.
- **Flags**: None.

### Q7 — Structured Component Vault Creation
- **Asked**: User requested creating a dedicated, structured vault for components similar to `shader-canvas-vault`.
- **Captured**: Build `premium-frontend-experience-system/references/component-vault/` structured into clean category subdirectories (`navigation/`, `heroes/`, `cards/`, `scrollytelling/`, `forms/`, `footers/`, `modals/`, `3d-widgets/`). Each entry contains raw `.tsx` code, props schema, variant options, and Tailwind v4 design token maps.
- **Flags**: None.

### Q8 — AIOS & Web Design Skills Integration Mandate
- **Asked**: User explicitly instructed: *"make sure the aios and web design skill also learn everything"*.
- **Captured**: Update `.agents/skills/website-design-engine/SKILL.md`, `/scrape-reference`, `/design-direction`, `/hallmark`, `AGENTS.md`, and `WORKSPACE_MAP.md` to automatically bind, query, and enforce the Structured Component Vault, Shader Vault, and upgraded CLI adapter across all web creation workflows.
- **Flags**: All decisions complete. Ready for implementation plan.

## Open flags (pending input)
- None. Ready for implementation planning and execution.








