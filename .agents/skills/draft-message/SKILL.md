---
name: draft-message
description: Use when the user wants to draft an Instagram DM, reply to an email, or write comments/replies using the ZORIXEL brand voice.
argument-hint: [recipient and context]
---

## What This Skill Does

Automates the drafting of emails, DMs, and community replies. It loads the brand personality and voice rules, gathers message constraints, generates 3 on-brand variations, and integrates with the Google Workspace CLI to create Gmail drafts.

## Steps

1. Read brand voice guidelines from [personality-and-voice.md](file:///d:/AI-OS/second-brain-zorixel/wiki/brand/personality-and-voice.md).
2. Gather context:
   - Platform (Instagram DM, Gmail, YouTube Comment)
   - Goal/Intent (Reply to client, request collaboration, reply to follower)
   - Recipient details or input message
3. Generate 3 distinct variations of the message matching the core voice parameters:
   - Casual, energetic, conversational (uses words like 'hey', 'just', 'wanna', 'insane').
   - Minimal punctuation/capitalization in DMs, highly structured but conversational.
   - Short sentences, no em dashes, bullet points over paragraphs.
4. Present the drafts to the user.
5. If the user selects a draft for Gmail, convert it to an RFC822 raw email and use the GWS CLI to create a draft in their inbox:
   ```powershell
   # Set context (personal or brand) and invoke GWS Gmail drafts create
   $env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_brand.json"; gws gmail users drafts create --params '{"userId": "me"}' --json '{"message": {"raw": "BASE64_ENCODED_MESSAGE"}}'
   ```
