import os

locations = [
    r'd:\AI-OS\.agents\skills\grill-me\SKILL.md',
    r'C:\Users\HP\.gemini\config\skills\grill-me\SKILL.md',
]

# Check if plugin folder exists
plugin_path = r'C:\Users\HP\.gemini\config\plugins\superpowers\skills\grill-me\SKILL.md'
if os.path.exists(os.path.dirname(plugin_path)):
    locations.append(plugin_path)

grillme_content = """---
name: grill-me
description: Interview the user relentlessly about a plan, design, or topic, checkpointing
  every answer to a brainstorm file so nothing is lost. Use when the user wants to
  stress-test a plan, get grilled on a design, run a brainstorm or discovery session,
  extract what's in their head into a doc, or says "grill me". Invokable directly
  via /grill-me.
argument-hint: '[optional parameters]'
---

# Grill Me (`/grill-me`)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/grill-me [optional parameters]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills or subagents via `/grill-me` or by reading `SKILL.md` directly.

---

## 📌 Non-Negotiable Core Execution Rules

1. **Global Zero-Hurry & Rigor Mandate**:  
   Never rush the discovery session. Complex systems take time (weeks or months). Deep exploration, option-based Q&A, and architectural rigor take absolute precedence over speed.

2. **Concept Explanation BEFORE Every Question**:  
   If the user has not watched a video, read source documentation, or touched a specific topic, **ALWAYS explain the underlying concept in clear, plain language FIRST** before asking any question or making a suggestion.

3. **Proactive Web Search Research**:  
   Before asking a question or offering options, search the web to discover industry-leading best practices, modern tools, or trending features in the target domain.

4. **Exhaustive Option-Based Inquiries**:  
   Present detailed, structured multiple-choice options for every question (with your recommended answer highlighted) so the user can easily confirm, correct, or redirect. Never artificially limit questions to 2-3 vague queries — ask as many detailed questions as needed until every decision branch is resolved.

5. **Pre-Write Feature Confirmation Check**:  
   Before generating any document content, spec file, or code, explicitly ask the user:  
   *"Would you like to add any additional features, suggestions, or modifications before I finalize this document/code?"*

6. **Checkpoint to Disk After Every Single Answer**:  
   Immediately append to `brainstorms/{YYYY-MM-DD}-{topic-slug}.md` after every user response BEFORE asking the next question. The capture file is the single source of truth.

7. **Mandatory Pre-Write `/roast` Council Audit**:  
   Run the `/roast` skill (5 persona council: Contrarian, Expansionist, Logician, Researcher, Buyer) to pressure-test every document concept before emitting final content.

8. **Pre-Coding Backstop**:  
   Before concluding the interview or moving to implementation, ask:  
   *"Is there anything else remaining before we touch the code?"*

---

## Setup (do this BEFORE the first question)

1. Create the capture file at `brainstorms/{YYYY-MM-DD}-{topic-slug}.md`.
2. Notify the user of the file path in one line.
3. Explain **Concept 1** in clear language, then ask **Question 1** with structured options and your recommended answer highlighted.

---

## Capture File Structure

```markdown
# {Topic}: Brainstorm / Discovery Notes
Date: {date} · Goal: {one line}

## Summary / key decisions
(running synthesis, updated as you go)

## Q&A log
### Q1 — {topic}
- Asked: {question}
- Captured: {facts, decisions, in their words where it matters}
- Flags: {open item -> owner}

## Open flags (pending input)
- {item} -> {who can answer}
```

---

## At the End of Session

1. Do a final read of the capture file for contradictions or gaps and reconcile them.
2. Convene the 5-persona `/roast` council to audit the captured decisions.
3. Give the user a short recap: what's captured, what's flagged, and the suggested next steps.
4. Execute the Pre-Coding Backstop check (*"Is there anything else remaining before we touch the code?"*).
"""

for path in locations:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(grillme_content)
    print(f"Upgraded grill-me skill at: {path}")
