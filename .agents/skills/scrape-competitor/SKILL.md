---
name: scrape-competitor
description: Use when the user wants to scrape a competitor's profile, run competitor content research, or parse scraped reels/posts.
argument-hint: [competitor url or topic]
---

## What This Skill Does

Automates the competitor content research pipeline. It guides the user through social media scraping collections, accepts raw scraped text or JSON inputs, structures the data into content pillars, and saves them as cross-linked research markdown files in the Zorixel Second Brain.

## Steps

1. If a competitor URL or topic is provided in `$ARGUMENTS`, search for relevant reference files or print instructions on how to use the `rtrvr.ai` browser extension to scrape their feed.
2. Prompt the user to paste the raw JSON or text output from their scraper clipper (e.g., fields: Profile, Topic, Transcript, Offering, Caption, Hashtags, CTA, Hook).
3. Once input is received:
   - Parse and clean the fields.
   - Categorize the competitor's post into ZORIXEL content pillars:
     - **UI Resources / Web Design**
     - **GSAP Animations**
     - **AI Automations**
     - **Creator Workflow**
   - Save the output as a new research file under [research/](file:///d:/AI-OS/second-brain-zorixel/wiki/research/) (e.g., `second-brain-zorixel/wiki/research/competitor-[name]-[date].md`).
   - Append a link to the new file in [index.md](file:///d:/AI-OS/second-brain-zorixel/wiki/index.md) and [log.md](file:///d:/AI-OS/second-brain-zorixel/wiki/log.md).
4. Present the parsed, structured analysis to the user, highlighting their hook, CTA, and offer strategy.
