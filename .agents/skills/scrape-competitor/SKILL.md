---
name: scrape-competitor
description: Use when the user wants to scrape a competitor's profile, run competitor content research, or parse scraped reels/posts across YouTube, Bilibili, Twitter, Reddit, V2EX, or web pages.
argument-hint: [competitor url, handle, or topic]
---

## What This Skill Does

Automates multi-platform competitor content research. It routes requests through **Agent Reach** (`/agent-reach`) and **Scrapling** to fetch transcripts, community posts, tweets, and articles, structures the data into content pillars, and saves them as cross-linked research markdown files in the Zorixel Second Brain.

## Multi-Platform Routing Pipeline

1. **Platform Detection & Data Fetching**:
   - **YouTube Video / Channel**: Route via Agent Reach (`yt-dlp` subtitle & metadata engine):
     `yt-dlp --write-sub --sub-lang en,zh-Hans --skip-download "$URL"`
   - **Bilibili Tech Content**: Route via Agent Reach (`bili-cli`):
     `bili search "$QUERY"` or `bili video "$URL"`
   - **V2EX / Reddit Community Sentiment**: Route via Agent Reach (`v2ex` / `rdt-cli` / `OpenCLI`):
     Query community posts, thread comments, and user feedback.
   - **General Web / Articles**: Fetch stealthily via Scrapling or Agent Reach Jina Reader:
     `python scripts/scrapling_runner.py --url "$URL" --mode stealth --text-only`
     or `curl https://r.jina.ai/$URL`

2. **Input Processing & Breakdown**:
   - Parse and clean transcripts, captions, hooks, CTAs, and user comment sentiment.
   - Categorize into ZORIXEL content pillars:
     - **UI Resources / Web Design**
     - **GSAP / Three.js Animations**
     - **AI OS & Automations**
     - **Creator Workflow / Vibe Coding**

3. **Vault Persistence**:
   - Save output as a new research file under `second-brain-zorixel/wiki/research/competitor-[name]-[date].md`.
   - Update `second-brain-zorixel/wiki/index.md` and `second-brain-zorixel/wiki/log.md`.

4. **Strategic Synthesis**:
   - Present the parsed competitor breakdown highlighting hook mechanics, script visual structure, CTA conversion levers, and AI automation takeaways.
