import os
import re

workspace_root = r"d:\AI-OS"
exclude_dirs = {".git", ".obsidian", "node_modules"}
target_extensions = {".md", ".json", ".txt", ".py", ".js", ".ts"}

filename_mappings = [
    ("2026-07-14-build-&-sell-claude-code-operating-systems-(2+-hour-course).md",
     "2026-07-14-build-&-sell-antigravity-operating-systems-(2+-hour-course).md"),
    ("2026-07-14-i-tried-100+-claude-code-skills.-these-6-are-the-best.md",
     "2026-07-14-i-tried-100+-antigravity-skills.-these-6-are-the-best.md"),
    ("claude-code-aios-course.md", "antigravity-aios-course.md"),
    ("claude-code-best-skills.md", "antigravity-best-skills.md")
]

text_replacements = [
    ("2026-07-14-build-&-sell-claude-code-operating-systems-(2+-hour-course).md",
     "2026-07-14-build-&-sell-antigravity-operating-systems-(2+-hour-course).md"),
    ("2026-07-14-build-&-sell-claude-code-operating-systems-(2+-hour-course)",
     "2026-07-14-build-&-sell-antigravity-operating-systems-(2+-hour-course)"),
    ("2026-07-14-i-tried-100+-claude-code-skills.-these-6-are-the-best.md",
     "2026-07-14-i-tried-100+-antigravity-skills.-these-6-are-the-best.md"),
    ("2026-07-14-i-tried-100+-claude-code-skills.-these-6-are-the-best",
     "2026-07-14-i-tried-100+-antigravity-skills.-these-6-are-the-best"),
    ("claude-code-aios-course.md", "antigravity-aios-course.md"),
    ("claude-code-aios-course", "antigravity-aios-course"),
    ("claude-code-best-skills.md", "antigravity-best-skills.md"),
    ("claude-code-best-skills", "antigravity-best-skills"),
    ("claude-code", "antigravity"),
    ("claude", "antigravity")
]

renamed_files = []
for old_name, new_name in filename_mappings:
    found_path = None
    for root, dirs, files in os.walk(workspace_root, followlinks=True):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        if old_name in files:
            found_path = os.path.join(root, old_name)
            break
    
    if found_path:
        new_path = os.path.join(os.path.dirname(found_path), new_name)
        try:
            os.rename(found_path, new_path)
            print(f"Renamed: {found_path} -> {new_path}")
            renamed_files.append((found_path, new_path))
        except Exception as e:
            print(f"Error renaming {found_path}: {e}")

scanned_files = []
modified_files = []
replacement_summary = {}

for root, dirs, files in os.walk(workspace_root, followlinks=True):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        _, ext = os.path.splitext(file)
        if ext.lower() in target_extensions:
            filepath = os.path.join(root, file)
            scanned_files.append(filepath)
            
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                print(f"Skipping {filepath} due to read error: {e}")
                continue
            
            original_content = content
            file_replacements = []
            
            for old, new in text_replacements:
                count = len(re.findall(re.escape(old), content))
                if count > 0:
                    content = content.replace(old, new)
                    file_replacements.append(f"'{old}' -> '{new}' ({count} times)")
            
            if content != original_content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    modified_files.append(filepath)
                    replacement_summary[filepath] = file_replacements
                except Exception as e:
                    print(f"Failed to write modified file {filepath}: {e}")

print("\n=== TEXT REPLACEMENT REPORT ===")
print(f"Total Scanned Files: {len(scanned_files)}")
print(f"Total Modified Files: {len(modified_files)}\n")

for filepath in modified_files:
    rel_path = os.path.relpath(filepath, workspace_root)
    print(f"- {rel_path}:")
    for summary in replacement_summary[filepath]:
        print(f"  * {summary}")
