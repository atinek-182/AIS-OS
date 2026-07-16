# Premium Frontend System Restructuring: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Restructure the Premium Frontend Experience System to eliminate duplication, simplify configuration size for AIOS consumption, configure new MCPs (Figma, Flowbite, shadcn), download Three.js/WebGL/GSAP skills, and align with AIOS operational workflows.

## Summary / key decisions
- **Scope**: Re-organizing the 10 root markdown files of `premium-frontend-experience-system/` into 4 core files to optimize token footprint and reduce developer friction.
- **MCP Integration**: Adding official `shadcn` and `flowbite-mcp` globally in `mcp_config.json`. Figma is skipped per user's preference.
- **Global Skill Integration**: Copying and consolidating Three.js and WebGL best practices from `CloudAI-X/threejs-skills` to a new global skill `threejs-webgl` under `C:\Users\HP\.gemini\config\skills\threejs-webgl\`.
- **QA Automation**: Creating `scripts/verify_design_milestone.py` to automate builds, Playwright console audits, and multi-viewport responsive screenshot renders.

## Q&A log
### Q1 — Root File Restructuring
- **Asked**: How should we restructure the 10 root markdown files of the design system to eliminate duplication and keep it lightweight for the AIOS?
- **Captured**: Option 1 approved with conditions. We will consolidate the 10 root files into 4 high-leverage core files: `AGENTS.md` (Identity & Prompting), `POLICIES.md` (Component, Motion, WebGL), `WORKFLOWS_AND_QA.md` (Workflows & QA Checklists), and `INTAKE_AND_REFERENCES.md` (Q&A & Reference Auditing). The consolidation must retain all granular checks, references, and questions, but simplify the formatting so the AIOS can consume it efficiently without redundancy.
- **Flags**: None.

### Q2 — MCP Server Selection
- **Asked**: Which of the new MCP servers (shadcn, flowbite-mcp, and figma) should we configure globally, and how should we handle the Figma API token?
- **Captured**: The user does not use Figma and does not want to set up the Figma MCP server. Only configure `shadcn` and `flowbite` globally in `mcp_config.json`.
- **Flags**: None.

### Q3 — Three.js / WebGL Custom Skill
- **Asked**: How should we handle the Three.js and WebGL coding guidelines? Should we create a new global custom skill `threejs-webgl`?
- **Captured**: Approved recommended strategy. We will create a new global custom skill `threejs-webgl` under the config folder containing guidelines for Three.js, React Three Fiber, GLSL shaders, and fallback rendering.
- **Flags**: None.

### Q4 — QA Automation
- **Asked**: Should we create an automated verification script `scripts/verify_design_milestone.py` to automate our responsive and console QA audits?
- **Captured**: Approved recommended strategy. We will create `scripts/verify_design_milestone.py` in the workspace to automate project building, Playwright console audits, and generating responsive screenshots at all 5 breakpoints.
- **Flags**: None.

### Q5 — Design Token Specifications
- **Asked**: Should we define concrete design tokens (like premium cubic-bezier easing curves, grid column rules, and type scales) directly in `POLICIES.md`?
- **Captured**: Approved recommended strategy. We will add a dedicated Design Token Specifications section inside `POLICIES.md` to define standard cubic-bezier curves (e.g. premium slow, tactile hover), grid layout columns, and font hierarchy rules.
- **Flags**: None.

### Q6 — Search-first and Roast Check
- **Asked**: Are there any other requirements or additions you want to make before we proceed to writing the implementation plan?
- **Captured**: Search the web for existing skills first, copy their best practices, then refine and combine them with our own. Run the Roast skill to identify gaps.
- **Flags**: None.

## Open flags (pending input)
- None. All Q&A branches resolved.

---

## Restructuring Stage 2 Q&A Log
### Q1 — Static Three.js & GSAP Skills Sourcing
- **Asked**: Should we save the community `threejs-skills` repository modules into `brain-aios/wiki/research/skills-library/` as static reference files?
- **Captured**: Yes. We will clone the full 10-module `threejs-skills` repository and save it statically under `brain-aios/wiki/research/skills-library/threejs-skills/`. We will also search the web for additional GSAP developer skills/prompts and copy them there.
- **Flags**: None.

### Q2 — Playwright Reference Ingestion
- **Asked**: Should we create an automated Playwright crawler script `scripts/fetch_ui_reference.js` to automate our reference and component documentation intake?
- **Captured**: No. The user prefers using the global Playwright MCP browser tools manually in their chat session to inspect links and copy component references rather than relying on a custom command-line crawler script.
- **Flags**: None.

### Q3 — Playwright Audit Instructions in Workflows
- **Asked**: Should we add instructions in `WORKFLOWS_AND_QA.md` on how to manually use global Playwright MCP tools for visual styling audits?
- **Captured**: Approved recommended strategy. We will add a dedicated section inside `WORKFLOWS_AND_QA.md` outlining how to start a local server and call Playwright MCP tools manually to visually verify components and check console message logs during development.
- **Flags**: None.

---

## Adversarial Roast (Self-Roast Verdict)

### THE VERDICT: RESHAPE
**Confidence**: High

**The call in one line**: Consolidate the design vault into 4 highly-structured files, add the Three.js global skill, and automate the QA checkpoints, but ensure we maintain a strict fast-track bypass to prevent procedural gridlock on small changes.

**Why**: Consolidating 10 files into 4 reduces LLM prompt tokens and prevents context dilution, but if those 4 files become too long, we will exceed the 800-line viewing limits of our development tools. We must use tight, clear, hierarchical markdown headers. The automated verification script will save hours of manual QA.

**Biggest Risk**: The `threejs-webgl` skill must contain React Three Fiber (R3F) specific warnings (such as preventing canvas hydration errors in SSR/Next.js and ensuring proper WebGL context disposal), otherwise we will introduce memory leaks in advanced builds.
**Biggest Upside**: Establishing a clear "Design Token" standard and a one-click verification script guarantees that any website we build will have premium motion and layout out-of-the-box.

**Cheapest 48-hour test**: Write the consolidated `AGENTS.md` and `POLICIES.md` first, run our workspace validator script, and write the custom global `threejs-webgl` skill file, checking that it correctly loads under our active skills.
