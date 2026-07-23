---
name: agent-reach
description: "Give your AI Agent eyes to see the entire internet. Search + read 10+ social & web platforms (YouTube, Bilibili, V2EX, GitHub, Twitter, Reddit, RSS, Xueqiu)."
argument-hint: "[command|doctor|url|platform query]"
---

# Agent Reach Skill (`/agent-reach`)

Use this skill to access, query, search, or diagnose connectivity across 10+ social and web platforms without manual browser setup.

---

## Capabilities & Usage Guide

### 1. Diagnostics & Health Check
Run diagnostic check to view active platform backends:
```powershell
python scripts/agent_reach_runner.py doctor
```
or via global CLI:
```bash
agent-reach doctor
```

### 2. Supported Platforms & Quick Commands

- 🌐 **Web Reading**: Fetch clean Markdown for any URL:
  `curl https://r.jina.ai/<URL>`

- 📺 **YouTube Subtitles & Info**:
  `yt-dlp --write-sub --sub-lang en,zh-Hans --skip-download <URL>`

- 📺 **Bilibili Search & Details**:
  `bili search "<query>"` (Zero config, no login needed)

- 💻 **V2EX Discussions**:
  Query hot tech topics, node posts, and replies via V2EX API.

- 📦 **GitHub Repositories**:
  `gh repo view <owner/repo>`
  `gh search repos "<query>"`

- 📡 **RSS / Atom Feeds**:
  Parse feeds via `feedparser`.

- 🔍 **AI Web Search**:
  Execute semantic web search via Exa / Jina.

- 🐦 **Twitter / X**:
  `twitter tweet <URL>` or `twitter search "<query>"` (Requires cookie setup)

- 📖 **Reddit / XiaoHongShu / Facebook / Instagram**:
  Uses desktop `OpenCLI` to reuse logged-in Chrome sessions without manual API keys.

---

## Architectural Principles

1. **Ordered Backend Fallback**: If a backend suffers anti-scraping blocks (e.g. 412 rate limits), the router dynamically cascades to the secondary fallback backend.
2. **Local Credential Privacy**: Cookies and tokens reside strictly in `~/.agent-reach/config.yaml` (`0600` POSIX permissions). No remote leakage.
