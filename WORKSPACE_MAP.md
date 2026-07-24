# ZORIXEL AIOS Workspace Map & Directory Registry

This document serves as the centralized directory and file index for Atinek Maurya's AI Operating System (AIOS). It defines the layout, purpose, and logging boundaries of all workspace resources to prevent context fragmentation and directory rot.

---

## 1. Directory Structure Map

### Workspace Root Core Configs & Indexes
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [GEMINI.md](file:///d:/AI-OS/GEMINI.md) | File | Primary system prompt, voice instructions, and operator guidelines. | Operator / AIOS |
| [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) | File | This map. Centralized index of configurations, scripts, and logs. | AIOS (Immediate updates) |
| [.vscode/settings.json](file:///d:/AI-OS/.vscode/settings.json) | File | VS Code workspace configuration, setting default Python interpreter to trials/.venv. | AIOS |
| [diagrams/](file:///d:/AI-OS/diagrams/) | Folder | Dedicated directory organizing all Excalidraw design and workflow diagrams. | AIOS |
| [diagrams/aios-workflow.excalidraw](file:///d:/AI-OS/diagrams/aios-workflow.excalidraw) | File | Excalidraw workflow diagram showing vaults, engines, processing and outputs. | AIOS |
| [diagrams/aios-skills-reference.excalidraw](file:///d:/AI-OS/diagrams/aios-skills-reference.excalidraw) | File | Detailed Excalidraw reference diagram mapping all 30 local & global skills. | AIOS |
| [diagrams/apps-security.excalidraw](file:///d:/AI-OS/diagrams/apps-security.excalidraw) | File | Excalidraw diagram showing application security zones, defense layers, and perimeters. | AIOS |
| [context/connections.md](file:///d:/AI-OS/context/connections.md) | File | Registry of all active external system API integrations. | Operator / AIOS |
| [decisions/log.md](file:///d:/AI-OS/decisions/log.md) | File | Append-only log recording architectural modifications to the root workspace. | AIOS |
| [MEMORY.md](file:///d:/AI-OS/MEMORY.md) | File | Persistent memory documenting cross-session learnings and preferences. | AIOS (Auto-update) |
| [EXPANSIONS.md](file:///d:/AI-OS/EXPANSIONS.md) | File | AIOS expansion roadmap outlining future workflows and system targets. | AIOS |
| [context/aios-intake.md](file:///d:/AI-OS/context/aios-intake.md) | File | Setup Intake Form answers detailing the user's business objectives and stack. | Operator |
| [hot.md](file:///d:/AI-OS/hot.md) | File | High-priority current issues cache and automation candidates queue. | AIOS / Operator |
| [context/](file:///d:/AI-OS/context/) | Folder | Business context, guidelines, and onboarded preferences. | Operator / AIOS |
| [context/experiences/README.md](file:///d:/AI-OS/context/experiences/README.md) | File | Chronological index tracking personal experiences and lessons. | AIOS |
| [archives/](file:///d:/AI-OS/archives/) | Folder | Archive repository directory for storing outdated files. | Operator / AIOS |
| [Finding Fonts/](file:///d:/AI-OS/Finding%20Fonts/) | Folder | Zip files of font candidates downloaded from Fontex. | Operator |
| [brainstorms/](file:///d:/AI-OS/brainstorms/) | Folder | Spec and design documentation files for AIOS improvements. | AIOS |
| [brainstorms/2026-07-23-site-reference-ingestion-queue.md](file:///d:/AI-OS/brainstorms/2026-07-23-site-reference-ingestion-queue.md) | File | Brainstorm & discovery notes for 18-site reference ingestion queue. | AIOS |
| [config/](file:///d:/AI-OS/config/) | Folder | Local tool configuration directory (mcporter MCP endpoints config). | AIOS |
| [.playwright-mcp/](file:///d:/AI-OS/.playwright-mcp/) | Folder | Temporary cache folder for Playwright MCP server screenshots and logs. | Playwright / AIOS |
| [projects/](file:///d:/AI-OS/projects/) | Junctions | Ignored folder containing junctions to external active project directories (Websites, Zorixel brand, For AIOS, My advisors, Products, Learning, Sandbox). | Operator / AIOS |
| [projects/font-showcase/](file:///d:/AI-OS/projects/font-showcase/) | Folder | Typographic brand exploration slides showcase project. | AIOS |
| [projects/font-showcase/colors_presentation.html](file:///d:/AI-OS/projects/font-showcase/colors_presentation.html) | File | Interactive color exploration slides showcase page. | AIOS |
| [projects/font-showcase/generate_nuqun_logo.js](file:///d:/AI-OS/projects/font-showcase/generate_nuqun_logo.js) | File | Local Playwright script generating high-resolution brand logos in Nuqun. | AIOS |
| [projects/font-showcase/qa/verify_colors.js](file:///d:/AI-OS/projects/font-showcase/qa/verify_colors.js) | File | Automated Playwright script verifying color presentation stability. | AIOS |
| [projects/For AIOS/Micrographics/](file:///d:/AI-OS/projects/For%20AIOS/Micrographics/) | Folder | Compiled micrographics library with SVG, HTML, and React components. | AIOS |
| [projects/For AIOS/Micrographics/compile_micrographics.py](file:///d:/AI-OS/projects/For%20AIOS/Micrographics/compile_micrographics.py) | File | Automation build script parsing Figma JSON nodes and generating assets. | AIOS |
| [projects/For AIOS/Micrographics/compare_screenshots.py](file:///d:/AI-OS/projects/For%20AIOS/Micrographics/compare_screenshots.py) | File | Pixel-by-pixel automated visual difference reporter for HTML vs Figma SVG. | AIOS |
| [projects/font-showcase/capture_all_frames.js](file:///d:/AI-OS/projects/font-showcase/capture_all_frames.js) | File | Playwright CLI capture script rendering raw SVGs and HTMLs for QA audit. | AIOS |
| [premium-frontend-experience-system/](file:///d:/AI-OS/premium-frontend-experience-system/) | Junction | Premium frontend experience design system vault mapped from external documents. | Operator / AIOS |
| [premium-frontend-experience-system/reference-inputs/INGESTION_QUEUE.md](file:///d:/AI-OS/premium-frontend-experience-system/reference-inputs/INGESTION_QUEUE.md) | File | Centralized tracking queue for the 18 reference websites ingestion pipeline. | AIOS |
| [premium-frontend-experience-system/vault-references/](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/) | Folder | New dedicated master reference vault containing ultra-granular design, UX, and code manuals. | AIOS |
| [premium-frontend-experience-system/vault-references/INDEX.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/INDEX.md) | File | Centralized index of all master vault reference manuals. | AIOS |
| [premium-frontend-experience-system/vault-references/sondaven-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/sondaven-granularity-master.md) | File | Dot-to-dot ultra-granular design, UX, motion physics, and source-code reference for Sondaven. | AIOS |
| [premium-frontend-experience-system/vault-references/oryzo-ai-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/oryzo-ai-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, 3D assets, and source code for Oryzo AI. | AIOS |
| [premium-frontend-experience-system/vault-references/the-line-studio-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/the-line-studio-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, card page transitions, and source code for The Line Studio. | AIOS |
| [premium-frontend-experience-system/vault-references/gehry-getty-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/gehry-getty-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, 3D GLB models, and audio stream for Gehry Getty. | AIOS |
| [premium-frontend-experience-system/vault-references/grids-obys-agency-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/grids-obys-agency-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, interactive grid visualizer, and runnable code for Grids by Obys Agency. | AIOS |
| [premium-frontend-experience-system/vault-references/grids-obys-agency-deep-research.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/grids-obys-agency-deep-research.md) | File | Comprehensive deep research document, word-for-word text corpus analysis, and Obys Grid System rules. | AIOS |
| [brain-aios/wiki/sops/grid-systems-sop.md](file:///d:/AI-OS/brain-aios/wiki/sops/grid-systems-sop.md) | File | Standard operating procedure codifying Obys 4 Grid Canons and Vertical Rhythm math. | AIOS |
| [premium-frontend-experience-system/vault-references/the-shift-tokyo-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/the-shift-tokyo-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, Tokyo live clock widget, and runnable code for The Shift Tokyo. | AIOS |
| [premium-frontend-experience-system/vault-references/good-fella-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/good-fella-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, Annnimate components, and Next.js Turbopack code for Good Fella. | AIOS |
| [premium-frontend-experience-system/vault-references/follow-art-granularity-master.md](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/follow-art-granularity-master.md) | File | Dot-to-dot ultra-granular 15-category reference manual, Vide Infra 3D WebGL engine, and Vite React code for Follow Art. | AIOS |
| [brain-aios/wiki/experiences/2026-07-24-exhaustive-10-pillar-reference-ingestion.md](file:///d:/AI-OS/brain-aios/wiki/experiences/2026-07-24-exhaustive-10-pillar-reference-ingestion.md) | File | Experience log codifying the 10-pillar ultra-exhaustive deep research ingestion pipeline and Obys grid engine. | AIOS |

| [templates/](file:///d:/AI-OS/templates/) | Folder | Unified templates folder containing junctions to Obsidian template directories. | AIOS |
| [templates/aios](file:///d:/AI-OS/templates/aios) | Junction | Directory junction pointing to the AIOS wiki templates (`brain-aios/wiki/templates`). | AIOS |
| [templates/zorixel](file:///d:/AI-OS/templates/zorixel) | Junction | Directory junction pointing to the Zorixel wiki templates (`second-brain-zorixel/wiki/templates`). | AIOS |
| [trials/](file:///d:/AI-OS/trials/) | Folder | Sandbox trial folders for prompt tuning, vision-in-the-loop design, and web speed loops. | AIOS / Operator |
| [trials/runner.py](file:///d:/AI-OS/trials/runner.py) | File | Host-side runner script orchestrating sandboxed mutation runs and Git controls. | AIOS |
| [audits/](file:///d:/AI-OS/audits/) | Folder | AIOS scorecard and Four Cs audit reports. | AIOS |
| [tests/](file:///d:/AI-OS/tests/) | Folder | System verification and demo test suites. | AIOS |
| [scratch/](file:///d:/AI-OS/scratch/) | Folder | Temporary scratch folder for repository ingestion clones and sandboxed experimentation. | AIOS |



### Reference Manuals (`references/`)
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [references/](file:///d:/AI-OS/references/) | Folder | Reference guides, API manuals, and framework docs. | AIOS |
| [references/3ms-framework.md](file:///d:/AI-OS/references/3ms-framework.md) | File | Framework documentation for Mindset, Method, and Machine models. | Operator |
| [references/aios-user-manual.md](file:///d:/AI-OS/references/aios-user-manual.md) | File | Centralized handbook containing commands and execution guides for all skills. | AIOS |
| [references/antigravity-skills-guide.md](file:///d:/AI-OS/references/antigravity-skills-guide.md) | File | Guide explaining custom skills structure, marketplace hooks, and plugin APIs. | AIOS |
| [references/chrome-devtools-api.md](file:///d:/AI-OS/references/chrome-devtools-api.md) | File | Playwright and Chrome DevTools MCP servers reference manual. | AIOS |
| [references/codegraph-api.md](file:///d:/AI-OS/references/codegraph-api.md) | File | Codegraph exploration tool manual. | AIOS |
| [references/context7-api.md](file:///d:/AI-OS/references/context7-api.md) | File | Context7 Upstash endpoint retrieval documentation. | AIOS |
| [references/figma-api.md](file:///d:/AI-OS/references/figma-api.md) | File | Figma remote MCP server tools and OAuth setup. | AIOS |
| [references/github-api.md](file:///d:/AI-OS/references/github-api.md) | File | GitHub repository and pull request MCP endpoints reference guide. | AIOS |
| [references/global-rules-conflict-resolution.md](file:///d:/AI-OS/references/global-rules-conflict-resolution.md) | File | Conflict resolution guide for global design rules (impeccable vs. ui-ux-pro-max). | AIOS |
| [references/gws-api.md](file:///d:/AI-OS/references/gws-api.md) | File | Google Workspace CLI account switching and credential profile configuration. | AIOS |
| [references/magic-api.md](file:///d:/AI-OS/references/magic-api.md) | File | Magic MCPS Component builder and design inspiration API guide. | AIOS |
| [references/notion-api.md](file:///d:/AI-OS/references/notion-api.md) | File | Notion MCP database and pages sync reference. | AIOS |
| [references/playwright-api.md](file:///d:/AI-OS/references/playwright-api.md) | File | Playwright headless browser automation actions manual. | AIOS |
| [references/utility-scripts.md](file:///d:/AI-OS/references/utility-scripts.md) | File | Manual documenting maintenance scripts (verifiers, copiers, adaptors). | AIOS |
| [references/voice.md](file:///d:/AI-OS/references/voice.md) | File | Brand voice tone guide and messaging guidelines. | Operator |

### Maintenance Scripts (`scripts/`)
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [scripts/](file:///d:/AI-OS/scripts/) | Folder | Centralized workspace maintenance and verification scripts. | AIOS |
| [scripts/compile_carousel.py](file:///d:/AI-OS/scripts/compile_carousel.py) | File | Python compiler script that generates slide HTML elements from copy drafts. | AIOS |
| [scripts/generate_security_diagram.py](file:///d:/AI-OS/scripts/generate_security_diagram.py) | File | Python generator script that programmatically compiles the app security Excalidraw diagram. | AIOS |
| [scripts/mirror-jordan-watkins.js](file:///d:/AI-OS/scripts/mirror-jordan-watkins.js) | File | Node script that mirrors HTML, CSS, JS, fonts, and images from jordanwatkins.xyz. | AIOS |
| [scripts/serve.js](file:///d:/AI-OS/scripts/serve.js) | File | Local static server to host mirrored reference assets for Playwright. | AIOS |
| [scripts/generate-brand-candidates.js](file:///d:/AI-OS/scripts/generate-brand-candidates.js) | File | Playwright script to query local tools for brand color and font ideas. | AIOS |
| [scripts/scrapling_runner.py](file:///d:/AI-OS/scripts/scrapling_runner.py) | File | Python CLI and module wrapper engine for Scrapling adaptive and stealthy web scraping. | AIOS |
| [scripts/agent_reach_runner.py](file:///d:/AI-OS/scripts/agent_reach_runner.py) | File | Python runner and diagnostic helper for Agent Reach multi-platform internet capability engine. | AIOS |
| [scripts/hallmark_runner.py](file:///d:/AI-OS/scripts/hallmark_runner.py) | File | Python audit & verification engine for Hallmark anti-AI-slop design skill. | AIOS |
| [scripts/validate_workspace_map.py](file:///d:/AI-OS/scripts/validate_workspace_map.py) | File | Python validator script executed during git commits to verify map alignment. | AIOS |
| [scripts/generate_visual_wireframes.py](file:///d:/AI-OS/scripts/generate_visual_wireframes.py) | File | Python engine creating hyper-detailed multi-section visual wireframe HTML pages and Playwright screenshots. | AIOS |

| [scripts/validate_links.py](file:///d:/AI-OS/scripts/validate_links.py) | File | Python link validator script checking for relative/Obsidian link rot. | AIOS |
| [scripts/verify_design_milestone.py](file:///d:/AI-OS/scripts/verify_design_milestone.py) | File | Python script to automate milestone visual verification and console checks. | AIOS |
| [scripts/hooks/pre-commit](file:///d:/AI-OS/scripts/hooks/pre-commit) | File | Tracked backup copy of the Git pre-commit hook script. | AIOS |
| `.git/hooks/pre-commit` | File | Local active Git pre-commit hook (runs workspace map validation). | AIOS |


### Workspace-Scoped Skills (`.agents/skills/`)
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [.agents/skills/](file:///d:/AI-OS/.agents/skills/) | Folder | Workspace-scoped custom slash commands. | AIOS |
| [.agents/skills/agent-adapt](file:///d:/AI-OS/.agents/skills/agent-adapt) | Folder | Skill guiding the LLM to safely adapt Claude Code tools to Antigravity. | AIOS |
| [.agents/skills/agent-reach](file:///d:/AI-OS/.agents/skills/agent-reach) | Folder | Skill for multi-platform internet searching and content reading across 10+ social/web platforms. | AIOS |
| [.agents/skills/canvas-design](file:///d:/AI-OS/.agents/skills/canvas-design) | Folder | Programmatic visual assets and canvas generator dynamic router. | AIOS |
| [.agents/skills/brand-colors](file:///d:/AI-OS/.agents/skills/brand-colors) | Folder | Custom skill to automate brand color palette selection, interactive swatch creation, and WCAG contrast audits. | AIOS |
| [.agents/skills/design-direction](file:///d:/AI-OS/.agents/skills/design-direction) | Folder | Visual design direction and roast council generator. | AIOS |
| [.agents/skills/carousel-copy](file:///d:/AI-OS/.agents/skills/carousel-copy) | Folder | Skill for planning viral slide copy outlines and visual structures. | AIOS |
| [.agents/skills/carousel-render](file:///d:/AI-OS/.agents/skills/carousel-render) | Folder | Rendering engine that builds HTML slide files and captures screenshots. | AIOS |
| [.agents/skills/audit](file:///d:/AI-OS/.agents/skills/audit) | Folder | Four-Cs setup gaps check. | AIOS |
| [.agents/skills/draft-message](file:///d:/AI-OS/.agents/skills/draft-message) | Folder | ZORIXEL brand voice copy drafting. | AIOS |
| [.agents/skills/excalidraw-diagram](file:///d:/AI-OS/.agents/skills/excalidraw-diagram) | Folder | Visual workflow design drawing. | AIOS |
| [.agents/skills/file-search](file:///d:/AI-OS/.agents/skills/file-search) | Folder | Obsidian vault document retrieval. | AIOS |
| [.agents/skills/grill-me](file:///d:/AI-OS/.agents/skills/grill-me) | Folder | Interactive discovery sessions capture. | AIOS |
| [.agents/skills/hallmark](file:///d:/AI-OS/.agents/skills/hallmark) | Folder | Together AI anti-AI-slop design engine skill. | AIOS |
| [.agents/skills/improve-system](file:///d:/AI-OS/.agents/skills/improve-system) | Folder | Analyzing session transcript to improve skills, save experiences, and prune configs. | AIOS |

| [.agents/skills/ingest-repo](file:///d:/AI-OS/.agents/skills/ingest-repo) | Folder | Autonomous 8-phase repository ingestion, security audit, roast council, and skill adaptation engine. | AIOS |
| [.agents/skills/ingest-skills](file:///d:/AI-OS/.agents/skills/ingest-skills) | Folder | Upgraded alias skill routing directly to /ingest-repo engine. | AIOS |
| [.agents/skills/level-up](file:///d:/AI-OS/.agents/skills/level-up) | Folder | Scoping automation features. | AIOS |
| [.agents/skills/marketing](file:///d:/AI-OS/.agents/skills/marketing) | Folder | Copywriting and marketing copy dynamic router. | AIOS |
| [.agents/skills/new-project](file:///d:/AI-OS/.agents/skills/new-project) | Folder | Initializes project directory, briefs, templates, and launches discovery Q&A. | AIOS |
| [.agents/skills/notion-sync](file:///d:/AI-OS/.agents/skills/notion-sync) | Folder | Syncing database logs. | AIOS |
| [.agents/skills/onboard](file:///d:/AI-OS/.agents/skills/onboard) | Folder | Day-1 workspace wizard. | AIOS |
| [.agents/skills/daily-plan-day](file:///d:/AI-OS/.agents/skills/daily-plan-day) | Folder | Daily morning checklists scheduler. | AIOS |
| [.agents/skills/project-agent](file:///d:/AI-OS/.agents/skills/project-agent) | Folder | Scoped background developer agent runner. | AIOS |
| [.agents/skills/daily-review-day](file:///d:/AI-OS/.agents/skills/daily-review-day) | Folder | Daily evening reflections log script. | AIOS |
| [.agents/skills/scrape-competitor](file:///d:/AI-OS/.agents/skills/scrape-competitor) | Folder | Competitor Instagram posts scanner. | AIOS |
| [.agents/skills/scrape-carousel](file:///d:/AI-OS/.agents/skills/scrape-carousel) | Folder | Scrapes competitor reels/posts and takes screenshots of carousel slides. | AIOS |
| [.agents/skills/scrape-component](file:///d:/AI-OS/.agents/skills/scrape-component) | Folder | Extracts a specific UI component, animation, or style from a website URL. | AIOS |
| [.agents/skills/scrape-reference](file:///d:/AI-OS/.agents/skills/scrape-reference) | Folder | Site DNA reference ingestion pipeline (Scrapling stealth fetch, Playwright multi-viewport visual & animation audit, 5-layer DNA extraction, user approval checklist, cross-vault sync & React component builder). | AIOS |
| [.agents/skills/scrape-web](file:///d:/AI-OS/.agents/skills/scrape-web) | Folder | Scraping, dynamic HTML parsing, anti-bot bypass, and adaptive element extraction via Scrapling engine. | AIOS |
| [.agents/skills/seo-audit](file:///d:/AI-OS/.agents/skills/seo-audit) | Folder | Technical SEO and GEO analysis dynamic router. | AIOS |
| [.agents/skills/skill-builder](file:///d:/AI-OS/.agents/skills/skill-builder) | Folder | Workspace custom skill optimization. | AIOS |
| [.agents/skills/vibesec](file:///d:/AI-OS/.agents/skills/vibesec) | Folder | Security scanning and audit rules tweaked for Antigravity. | AIOS |
| [.agents/skills/gstack](file:///d:/AI-OS/.agents/skills/gstack) | Folder | Garry Tan's virtual engineering team workflow (CEO strategy, EM architecture, UI/UX design, browser QA, release audit). | AIOS |
| [.agents/skills/using-superpowers](file:///d:/AI-OS/.agents/skills/using-superpowers) | Folder | Enforcing superpowers checkpoint gates. | AIOS |
| [.agents/skills/verify-design](file:///d:/AI-OS/.agents/skills/verify-design) | Folder | Visual and console audits of front-end milestones. | AIOS |
| [.agents/skills/autoresearch-manage](file:///d:/AI-OS/.agents/skills/autoresearch-manage) | Folder | Manage Autoresearch loop target directories and registries. | AIOS |
| [.agents/skills/frontend-slides](file:///d:/AI-OS/.agents/skills/frontend-slides) | Folder | Programs 16:9 responsive HTML presentation deck layouts. | AIOS |
| [.agents/skills/slide-component](file:///d:/AI-OS/.agents/skills/slide-component) | Folder | Injects custom components and animations into slide layouts. | AIOS |

### Workspace-Scoped Agents (`.agents/agents/`)
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [.agents/agents/](file:///d:/AI-OS/.agents/agents/) | Folder | Workspace-scoped custom background subagent configurations. | AIOS |
| [.agents/agents/developer.md](file:///d:/AI-OS/.agents/agents/developer.md) | File | Scoped background developer agent configuration defining lead developer behaviors. | AIOS |

### Global Systems & Vaults (External/Local)
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| `C:\Users\HP\.gemini\config\skills\` | Folder | Global slash command skills available across all workspace projects. | AIOS |
| `C:\Users\HP\.gemini\config\skills\karpathy-guidelines\` | Folder | Global skill enforcing Karpathy-inspired coding behavioral guidelines. | AIOS |
| `C:\Users\HP\.gemini\config\AGENTS.md` | File | Global rules pre-hook executed before tool calls. | Operator / AIOS |
| [brain-aios/](file:///d:/AI-OS/brain-aios/) | Junction | General AIOS Obsidian vault hub (junction to local vault). | AIOS / Obsidian |
| [brain-aios/wiki/experiences/](file:///d:/AI-OS/brain-aios/wiki/experiences/) | Folder | Personal lessons, stories, and insights captured in Obsidian. | AIOS |
| [brain-aios/wiki/research/skills-library/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/) | Folder | Static reference library of marketing and SEO skills. | AIOS |
| [brain-aios/wiki/research/skills-library/gstack/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/gstack/) | Folder | Static reference library for Garry Tan's gstack AI engineering team guide. | AIOS |
| [brain-aios/wiki/research/skills-library/canvas-design/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/canvas-design/) | Folder | Static reference library for Canvas Design styles and templates. | AIOS |
| [brain-aios/wiki/research/skills-library/threejs-skills/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/threejs-skills/) | Folder | Static reference library for Three.js, shaders, and R3F. | AIOS |
| [brain-aios/wiki/research/skills-library/gsap-skills/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/gsap-skills/) | Folder | Static reference library for GSAP, ScrollTrigger, and timelines. | AIOS |
| [brain-aios/wiki/research/skills-library/seo-audit-reference/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/seo-audit-reference/) | Folder | Static reference library containing SEO audit guidelines and validation scripts. | AIOS |
| [second-brain-zorixel/](file:///d:/AI-OS/second-brain-zorixel/) | Junction | ZORIXEL brand-specific Obsidian vault (junction to local vault). | AIOS / Obsidian |
| [second-brain-zorixel/wiki/research/jordan-watkins-reference/](file:///d:/AI-OS/second-brain-zorixel/wiki/research/jordan-watkins-reference/) | Folder | Mirrored assets, design scripts, and visual analysis of jordanwatkins.xyz. | AIOS |

---

## 2. Read/Write Policy & Log Alignment Table

To keep vaults isolated and logging consistent, any modifications made within the workspace directories must follow this strict log alignment schedule:

| Target Directory | Index File to Update | Log File to Append | Logging Protocol |
| :--- | :--- | :--- | :--- |
| **Workspace Root** (`d:/AI-OS/` scripts/references/configs) | N/A | [decisions/log.md](file:///d:/AI-OS/decisions/log.md) | Append decisions under the format `## YYYY-MM-DD — Short title`. |
| **Brain for AIOS** (`brain-aios/` checklists/wiki/SOPs) | [brain-aios/wiki/index.md](file:///d:/AI-OS/brain-aios/wiki/index.md) | [brain-aios/wiki/log.md](file:///d:/AI-OS/brain-aios/wiki/log.md) | Log details of vault content changes and index new markdown files. |
| **Second Brain** (`second-brain-zorixel/` strategy/briefs) | [second-brain-zorixel/wiki/index.md](file:///d:/AI-OS/second-brain-zorixel/wiki/index.md) | [second-brain-zorixel/wiki/log.md](file:///d:/AI-OS/second-brain-zorixel/wiki/log.md) | Log brand strategy/brief updates and index content files. |
| **Custom Skills** (`.agents/skills/` or global config) | [GEMINI.md](file:///d:/AI-OS/GEMINI.md) | [decisions/log.md](file:///d:/AI-OS/decisions/log.md) | Register new slash commands under the "Your skills" section of GEMINI.md. |

---

## 3. Maintenance and Drift Prevention

1. **Immediate Updates:** Whenever a new folder, junction, or config file (like adding an MCP server, API guide, or custom script) is created, the agent **MUST** immediately update this map to register the path.
2. **Daily Wrap-up Verification:** During the `/daily-review-day` evening routine, the agent must check the git status and directory additions to ensure any workspace layout alterations are reflected in this map.
