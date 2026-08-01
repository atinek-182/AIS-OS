# -*- coding: utf-8 -*-
import os
import shutil
import json

base_dir = r"D:\ZORIXEL-BRAND-OS\research"
yt_dir = os.path.join(base_dir, "youtube-transcripts")
fw_dir = os.path.join(base_dir, "frameworks")

os.makedirs(yt_dir, exist_ok=True)
os.makedirs(fw_dir, exist_ok=True)

video_map = {
    "8LL5Z9Lz0-4": {
        "filename": "01-10k-claude-ai-side-hustle.md",
        "title": "How I'd Start a $10K/Month Claude AI Side Hustle That Pays More Than a 9-5",
        "url": "https://youtu.be/8LL5Z9Lz0-4",
        "channel": "Patrick Dang",
        "skills": ["pd-1-person-business"]
    },
    "gRcBu8LyfGo": {
        "filename": "02-1-person-business-claude-30-days.md",
        "title": "How I'd Start a 1-Person Business With Claude AI in 30 Days",
        "url": "https://youtu.be/gRcBu8LyfGo",
        "channel": "Patrick Dang",
        "skills": ["pd-ikigai-pro"]
    },
    "DuOolRhG2UY": {
        "filename": "03-10k-one-person-business-claude-masterclass.md",
        "title": "How I'd Start a $10K/Month One-Person Business With Claude (Masterclass)",
        "url": "https://youtu.be/DuOolRhG2UY",
        "channel": "Patrick Dang",
        "skills": ["pd-1-person-business"]
    },
    "4lbl9MtKUF8": {
        "filename": "04-claude-ai-premium-personal-brand.md",
        "title": "How I'd Use Claude AI to Build a Premium Personal Brand (1-Person Business)",
        "url": "https://youtu.be/4lbl9MtKUF8",
        "channel": "Patrick Dang",
        "skills": ["pd-ikigai-pro", "pd-personal-brand-positioning"]
    },
    "qy_MIMtT_d8": {
        "filename": "05-job-to-1-person-business-claude.md",
        "title": "If you have a Job, Start a 1-Person Business with Claude AI ASAP",
        "url": "https://youtu.be/qy_MIMtT_d8",
        "channel": "Patrick Dang",
        "skills": ["pd-1-person-business"]
    }
}

print("1. Reorganizing YouTube Video Research Notes...")

# Build clean markdown files for YouTube transcripts
for vid, info in video_map.items():
    txt_file = os.path.join(yt_dir, f"{vid}_transcript.txt")
    target_md = os.path.join(yt_dir, info["filename"])
    
    if os.path.exists(txt_file):
        with open(txt_file, 'r', encoding='utf-8') as f:
            txt_content = f.read()
            
        md_text = f"""---
title: "{info['title']}"
video_id: "{vid}"
url: "{info['url']}"
channel: "{info['channel']}"
skills: {json.dumps(info['skills'])}
type: youtube-transcript
date_ingested: 2026-07-30
---

# 📺 YouTube Research: {info['title']}

- **Channel:** {info['channel']}
- **Video Link:** [{info['url']}]({info['url']})
- **Associated Skill(s):** {', '.join([f'`{s}`' for s in info['skills']])}
- **Transcript Length:** ~{len(txt_content.split())} words

---

## 🎯 Executive Summary & Frameworks

- **Founder X Model:** 3-Step growth loop: Offer $\\rightarrow$ Lead Generation $\\rightarrow$ Monetization.
- **Offer Triangle:** What to Sell (AI-Powered Service) $\\rightarrow$ Who to Sell to (Able & Willing Buyers) $\\rightarrow$ Pricing (High Ticket / Value Based).
- **Positioning:** Async sales closing via DMs, Loom video teardowns, and Notion proposals without live Zoom call friction.

---

## 📝 Full Transcript

{txt_content}
"""
        with open(target_md, 'w', encoding='utf-8') as f:
            f.write(md_text)
        print(f"  [CREATED] {info['filename']}")

# Clean up raw cryptic ID files (.txt and .json)
for file in os.listdir(yt_dir):
    if file.endswith(".txt") or file.endswith(".json") or (file.endswith("_summary.md") and not file.startswith("0")):
        os.remove(os.path.join(yt_dir, file))
        print(f"  [CLEANED] Removed raw file: {file}")

