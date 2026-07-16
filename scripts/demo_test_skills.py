import os
import re

workspace_root = r"d:\AI-OS"
exclude_dirs = {".git", ".obsidian", "node_modules"}

print("=== SKILLS DEMO TEST RUN ===\n")

# 1. Test /file-search logic
print("--- TEST 1: /file-search ('GSAP') ---")
search_query = "GSAP"
matches = []

for root, dirs, files in os.walk(workspace_root, followlinks=True):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for idx, line in enumerate(lines):
                    if search_query.lower() in line.lower():
                        matches.append((filepath, idx + 1, line.strip()))
            except Exception:
                pass

if matches:
    print(f"Found {len(matches)} matches for '{search_query}':")
    for path, line_no, content in matches[:5]: # Show top 5
        rel_path = os.path.relpath(path, workspace_root)
        print(f"  * [{rel_path}:L{line_no}]: {content}")
else:
    print("No matches found.")
print()

# 2. Test /draft-message logic
print("--- TEST 2: /draft-message (Instagram DM) ---")
# Voice Guidelines: casual, energetic, conversational, 'hey', 'just', 'wanna', 'insane', short sentences, minimal punctuation, bullet points over paragraphs
recipient = "freelancer"
platform = "Instagram DM"
user_prompt = "Hey, how do I get started with GSAP?"

print(f"Platform: {platform}")
print(f"Recipient: {recipient}")
print(f"Prompt: {user_prompt}\n")

variations = [
    # Var 1
    "hey! just start with the basics. check out their official docs and copy their simple scrolltrigger templates. it's actually insane what you can do with a few lines. wanna share what project you're building?",
    # Var 2
    "hey there! GSAP is insane once you get it. i'd suggest starting with simple tween animations first, then move to scrolltrigger. just take it step by step. what's your design stack looking like?",
    # Var 3
    "hey! just download their starter template on codepen. it makes it super easy to play around. scrolltrigger is the magic sauce. let me know if you wanna link to a quick tutorial i made."
]

for idx, var in enumerate(variations):
    print(f"Variation {idx+1}:")
    print(f"  {var}")
print()

# 3. Test /daily-plan-day logic
print("--- TEST 3: /daily-plan-day ---")
priorities = "Launching ZORIXEL (Instagram publishing & website), AI OS workflows"
tasks = [
    "- [x] Configure core Antigravity/Claude plugins",
    "- [/] Draft Instagram content",
    "- [ ] Build Sheets logger"
]
print(f"Priorities: {priorities}")
print("Active Tasks:")
for t in tasks:
    print(f"  {t}")

print("\nGenerated Daily Schedule:")
print("| Time | Task / Block | Focus Area |")
print("|---|---|---|")
print("| 09:00 - 10:00 | Morning Routine & Priority Review | Context |")
print("| 10:00 - 12:30 | Draft first week's content (5 reels) | Zorixel Launch |")
print("| 12:30 - 13:30 | Lunch Break | - |")
print("| 13:30 - 16:00 | Build competitor scraper skill | AIOS Workflows |")
print("| 16:00 - 17:00 | Review/test custom skills | Verification |")
print("| 17:00 - 18:00 | Evening loop (/daily-review-day) & plan tomorrow | Cadence |")
print()

# 4. Test /daily-review-day logic
print("--- TEST 4: /daily-review-day ---")
completed_tasks = ["Configure core Antigravity/Claude plugins", "Verify custom skills"]
manual_tasks = "Manually logging hours in excel and messaging team about task status"
time_saved = "45 minutes"

print(f"Tasks Completed: {', '.join(completed_tasks)}")
print(f"Manual overhead identified: {manual_tasks}")
print(f"Estimated time saved: {time_saved}")
print("\nReflection Action Items:")
print(f"1. Mark {len(completed_tasks)} tasks as [x] in master-task-list.md.")
print(f"2. Log new automation candidate for next /level-up session: '{manual_tasks}'.")
print(f"3. Log time saved data ({time_saved}) in the log files.")
