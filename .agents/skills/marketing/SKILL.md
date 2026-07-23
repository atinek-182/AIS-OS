---
name: marketing
description: Use when copywriting, writing or improving marketing copy, headlines, CTAs, landing page copy, value propositions, taglines, email sequences, or drafting Instagram reels/captions.
---

# Marketing & Copywriting Router Skill

When this skill is triggered, you will route the copywriting or marketing task using the reference libraries in the static skills-library.

## Step-by-Step Execution Workflow

### 1. Identify the Task Category & VoC Research Integration
Map the user's request to one of the following copywriting/marketing categories in the static library:
* **`copywriting`**: General copywriting guidelines, PAS (Problem-Agitation-Solution) framework, homepage, landing pages.
* **`emails`**: Email marketing sequences, newsletters, onboarding series.
* **`pricing`**: Pricing page strategy, plans comparison, risk reversals.
* **`cro`**: Conversion rate optimization, page flow, visual hierarchy audits.
* **`social`**: Social media copy, Instagram Reels drafts, LinkedIn posts.
* **`competitor-profiling`**: Researching competitor hooks and positioning via **Agent Reach** (`/agent-reach`).
* **`customer-research`**: Mapping customer pain points & Voice of Customer (VoC) by querying real-world community sentiment across Reddit, V2EX, Twitter, and YouTube transcripts via **Agent Reach**.
* **`offers`**: Constructing guarantees, bonuses, value framing.

### 2. Read the Reference Skill File
Once the category is identified, read the corresponding reference file using the `view_file` tool:
`d:\AI-OS\brain-aios\wiki\research\skills-library/marketingskills/skills/{category}/SKILL.md`

*(Also check if there are reference files like `references/copy-frameworks.md` inside that folder, and read them if more depth is needed.)*

### 3. Check for Context Files
Before drafting, check if product marketing context is available in the workspace:
* Check [product-marketing.md](file:///d:/AI-OS/context/product-marketing.md) or similar files in `d:\AI-OS\context/` or `d:\AI-OS/`.
* Check the ZORIXEL brand voice in [voice.md](file:///d:/AI-OS/references/voice.md).

### 4. Execute and Produce Output
Apply the rules, style constraints (clear > clever, specific > vague, active voice, removal of jargon), and guidelines from the reference file. Output must include:
* The drafted copy (structured by page section).
* Design/strategy annotations explaining why choices were made.
* 2-3 headline/CTA alternatives.
