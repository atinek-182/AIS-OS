import os
import re

workspace_root = r"d:\AI-OS"
exclude_dirs = {".git", ".obsidian", "node_modules"}
target_extensions = {".md", ".json", ".txt", ".py", ".js", ".ts"}

replacements = [
    ("Claude Code", "Antigravity"),
    ("Claude", "Antigravity"),
    ("CLAUDE.md", "GEMINI.md"),
    (".claude", ".agents"),
    ("CLAUDE_SESSION_ID", "ANTIGRAVITY_SESSION_ID")
]

scanned_files = []
modified_files = []
replacement_summary = {}

for root, dirs, files in os.walk(workspace_root):
    # Exclude directories
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
            
            for old, new in replacements:
                # Find occurrences (case sensitive as per agent-adapt instructions)
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

print("=== AGENT-ADAPT MIGRATION REPORT ===")
print(f"Total Scanned Files: {len(scanned_files)}")
print(f"Total Modified Files: {len(modified_files)}\n")

if modified_files:
    print("Modified Files Details:")
    for filepath in modified_files:
        rel_path = os.path.relpath(filepath, workspace_root)
        print(f"- {rel_path}:")
        for summary in replacement_summary[filepath]:
            print(f"  * {summary}")
else:
    print("No files were modified.")
