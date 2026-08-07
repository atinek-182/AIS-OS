# Client Setup Guide Presentation: Discovery & Setup Notes
Date: 2026-08-06 · Goal: Client-Facing Onboarding & Setup Manual HTML Deck · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Brand Typography Applied**: Big primary display headlines in `Havock` (Base64 inlined `.otf`), subheadings and section tags in `Rosehot` (Base64 inlined `.ttf`), body text in clean `Outfit` sans.
- **Client-Centric Copywriting (/humanizer)**: Reframed entirely as a 4-step onboarding guide written **for the client** to set up the template on their own Google account & Notion workspace.
- **Strict Anonymization & Data Hygiene**: Completely removed all internal Notion database IDs (`355543dfcd8541af9d2420adb903959b`), Vashishthya names, and personal emails (`parsjp17@gmail.com`). Replaced with clean, copyable placeholders (`[YOUR_NOTION_SECRET_TOKEN]`, `[YOUR_NOTION_DATABASE_ID]`, `[YOUR_COMPANY_NAME]`).
- **Visual Mockups**: Re-rendered 7 slide mockups with simplified non-technical step descriptions and clear UI callouts.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **Client Onboarding Guide**: A self-contained, 16:9 interactive HTML deck that guides non-technical client operators through linking their Notion workspace to Google Sheets.
- **Havock & Rosehot Base64 Inlining**: Embeds OTF/TTF font files as base64 Data URIs directly in CSS `@font-face` blocks to eliminate external asset dependency crashes.

## Q&A Log
### Q2 — Reframing for Client Audience & Brand Typography
- **Fonts Used**: `Havock` (Big headline hero), `Rosehot` (Editorial tags), `Outfit` (Body).
- **Tone & Copywriting**: Applied `/humanizer` rules — plain English, active voice, zero AI fluff words ("tapestry", "delve"), zero em dashes, simple 4-step structure.
