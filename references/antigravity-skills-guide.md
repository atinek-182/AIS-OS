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

## 🎨 6. Front-End Design (`frontend-design`)
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


