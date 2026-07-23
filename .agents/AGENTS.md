# Workspace Rules

## Maintenance of WORKSPACE_MAP.md

- When creating a new folder, junction, or config file (like adding an MCP server or utility script), you MUST update [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) immediately before concluding the task.

## System Self-Improvement
- Suggest invoking `/improve-system` when:
  - A custom skill's output is iterated upon or corrected multiple times.
  - A significant lesson, decision, or business story is shared by the user.
  - Do NOT suggest it for minor syntax fixes or small one-off file edits. Suggest it only for high-leverage changes.

## Adapting Skills to Antigravity & Gemini
- Whenever reading or invoking any custom skill, prompt, or reference guide (especially those originally written for Claude Code, Cursor, or other AI agents):
  1. Scan the contents for platform-specific references (e.g., `Claude`, `Claude Code`, `Cursor`, `.claude/skills/`) and dynamically adapt them to `Antigravity` or `Gemini` equivalents.
  2. Preserve all core execution logic, design frameworks, and copywriting/audit guidelines without changing their meaning or losing their original capabilities.
  3. Run all tests, verifications, and directory-level checks strictly under the Antigravity environment.

## Sandboxed Font Rendering & SVG Outline Layouts
- Never assume local asset files load via `file:///` inside headless browser screenshots (Playwright); always prefer base64 Data URIs for local fonts in temporary HTML pages.
- Double-check that user-finalized fonts (e.g. `Nuqun` logo, `Rosehot` headings, `Outfit` body) are strictly preserved, and avoid switching brand typefaces.

## Visual Regression QA Audits
- **Auditing on compiler modifications**: When changing a builder script, compiler, or shared stylesheet that compiles multiple independent cards/pages, you must execute a Playwright regression visual audit sweep (`verify_micrographics_design.js` or `verify_design_milestone.py`). Inspect the screenshots of multiple layouts (not just the target card) to confirm that no other assets suffer from text-wrapping, scaling, or spacing regressions.

## Variable Scoping Safety
- **Order of Variable Declarations**: Review all Python and JavaScript modifications to ensure all referenced variables (e.g. customized styling strings, layout dimensions, or local CSS overrides) are fully declared and bound under all conditional code paths before they are accessed, preventing `UnboundLocalError` or scoping ReferenceErrors.

## Playwright Execution Context Path
- **Dependency Folder Resolution**: Node resolves script dependencies relative to the script file's path rather than the execution Cwd. When running custom Playwright node scripts, do not execute them directly in transient scratch directories unless the package `playwright` is installed there. Always write or copy the script to the nearest project folder containing the local `node_modules` where playwright is installed, and run it in that directory's context.

## Operator Communication & Verification Rules
- **Understand & Verify First**: Never blindly output changes or make assertions without running physical validation first. Run actual verification scripts, inspect visual outputs (such as Playwright screens), and check for errors. Do not just state "I have checked something"—prove it.
- **Security, Bloat, & Duplication Analysis**: Before writing code, analyze: (1) Can this be done cleanly? (2) What are the potential security vulnerabilities? (3) Does this add unnecessary bloat or duplicate existing logic?
- **Brainstorming via /grill-me and /roast**: For any new design, feature, or business idea, prioritize running or recommending `/grill-me` (to align on details) and `/roast` (to pressure-test and stress-test the concept) before writing implementation code.
- **Bootup Skill Upgrades**: On starting a fresh session or chat, before executing any new feature instructions, check and upgrade custom skills (like `grill-me` or `roast`) to ensure they run with the latest improvements. Never follow user directions blindly if they conflict with safety, security, or design principles; stop and clarify first.

## Figma Compiler & SVG Geometry Safeguards
- **Figma Node Visibility Rule**: Always filter out `if not child.get("visible", True): continue` during symbol extraction and element compilation when parsing Figma API JSON nodes to prevent invisible background placeholders from rendering into production output.
- **Pre-Rotated SVG Geometry Rule**: Never apply CSS `transform: rotate(...)` to Figma-exported graphic SVG wrappers. Scope CSS rotation transforms strictly to HTML text nodes.
- **JSX SVG Style Object Rule**: Always convert inline SVG `style="..."` string attributes into camelCase JSX style objects (`style={{...}}`) during SVG-to-JSX conversion to prevent React runtime rendering errors.
- **Secrets Hygiene & Security Rule**: Never leave hardcoded API tokens, OAuth keys, or credentials in workspace scripts or committed files. Use environment variables or prompt inputs for secret management.

