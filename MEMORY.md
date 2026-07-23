# ZORIXEL AIOS Persistent Memory

This file logs cross-session learnings, operational preferences, and recurring contexts to prevent knowledge decay and optimize context limits.

---

## 🧠 Core Identity & Context
- **Operator:** Atinek Maurya (Aspiring Web Designer/Developer, AI Automation Builder, and Digital Creator).
- **Brand Goal:** Launch ZORIXEL (educational brand for web design and AI tools) and build a sellable AI automation (Q4 target: ₹1,00,000 revenue in 2026).
- **Obsidian Vaults:**
  - `brain-aios/` -> General AI OS hub and checklist vault.
  - `second-brain-zorixel/` -> ZORIXEL content drafts and research.

---

## 🛠️ Global Environment & Integrations
- **Credentials Config:** Google Workspace CLI (`gws`) uses dual profiles. Personal context matches Personal json credentials; Brand context matches Brand json credentials.
- **Ecosystem Focus:** The coding execution environment is strictly **Antigravity**. Verification, tests, and mockups must never be run or checked in the Claude CLI.
- **Marketplaces Configured:** All global coding plugins (`superpowers`, `skill-creator`, `frontend-design`, `context-mode`) are uninstalled from the Claude CLI database and configured under the Antigravity customization path. Persistent memory (`claude-mem`) is installed natively for the Antigravity CLI (`agy`) with its worker daemon running at port 37777 and MCP tools (`search`, `timeline`, `get_observations`) registered.
- **Bun Runtime Path:** Standard Bun executable is located at `C:\Users\HP\.bun\bin\bun.exe` and must be used as the runtime for memory worker tasks.

---

## ⚙️ Operational Rules & Preferences
1. **Default Shift:** Stubbornly refuse to execute repetitive tasks manually. Proactively offer to automate 30% to 75% of them.
2. **Curiosity Rule:** Explain the structural logic, handle empty states, and prevent "dark code" (running unverified black-box commands) rather than just dumping output.
3. **Search-First Adaptation:** When links or guides mention Claude Code, search the web first for native Antigravity ports. Only copy-paste Claude folders as a last resort, and *always* ask for user confirmation first.
4. **Token Optimization:** Proactively clean up folders, keep file logs concise, and organize guides to reduce context overhead.
5. **No Placeholders:** Generate real working assets and layouts. Never use placeholder images.
6. **Local Reference Mirroring & Server Bypasses:** Mirror design references locally. Spin up background Node static servers (e.g. port 3000) to render local HTML files for visual Playwright tests to bypass browser permission blocks.
7. **Diagram Storage Policy:** Always create and save Excalidraw diagrams inside the dedicated `diagrams/` folder at the workspace root instead of cluttering the root workspace directory.
8. **Understand & Verify First Principle:** Never output changes or assert a task is complete without running physical verification (like Playwright browser checks or compilers) and reviewing the outputs. Always check everything before delivering.
9. **Vulnerability, Bloat, & Duplication Auditing:** Before any code is written, conduct a check-first analysis of potential vulnerabilities, bloat code, or duplicate logic.
10. **Grill Me & Roast Prerequisite:** For any new design, feature, or business idea, run or recommend `/grill-me` or `/roast` to define and pressure-test the concept before starting implementation.
11. **Fresh Session Bootup upgrades**: At the start of a new chat or session, before implementing new instructions, check and upgrade custom skills (such as `grill-me` or `roast`) to keep them up to date. Avoid blindly following instructions that conflict with system safety, logic, or clean design standards; stop and clarify first.
12. **Playwright Context & Require Resolutions**: Always execute Playwright Node scripts from the nearest directory containing the local `node_modules` where playwright is installed. Do not execute them in transient scratch folders unless the script manually references the full dependency path.
13. **Order of Variable Declarations**: Review all compiler and scripting modifications to ensure all referenced variables (e.g. customized styling strings or CSS overrides) are fully declared and bound under all conditional code branches before they are accessed.
14. **No Compiler Changes Without Regression QA**: When modifying a builder script, compiler, or shared stylesheet, execute a Playwright visual QA screenshot sweep of a representative set of layouts (not just the target file) across all 5 responsive viewports to verify no regressions in text-wrapping, scaling, or spacing.
15. **Figma Compiler, SVG Geometry, & Secrets Hygiene Rules**: Always filter `visible: false` nodes when compiling Figma JSON; never apply CSS `transform: rotate(...)` to Figma-exported graphic SVGs (scope rotation to HTML text nodes only); convert inline SVG `style="..."` strings into camelCase JSX style objects (`style={{...}}`); and strip hardcoded secrets or API tokens from workspace scripts.
16. **Scrapling Web Scraping & Stealth Data Extraction**: Use `/scrape-web` (powered by `scripts/scrapling_runner.py`) for fast HTTP parsing, anti-bot stealth scraping, and dynamic DOM element extraction. Ensure `scrapling`, `curl_cffi`, and `browserforge` are installed together. Reserved `/scrape-reference` for full offline visual asset cloning (CSS, fonts, 3D models).
17. **Repository Ingestion & Automatic Skills-Library Search Engine**: Use `/ingest-repo` (or `/ingest-skills`) to clone, security audit, compare, roast via 5 personas, and adapt any GitHub repo into active scripts/skills. The AI agent MUST automatically check and scan all reference manuals in `brain-aios/wiki/research/skills-library/` whenever relevant without prompting the user. Force-delete temporary scratch clones (`scratch/ingest-[repo]/`) post-ingestion.
18. **Agent Reach Unified Internet & Multi-Platform Research**: Use `/agent-reach` (`scripts/agent_reach_runner.py`) for multi-backend internet search, YouTube transcript extraction, Bilibili video research, V2EX tech feeds, GitHub repo search, and Reddit community sentiment. Use `agent-reach doctor` to verify channel health.
19. **Hallmark Anti-AI-Slop Design & Verification Engine**: Use `/hallmark` (`scripts/hallmark_runner.py`) when building frontend interfaces to enforce structural variety (21 macrostructures, 20 color themes, OKLCH palettes, 57 anti-slop test gates). Perform pre-emit self-critique scores before handing back design outputs.
20. **Dot-to-Dot Technical Rigor & Unbounded Discovery**: Refuse high-level textual summaries or superficial name-dropping. Analyze, extract, and document every single micro and macro web decision (from meta tags, OpenGraph ratios, scrollbar width calculations down to GLSL fragment shaders and page transition cleanups). Example lists are non-exhaustive sample illustrations; proactively inspect and discover EVERY SINGLE novel element on the target.
21. **Sequential One-by-One Queue Discipline**: When processing a queue of items (such as the 18 reference websites queue), process EXACTLY ONE SITE AT A TIME. Complete site $N$ fully, present all raw file links, update queue tracking, and STOP to await explicit user confirmation before touching site $N+1$.
22. **Hyper-Detailed Visual UI/UX Wireframes**: Never output basic placeholder shapes or raw Excalidraw JSON strings for wireframe requests. All reference site ingestion wireframes MUST be hyper-detailed, section-by-section HTML visual pages (`wireframe.html`) and Playwright screenshots (`wireframe.png`) containing real site copy, real headlines, component spec tags (`COMPONENT: HEADER / NAV SYSTEM`), 3D stage boxes (`canvas#canvas`), 12-column grid overlays, and explicit technical annotations.