print("2. Creating Detailed Deep Topic Framework Manuals...")

# Framework 1: Offer Triangle & Pricing
fw1 = os.path.join(fw_dir, "01-offer-triangle-and-pricing-architecture.md")
with open(fw1, 'w', encoding='utf-8') as f:
    f.write("""# 📐 Framework 01: The Offer Triangle & High-Ticket Pricing Architecture

## 1. The Offer Triangle Mechanics
1. **What to Sell:** AI Workflows & Business Automations + Custom Web UI Dashboards. AI agents perform 80% of operational work, human engineering provides system architecture and visual polish.
2. **Who to Sell To:** Business owners, founders, SMBs, and agency leads seeking operational bottleneck resolution.
3. **Pricing Model:** Value-based DFY Build Sprint pricing ($1,500 – $5,000+ per sprint). Never charge hourly.

## 2. The 3 Pricing Tiers
- **Foundation Sprint Tier:** $1,500 (Basic bottleneck resolution + n8n/Python agent build).
- **Engine Sprint Tier (Recommended Start):** $2,500–$3,500 (Complete multi-agent workflow + custom Next.js web dashboard).
- **Operator Enterprise Tier:** $5,000+ (Full autonomous business infrastructure + ongoing system tuning).
""")

# Framework 2: 100% Async Sales
fw2 = os.path.join(fw_dir, "02-100-percent-async-b2b-sales-and-loom-teardowns.md")
with open(fw2, 'w', encoding='utf-8') as f:
    f.write("""# 🤝 Framework 02: 100% Asynchronous B2B Sales & Loom Video Teardowns

## 1. Why Async Closing Wins in 2026
Modern SaaS founders and agency owners hate 45-minute sales calls. Closing asynchronously via text DMs, 2-minute Loom teardowns, and Notion proposals eliminates meeting friction and closes clients on visual proof.

## 2. The Loom Teardown Script
1. **Personalized Hook (15s):** Acknowledge recent milestone/funding.
2. **Friction Identification (30s):** Point out generic typography or missing mobile micro-interactions.
3. **Interactive Prototype (45s):** Show live interactive component redesign built in local AIOS stack.
4. **Low-Friction CTA (30s):** Offer to send Notion proposal link.
""")

# Framework 3: Speed-to-Lead & Intake Automations
fw3 = os.path.join(fw_dir, "03-speed-to-lead-and-intake-automations.md")
with open(fw3, 'w', encoding='utf-8') as f:
    f.write("""# ⚡ Framework 03: Speed-to-Lead & Instant Intake Automations

## 1. The <5-Minute Lead Response Rule
78% of B2B clients buy from the vendor that responds first. Responding in under 300 seconds increases lead qualification by 21x.

## 2. Review & Missed-Call Text-Back Automations
- **Review Automation:** Automated post-service SMS/email requesting Google reviews.
- **Missed-Call Text-Back:** Instant text sent to missed inbound calls to retain local leads.
""")

# Framework 4: India Global Arbitrage Model
fw4 = os.path.join(fw_dir, "04-india-global-async-arbitrage-model.md")
with open(fw4, 'w', encoding='utf-8') as f:
    f.write("""# 🇮🇳 Framework 04: The India Global Async Arbitrage Model

## 1. Arbitrage Economics
Operating from India at 100% zero local overhead while charging global US/Western rates ($3,000 per sprint).
- $3,000 USD $\\approx$ ₹2,50,000 INR per sale.
- 3 Sales/Month = $10,500/mo $\\approx$ ₹8.5 Lakhs INR/month.

## 2. Zero-Cost Tech Stack
- Anthropic Claude / Antigravity IDE
- Playwright Headless Visual QA
- Scrapling Stealth Scraper Engine
- Local Component & Shader Vault
""")

# Framework 5: Screen-First Branding
fw5 = os.path.join(fw_dir, "05-screen-first-branding-and-micro-graphics.md")
with open(fw5, 'w', encoding='utf-8') as f:
    f.write("""# 🎨 Framework 05: Screen-First Personal Branding & Micro-Graphics

## 1. No-Camera Personal Brand Architecture
Building a high-converting brand using screen-share videos, code walkthroughs, slide graphics (`/frontend-slides`), and audio voiceover.

## 2. Destroying AI Slop
Replacing generic purple gradients with locked OKLCH tokens, custom typography (`Rosehot`/`Nuqun` + `Outfit`), and GSAP micro-interactions.
""")

