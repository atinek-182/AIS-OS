---
name: scrape-web
description: Scraping, dynamic HTML parsing, anti-bot bypass, and adaptive element extraction using Scrapling engine. Use when scraping web content, extracting structured text/DOM elements, or fetching dynamic/stealth web pages.
argument-hint: [url] [--mode fast|dynamic|stealth] [--css selector]
---

# Scrape Web Skill (Scrapling Engine)

Use this skill whenever you need to scrape live web pages, bypass anti-bot mechanisms, extract structured DOM elements, or fetch content resiliently without manual site mirroring.

## Engine Overview

The skill is powered by the local Python Scrapling engine at `scripts/scrapling_runner.py`.

### Fetcher Modes:
1. **`fast` (Default)**: Lightweight HTTP request parser powered by Scrapling's adaptive parser. Instant, token-efficient, ideal for standard web pages, blogs, and static sites.
2. **`dynamic`**: Headless browser execution powered by Playwright. Executes JavaScript, handles client-side rendered single-page apps (React, Next.js, Vue).
3. **`stealth`**: Anti-bot stealth mode powered by Scrapling's `StealthyFetcher`. Emulates browser signatures and circumvents basic Cloudflare/bot protections.

---

## Usage Guide

### 1. Basic Web Extraction (Fast Mode)
```powershell
python scripts/scrapling_runner.py --url "https://example.com" --mode fast
```

### 2. Extract Specific Elements by CSS Selector
```powershell
python scripts/scrapling_runner.py --url "https://news.ycombinator.com" --mode fast --css ".titleline > a"
```

### 3. Dynamic JavaScript Rendering
```powershell
python scripts/scrapling_runner.py --url "https://target-spa-app.com" --mode dynamic --text-only
```

### 4. Stealth Mode for Protected Sites
```powershell
python scripts/scrapling_runner.py --url "https://protected-site.com" --mode stealth --output "second-brain-zorixel/wiki/research/scraped-data.json"
```

---

## Integration with AIOS Vaults & Workflows

1. **Competitor & Content Research**:
   - Use `/scrape-web` to pull post captions, transcripts, and headers.
   - Save output under `second-brain-zorixel/wiki/research/`.

2. **SEO & Meta Auditing**:
   - Run `/scrape-web` with `--css "meta, h1, h2, title"` to perform instant meta schema audits without launching full browser GUI sessions.

3. **Comparison with `/scrape-reference`**:
   - Use **`/scrape-web`** when you need **fast data, text, or DOM element extraction**.
   - Use **`/scrape-reference`** when you need **full offline visual asset cloning (CSS files, local fonts, 3D models, images)**.