## Windows MCP Server Command Resolution Rules
- **Explicit Binary Path Rule**: When configuring CLI-based MCP servers on Windows in `mcp_config.json`, specify explicit `.cmd` or `.exe` binary paths (e.g. `C:\Users\HP\AppData\Local\codegraph\current\bin\codegraph.cmd`) to prevent child process resolution hangs and context deadline timeouts.
- **Pre-Caching & Validation Rule**: Verify npm package existence before adding `npx -y` commands to `mcp_config.json` to prevent HTTP 404 initialization aborts. Pre-install or cache CLI packages globally to eliminate cold-start network latency.
## Automatic Skills-Library Search & Repository Ingestion Rules
- **Automatic Skills-Library Search Rule**: The AI agent MUST automatically check and scan all reference manuals, specs, and guides stored under `brain-aios/wiki/research/skills-library/` whenever relevant to a user task or coding problem, without asking for explicit user prompt permission.
- **Repository Ingestion Scratch Isolation & Cleanup Rule**: When cloning external repositories during ingestion or skill adaptation, strictly isolate clones inside `scratch/ingest-[repo-name]/`. Force-delete the temporary scratch folder post-ingestion to prevent workspace pollution, git tracking bloat, and context token leaks.

## Environment, Media, & Browser Bridge Integration Rules
- **Env Variable Token Precedence Rule**: Never leave stale or invalid API tokens (e.g. `GITHUB_TOKEN`) in `.env` files or process environments when an authenticated CLI keyring (such as `gh` CLI) is available. Unset process environment overrides before running CLI health checks.
- **yt-dlp JS Runtime Rule**: Always ensure `C:\Users\HP\AppData\Roaming\yt-dlp\config` contains `--js-runtimes node` to guarantee YouTube video subtitle and metadata extraction stability.
- **Brave Browser Bridge Compatibility Rule**: When running browser-session bridge tools (`OpenCLI`, Playwright), recognize Brave as a Chromium-compatible browser utilizing `brave://extensions` for unpacked extension loading.

## GStack Virtual Engineering Team Dynamic Invocation Rules
- **Automatic GStack Executive Review**: Whenever creating a feature plan, refactoring code, or designing a frontend interface, the AI agent MUST dynamically apply Garry Tan's GStack review rules without requiring an explicit `/gstack` slash command:
  1. **CEO Lens (`/gstack ceo`)**: Verify user value, MVP scope discipline, and visual wow factor before writing code.
  2. **EM Lens (`/gstack eng`)**: Enforce surgical edits, zero speculative abstractions, and type safety during implementation.
  3. **Designer Lens (`/gstack design`)**: Enforce custom typography, dark mode palettes, micro-interactions, and 5-viewport responsiveness.
  4. **QA Lens (`/gstack qa`)**: Execute Playwright headless browser testing and console error checks before claiming completion.

## Hallmark Anti-AI-Slop Dynamic Invocation Rules
- **Automatic Hallmark Quality Gates & Variety Audit**: Whenever generating, refactoring, or reviewing web applications, landing pages, or HTML mockups, the AI agent MUST dynamically apply Together AI's Hallmark design rules without requiring an explicit `/hallmark` slash command:
  1. **Structural Variety (21 Macrostructures)**: Avoid defaulting to standard hero -> 3-column feature -> CTA templates. Select an appropriate macrostructure archetype for the brief.
  2. **OKLCH Color Math & Token Discipline**: Use locked design tokens from 20 catalog OKLCH themes or a custom OKLCH palette. Never improvise inline hex/rgb colors.
  3. **57 Anti-Slop Quality Gates**: Eliminate generic AI purple/blue gradients, invented fake metrics ("+47% conversion", "50,000+ teams"), un-tokenized font stacks, and missing semantic HTML5 elements.
  4. **Pre-Emit Self-Critique Header**: Score and stamp output on 6 axes (Philosophy, Hierarchy, Execution, Specificity, Restraint, Variety) via a CSS header (`/* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */`).
  5. **DNA Extraction (`hallmark study`)**: When given a design URL or screenshot reference, extract design DNA (macrostructure, type-pairing, color anchor) into `design.md`.

## Exhaustive Discovery & Non-Exhaustive Examples Rule
- **Examples Are Non-Exhaustive Samples**: Whenever the user or workspace instructions provide examples (e.g. "buttons, nav, hero, GSAP, WebGL, shaders"), treat them as illustrative samples, NEVER as artificial bounds or complete lists.
- **Unbounded Site & Asset Extraction**: Every website, repository, or project has its own unique tech stack, custom components, novel scripts, canvas shaders, SVG physics, or interaction models. The AI agent MUST proactively inspect, discover, extract, and document EVERY SINGLE novel element, component, script, animation, shader, and interaction present on the target — even if not explicitly named in an example list.
- **Dynamic Category Creation**: Never force-fit unique elements into rigid categories or omit them. If a target features a novel pattern (e.g., audio-reactive UI, 3D product customizer, fluid simulations, custom physics canvas), create a dedicated subfolder/section for it automatically.

## Hyper-Detailed Visual UI/UX Wireframe Rule
- **Visual Wireframe Mandate**: Never output basic placeholder shapes or basic Excalidraw JSON strings for wireframe requests. All reference ingestion wireframes MUST be hyper-detailed visual HTML pages (`wireframe.html`) and Playwright screenshots (`wireframe.png`) containing real site copy, real headlines, component spec tags (`COMPONENT: HEADER / NAV SYSTEM`), 3D stage boxes (`canvas#canvas`), 12-column grid overlays, and explicit technical annotations.








