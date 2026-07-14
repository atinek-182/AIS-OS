import os
import shutil
import re

source_dirs = [
    r"C:\Users\HP\.claude\skills",
    r"C:\Users\HP\.claude\plugins\marketplaces\context-mode\skills",
    r"C:\Users\HP\.claude\plugins\marketplaces\thedotmack\plugin\skills"
]
target_dir = r"C:\Users\HP\.gemini\config\skills"

replacements = [
    ("Claude Code", "Antigravity"),
    ("Claude", "Antigravity"),
    ("CLAUDE.md", "GEMINI.md"),
    (".claude", ".agents"),
    ("CLAUDE_SESSION_ID", "ANTIGRAVITY_SESSION_ID"),
    # General lower-case occurrences
    ("claude-code", "antigravity"),
    ("claude", "antigravity")
]

os.makedirs(target_dir, exist_ok=True)

copied_count = 0
modified_count = 0

for source_root in source_dirs:
    if not os.path.exists(source_root):
        print(f"Skipping non-existent source root: {source_root}")
        continue
    
    # List immediate children sub-directories (each folder represents a skill)
    for skill_name in os.listdir(source_root):
        skill_src_path = os.path.join(source_root, skill_name)
        if os.path.isdir(skill_src_path):
            skill_target_path = os.path.join(target_dir, skill_name)
            
            # Copy directory recursively
            if os.path.exists(skill_target_path):
                shutil.rmtree(skill_target_path)
            shutil.copytree(skill_src_path, skill_target_path)
            copied_count += 1
            
            # Run agent-adapt replacements on copied files recursively
            for root, dirs, files in os.walk(skill_target_path):
                for file in files:
                    filepath = os.path.join(root, file)
                    _, ext = os.path.splitext(file)
                    if ext.lower() in {".md", ".json", ".txt", ".py", ".js", ".ts"}:
                        try:
                            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                        except Exception as e:
                            continue
                        
                        original_content = content
                        for old, new in replacements:
                            content = content.replace(old, new)
                        
                        if content != original_content:
                            try:
                                with open(filepath, 'w', encoding='utf-8') as f:
                                    f.write(content)
                                modified_count += 1
                            except Exception as e:
                                print(f"Failed to write replacements in {filepath}: {e}")

print("=== ANTIGRAVITY GLOBAL SKILLS SETUP REPORT ===")
print(f"Total skills directories copied: {copied_count}")
print(f"Total files adapted to Antigravity: {modified_count}")
