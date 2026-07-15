# ZORIXEL AIOS Workspace Map & Directory Registry

This document serves as the centralized directory and file index for Atinek Maurya's AI Operating System (AIOS). It defines the layout, purpose, and logging boundaries of all workspace resources to prevent context fragmentation and directory rot.

---

## 1. Directory Structure Map

### Workspace Root Core Configs & Indexes
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [GEMINI.md](file:///d:/AI-OS/GEMINI.md) | File | Primary system prompt, voice instructions, and operator guidelines. | Operator / AIOS |
| [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) | File | This map. Centralized index of configurations, scripts, and logs. | AIOS (Immediate updates) |
| [connections.md](file:///d:/AI-OS/connections.md) | File | Registry of all active external system API integrations. | Operator / AIOS |
| [decisions/log.md](file:///d:/AI-OS/decisions/log.md) | File | Append-only log recording architectural modifications to the root workspace. | AIOS |
| [MEMORY.md](file:///d:/AI-OS/MEMORY.md) | File | Persistent memory documenting cross-session learnings and preferences. | AIOS (Auto-update) |
| [EXPANSIONS.md](file:///d:/AI-OS/EXPANSIONS.md) | File | AIOS expansion roadmap outlining future workflows and system targets. | AIOS |
| [aios-intake.md](file:///d:/AI-OS/aios-intake.md) | File | Setup Intake Form answers detailing the user's business objectives and stack. | Operator |
| [hot.md](file:///d:/AI-OS/hot.md) | File | High-priority current issues cache and automation candidates queue. | AIOS / Operator |
| [context/](file:///d:/AI-OS/context/) | Folder | Business context, guidelines, and onboarded preferences. | Operator / AIOS |
| [context/experiences/README.md](file:///d:/AI-OS/context/experiences/README.md) | File | Chronological index tracking personal experiences and lessons. | AIOS |
| [archives/](file:///d:/AI-OS/archives/) | Folder | Archive repository directory for storing outdated files. | Operator / AIOS |
| [brainstorms/](file:///d:/AI-OS/brainstorms/) | Folder | Spec and design documentation files for AIOS improvements. | AIOS |
| [projects/](file:///d:/AI-OS/projects/) | Junctions | Ignored folder containing junctions to external active project directories (Websites, Zorixel brand, For AIOS, My advisors, Products, Learning, Sandbox). | Operator / AIOS |

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
| [references/github-api.md](file:///d:/AI-OS/references/github-api.md) | File | GitHub repository and pull request MCP endpoints reference guide. | AIOS |
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
| [scripts/validate_workspace_map.py](file:///d:/AI-OS/scripts/validate_workspace_map.py) | File | Python validator script executed during git commits to verify map alignment. | AIOS |
| [scripts/hooks/pre-commit](file:///d:/AI-OS/scripts/hooks/pre-commit) | File | Tracked backup copy of the Git pre-commit hook script. | AIOS |
| `.git/hooks/pre-commit` | File | Local active Git pre-commit hook (runs workspace map validation). | AIOS |

### Workspace-Scoped Skills (`.agents/skills/`)
| Directory / File | Type | Purpose | Owner / Writer |
| :--- | :--- | :--- | :--- |
| [.agents/skills/](file:///d:/AI-OS/.agents/skills/) | Folder | Workspace-scoped custom slash commands. | AIOS |
| [.agents/skills/agent-adapt](file:///d:/AI-OS/.agents/skills/agent-adapt) | Folder | Skill guiding the LLM to safely adapt Claude Code tools to Antigravity. | AIOS |
| [.agents/skills/audit](file:///d:/AI-OS/.agents/skills/audit) | Folder | Four-Cs setup gaps check. | AIOS |
| [.agents/skills/draft-message](file:///d:/AI-OS/.agents/skills/draft-message) | Folder | ZORIXEL brand voice copy drafting. | AIOS |
| [.agents/skills/excalidraw-diagram](file:///d:/AI-OS/.agents/skills/excalidraw-diagram) | Folder | Visual workflow design drawing. | AIOS |
| [.agents/skills/file-search](file:///d:/AI-OS/.agents/skills/file-search) | Folder | Obsidian vault document retrieval. | AIOS |
| [.agents/skills/grill-me](file:///d:/AI-OS/.agents/skills/grill-me) | Folder | Interactive discovery sessions capture. | AIOS |
| [.agents/skills/improve-system](file:///d:/AI-OS/.agents/skills/improve-system) | Folder | Analyzing session transcript to improve skills, save experiences, and prune configs. | AIOS |
| [.agents/skills/level-up](file:///d:/AI-OS/.agents/skills/level-up) | Folder | Scoping automation features. | AIOS |
| [.agents/skills/notion-sync](file:///d:/AI-OS/.agents/skills/notion-sync) | Folder | Syncing database logs. | AIOS |
| [.agents/skills/onboard](file:///d:/AI-OS/.agents/skills/onboard) | Folder | Day-1 workspace wizard. | AIOS |
| [.agents/skills/plan-day](file:///d:/AI-OS/.agents/skills/plan-day) | Folder | Daily morning checklists scheduler. | AIOS |
| [.agents/skills/project-agent](file:///d:/AI-OS/.agents/skills/project-agent) | Folder | Scoped background developer agent runner. | AIOS |
| [.agents/skills/review-day](file:///d:/AI-OS/.agents/skills/review-day) | Folder | Daily evening reflections log script. | AIOS |
| [.agents/skills/scrape-competitor](file:///d:/AI-OS/.agents/skills/scrape-competitor) | Folder | Competitor Instagram posts scanner. | AIOS |
| [.agents/skills/skill-builder](file:///d:/AI-OS/.agents/skills/skill-builder) | Folder | Workspace custom skill optimization. | AIOS |
| [.agents/skills/using-superpowers](file:///d:/AI-OS/.agents/skills/using-superpowers) | Folder | Enforcing superpowers checkpoint gates. | AIOS |

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
| [second-brain-zorixel/](file:///d:/AI-OS/second-brain-zorixel/) | Junction | ZORIXEL brand-specific Obsidian vault (junction to local vault). | AIOS / Obsidian |

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
2. **Daily Wrap-up Verification:** During the `/review-day` evening routine, the agent must check the git status and directory additions to ensure any workspace layout alterations are reflected in this map.