print("3. Creating Central Master Research Index (INDEX.md)...")

index_md = os.path.join(base_dir, "INDEX.md")
with open(index_md, 'w', encoding='utf-8') as f:
    f.write("""# 📚 ZORIXEL Brand OS — Master Research & Frameworks Index

Welcome to the central research index of the **ZORIXEL Brand Operating System**. This document links all ingested transcripts, field manuals, and deep framework guides.

---

## 📺 YouTube Video Ingestion Vault (`research/youtube-transcripts/`)

1. [01-10k-claude-ai-side-hustle.md](file:///D:/ZORIXEL-BRAND-OS/research/youtube-transcripts/01-10k-claude-ai-side-hustle.md) — *How I'd Start a $10K/Month Claude AI Side Hustle*
2. [02-1-person-business-claude-30-days.md](file:///D:/ZORIXEL-BRAND-OS/research/youtube-transcripts/02-1-person-business-claude-30-days.md) — *1-Person Business With Claude AI in 30 Days*
3. [03-10k-one-person-business-claude-masterclass.md](file:///D:/ZORIXEL-BRAND-OS/research/youtube-transcripts/03-10k-one-person-business-claude-masterclass.md) — *$10K/Month One-Person Business Masterclass*
4. [04-claude-ai-premium-personal-brand.md](file:///D:/ZORIXEL-BRAND-OS/research/youtube-transcripts/04-claude-ai-premium-personal-brand.md) — *Premium Personal Brand (1-Person Business)*
5. [05-job-to-1-person-business-claude.md](file:///D:/ZORIXEL-BRAND-OS/research/youtube-transcripts/05-job-to-1-person-business-claude.md) — *Job to 1-Person Business with Claude AI*

---

## 📖 Field Manuals & PDF Ingestions (`research/`)

1. [the-first-client-playbook.md](file:///D:/ZORIXEL-BRAND-OS/research/the-first-client-playbook.md) — *Adam Erhart's 40-Page The First Client Playbook*

---

## 🧠 Deep Framework Manuals (`research/frameworks/`)

1. [01-offer-triangle-and-pricing-architecture.md](file:///D:/ZORIXEL-BRAND-OS/research/frameworks/01-offer-triangle-and-pricing-architecture.md) — *Offer Triangle & $3k Pricing Architecture*
2. [02-100-percent-async-b2b-sales-and-loom-teardowns.md](file:///D:/ZORIXEL-BRAND-OS/research/frameworks/02-100-percent-async-b2b-sales-and-loom-teardowns.md) — *100% Async Closing & Loom Teardowns*
3. [03-speed-to-lead-and-intake-automations.md](file:///D:/ZORIXEL-BRAND-OS/research/frameworks/03-speed-to-lead-and-intake-automations.md) — *<5-Min Speed-to-Lead & Intake Automations*
4. [04-india-global-async-arbitrage-model.md](file:///D:/ZORIXEL-BRAND-OS/research/frameworks/04-india-global-async-arbitrage-model.md) — *India Global Async Arbitrage & $0 Overhead Stack*
5. [05-screen-first-branding-and-micro-graphics.md](file:///D:/ZORIXEL-BRAND-OS/research/frameworks/05-screen-first-branding-and-micro-graphics.md) — *Screen-First Branding & Micro-Graphics*

---

## 🎯 Master Strategy & Operating Playbooks (`strategy/` & `deliverables/`)

1. [ZORIXEL_FOUNDATION_MASTER_STRATEGY.md](file:///D:/ZORIXEL-BRAND-OS/strategy/ZORIXEL_FOUNDATION_MASTER_STRATEGY.md) — *Master Foundation Strategy*
2. [personal-brand-positioning.md](file:///D:/ZORIXEL-BRAND-OS/strategy/personal-brand-positioning.md) — *Personal Brand Positioning Brief*
3. [service-offer-spec.md](file:///D:/ZORIXEL-BRAND-OS/strategy/service-offer-spec.md) — *14-Day $3,000 Web Experience Sprint Spec*
4. [zorixel-master-brand-playbook.html](file:///D:/ZORIXEL-BRAND-OS/deliverables/zorixel-master-brand-playbook.html) — *Master Brand Playbook HTML Report*
""")

print("Organize and indexing process complete.")
