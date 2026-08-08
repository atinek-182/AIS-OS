# Antigravity Skills & Plugins Guide

This reference guide summarizes the core skills and plugins referenced in Nate Herk's AIOS guides, mapped to their GitHub repositories, documentation, and installation instructions for the **Antigravity** platform.

---

## 🚀 1. Superpowers (`superpowers`)
*   **Purpose:** Forces a structured development workflow: planning first, creating isolated test environments, writing tests before coding, and running two-stage reviews (specification compliance and code quality).
*   **Antigravity Native Port:** [roundpilot/superpowers-antigravity](https://github.com/roundpilot/superpowers-antigravity)
*   **Installation Command:**
  ```bash
  antigravity plugin install superpowers@roundpilot/superpowers-antigravity
  ```

---

## 🛠️ 2. Skill Creator (`skill-creator`)
*   **Purpose:** Automatically generates, tests, and refines reusable skills (`SKILL.md` configurations with YAML frontmatter) from plain-English prompts or SOPs, avoiding formatting errors.
*   **Antigravity Native Ports:** 
    - [rahultalwar/AntigravitySkillCreator](https://github.com/rahultalwar/AntigravitySkillCreator)
    - [mohan25manu/antigravity-skill-creator](https://github.com/mohan25manu/antigravity-skill-creator)
*   **Installation Command:** (Utilizes the native `/agents/skills/skill-builder` local skill or custom templates)

---

## 🧠 3. Antigravity Memory (`antigravity-mem`)
*   **Purpose:** Persists long-term vault memory across coding sessions. Automatically indexes session decisions, edits, and milestones into a local SQLite database using vector search, injecting relevant context on startup to avoid the "startup tax" of re-explaining the workspace.
*   **Antigravity Native Ports:**
    - [aroldos91/antigravity-mem](https://github.com/aroldos91/antigravity-mem)
    - [keyut-shah/gemini-mem](https://github.com/keyut-shah/gemini-mem)
*   **Installation Command:** (Typically loaded as an MCP server linked to a local SQLite instance)

---

## 📦 4. Context Mode (`context-mode`)
*   **Purpose:** Restores session snapshot databases and routes external tool output (like long logs or Playwright HTML outputs) through a sandbox that compresses them, preventing context bloat and token exhaust.
*   **Repository:** [mksglu/context-mode](https://github.com/mksglu/context-mode)
*   **Installation Command:** Add the repository as an MCP server configuration in `.agents/settings.json`.

---

## ⚙️ 5. Get Shit Done (`get-shit-done-cc` / GSD)
*   **Purpose:** Orchestrates clean, isolated sub-agents to carry out sub-tasks under strict verification guidelines (checks for scope reduction and security threats).
*   **Repository:** [nateherk/get-shit-done-cc](https://github.com/nateherk/get-shit-done-cc)
*   **Installation Command:**
  ```bash
  npx get-shit-done-cc --antigravity --global
  ```

---

## 👁️ 6. Agent Reach (`agent-reach`)
*   **Purpose:** Multi-backend router & diagnostic engine giving AI Agents single-command internet search, reading, and content extraction across 10+ social & web platforms (YouTube, Bilibili, V2EX, GitHub, Reddit, RSS, Twitter/X, Exa AI Search).
*   **Repository:** [Panniantong/agent-reach](https://github.com/Panniantong/agent-reach)
*   **Active Local Skill:** `.agents/skills/agent-reach/SKILL.md` (`/agent-reach`)
*   **Runner Script:** `scripts/agent_reach_runner.py`

---

## 🕸️ 7. Graphify Knowledge Graph Engine (`graphify`)
* **Purpose**: Maps codebases, docs, PDFs, images, and videos into deterministic, zero-LLM tree-sitter AST knowledge graphs. Replaces brute-force file grepping with `graphify query`, `graphify explain`, and `graphify path`.
* **Repository**: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
* **Active Local Skill**: `.agents/skills/graphify/SKILL.md` (`/graphify`)
* **Runner Script**: `scripts/graphify_runner.py` (Managing 4 workspace hubs: `root`, `brain`, `zorixel`, `frontend`)

---

## 🎨 8. Front-End Design (`frontend-design`)
*   **Purpose:** Injects styling guidelines and assets so that generated user interfaces use premium visual rules (harmonious HSL colors, outfit typography, hover transitions) instead of default layouts.
*   **Installation Command:** Utilizes local design SOP instructions or Antigravity Design native configurations.

---

## 📚 7. Context7 (`context7`)
*   **Purpose:** Fetches up-to-date, version-specific documentation and code examples directly from source to eliminate hallucinations.
*   **Repository:** [upstash/context7](https://github.com/upstash/context7)
*   **Installation Command:** Registers the remote MCP server URL `https://mcp.context7.com/mcp` globally in `mcp_config.json` and installs the global skill `context7`.

---

## 📊 8. Codegraph (`codegraph`)
*   **Purpose:** Indexes codebase structure and exposes AST relations to the agent.
*   **Installation Command:** Registers the `codegraph` command globally in `mcp_config.json`.

---

## 🌐 9. Playwright (`playwright`)
*   **Purpose:** Exposes headless browser driving and visual screenshot capability for audits.
*   **Installation Command:** Registers `@playwright/mcp` server globally in `mcp_config.json`.

---

## 🐙 10. GitHub (`github`)
*   **Purpose:** Exposes repo, issue, and pull request management natively.
*   **Installation Command:** Registers `@modelcontextprotocol/server-github` globally in `mcp_config.json`.

---

## 🪄 11. Magic (`magic`)
*   **Purpose:** Sourcing Tailwind components, templates, and brand logos.
*   **Installation Command:** Registers `@21st-dev/magic` globally in `mcp_config.json`.

---

## 🛠️ 12. Chrome DevTools (`chrome-devtools-mcp`)
*   **Purpose:** Exposes viewport audits, console logs, and performance metrics.
*   **Installation Command:** Registers `chrome-devtools-mcp` globally in `mcp_config.json`.

---

## 📒 13. Notion (`notion-mcp-server`)
*   **Purpose:** Access and modify remote database boards, checklists, and logs.
*   **Installation Command:** Registers `@notionhq/notion-mcp-server` globally in `mcp_config.json`.

---

## 🏛️ 14. GStack Virtual Engineering Team (`gstack`)
*   **Purpose:** Organizes the agent into an executive engineering team (CEO strategy, EM architecture, UI/UX design, browser QA, release audit) to evaluate features, code changes, and UI layouts before shipping.
*   **Repository:** [garrytan/gstack](https://github.com/garrytan/gstack)
*   **Active Local Skill:** `.agents/skills/gstack/SKILL.md` (`/gstack`)
*   **Reference Manual:** `brain-aios/wiki/research/skills-library/gstack/README.md`
*   **Dynamic Triggering:** Automatically triggers during planning, code reviews, design audits, or visual QA without needing to type `/gstack` explicitly.

---

## 🎨 15. Hallmark Anti-AI-Slop Engine (`hallmark`)
*   **Purpose:** Enforces macrostructure variety (21 layout archetypes), theme palettes (20 OKLCH themes + custom engine), and 57 anti-slop quality gates across build, audit, redesign, and study verbs.
*   **Repository:** [nutlope/hallmark](https://github.com/nutlope/hallmark)
*   **Active Local Skill:** `.agents/skills/hallmark/SKILL.md` (`/hallmark`)
*   **Runner Script:** `scripts/hallmark_runner.py`
*   **Reference Manual:** `brain-aios/wiki/research/skills-library/hallmark/README.md`
*   **Dynamic Triggering:** Automatically triggers when designing frontend UIs, performing design audits, or extracting design DNA from URLs or screenshots.
---

## 🔍 16. OS Audit (`os-audit`)
*   **Purpose:** Conducts a read-only audit of operating context drift, freshness, routing integrity, index truth, bloat, hygiene, and context placement across the AIOS workspace.
*   **Active Local Skill:** `.agents/skills/os-audit/SKILL.md` (`/os-audit`)
*   **Reference Manual:** `brain-aios/wiki/research/skills-library/os-audit/SKILL.md`
*   **Dynamic Triggering:** Automatically triggers when verifying context freshness, auditing project structure, checking stale indexes, or organizing project files.

---

## 💻 17. JS Mastery Skills (`jsmastery-skills`)
*   **Purpose:** Fullstack JavaScript & Next.js development skills covering architecture, scoping, testing, code audits, and documentation.
*   **Repository:** [jsmastery-pro/skills](https://github.com/jsmastery-pro/skills)
*   **Active Local Skills:**
    - `.agents/skills/jsmastery-architect/SKILL.md` (`/jsmastery-architect`)
    - `.agents/skills/jsmastery-audit/SKILL.md` (`/jsmastery-audit`)
    - `.agents/skills/jsmastery-scope/SKILL.md` (`/jsmastery-scope`)
*   **Reference Vault Archival:** `brain-aios/wiki/research/skills-library/jsmastery-skills/`
*   **Dynamic Triggering:** Automatically triggers when designing Next.js App Router features, building fullstack JS apps, scoping milestones, or running code audits.

---

## ⚡ 18. Matt Pocock Engineering Skills (`mattpocock-skills`)
*   **Purpose:** High-rigor engineering discipline, TypeScript domain modeling, multi-session wayfinding, spec-to-tickets deconstruction, and Socratic teaching.
*   **Repository:** [mattpocock/skills](https://github.com/mattpocock/skills)
*   **Active Local Skills:**
    - `.agents/skills/mattpocock-domain-modeling/SKILL.md` (`/mattpocock-domain-modeling`)
    - `.agents/skills/mattpocock-wayfinder/SKILL.md` (`/mattpocock-wayfinder`)
    - `.agents/skills/mattpocock-to-spec/SKILL.md` (`/mattpocock-to-spec`)
    - `.agents/skills/mattpocock-to-tickets/SKILL.md` (`/mattpocock-to-tickets`)
    - `.agents/skills/mattpocock-teach/SKILL.md` (`/mattpocock-teach`)
    - `.agents/skills/mattpocock-setup-ts-deep-modules/SKILL.md` (`/mattpocock-setup-ts-deep-modules`)
*   **Reference Vault Archival:** `brain-aios/wiki/research/skills-library/mattpocock-skills/`
*   **Dynamic Triggering:** Automatically triggers when modeling TS types, managing multi-session epics, compiling specs, decomposing tickets, or explaining complex engineering concepts.

---

## 🛡️ 19. Resemble AI Detect (`resemble-detect`)
*   **Purpose:** Enterprise deepfake detection, audio source tracing (ElevenLabs vs Resemble vs human), and media safety across audio, video, and images via direct Resemble AI REST API v2 calls.
*   **Repository:** [resemble-ai/detect-skill](https://github.com/resemble-ai/detect-skill)
*   **Active Local Skill:** `.agents/skills/resemble-detect/SKILL.md` (`/resemble-detect`)
*   **Runner Script:** `scripts/resemble_detect_runner.py`
*   **Dynamic Triggering:** Automatically triggers when checking media authenticity, verifying audio/video deepfakes, tracing synthetic voice platforms, or performing media safety audits.