---


## 🎨 Zorixel Design Taste & Visual Guidelines
- **Visual Identity (Light Editorial)**: The brand uses a premium print Editorial Magazine theme: warm linen off-white paper canvas background (`#fbfaf7`), dark charcoal text (`#141413`), and very sparse brand coral highlights (`#ff6b4a` - under 10% screen space).
- **Typography Scale & Finalized Font System**:
  - **Core Brand Logo**: lowercase `"zorixel"` in `Nuqun` regular, bold weight, with wide letter-spacing (`0.05em`) and cyan/red chromatic aberration (RGB split) effect.
  - **Editorial & Section Headings**: `Rosehot` (Title Case or Sentence Case, never all-caps or all-lowercase).
  - **Poster & Creative Headings**: `Vixa` (Title Case, 2-5 words max, massive size `90px`+ only, no small text).
  - **Long-form & Body Copy**: `Outfit` (Sentence Case, size `16px`-`19px`, `line-height: 1.6` for clean reading legibility).
  - **Monospace Metrics & Dashboard Cards**: `Space Mono` (monospace typeface to prevent clumped layout numbers).
- **Card Panels (Diffused Paper Sheets)**: Comparison blocks and modules must be styled as pure white card panels (`#ffffff`) floating with highly diffused, soft shadows (`box-shadow: 0 20px 48px rgba(20, 20, 19, 0.04)`) and rounded corners (`12px`). Avoid thick borders or raw borderless flat text panels.
- **Top Safe Zones**: Standard safe-offset of at least `120px` to clear top absolute header overlays.
- **CTA Contrast**: Buttons must use high-contrast solid backgrounds with white text.
- **AI Slop Bans**: Never use standard SaaS-cream colors, default card outlines, emoji icons, uppercase tracked eyebrows, or generic sequential numbering prefixes (01 / 02) unless representing an actual ordered process.
- **Headless Font Loading & SVG Outlines (Rule 8)**: When rendering local fonts in headless tests/renders, always encode font files to base64 Data URIs to prevent browser sandbox fallback. To emulate synthetic bolding and custom letter-spacing in vector SVGs, manually compile outline paths using custom glyph offsets and stroke properties.

