import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

local_skills_dir = r"d:\AI-OS\.agents\skills"
global_skills_dir = r"C:\Users\HP\.gemini\config\skills"

skills = {}

def scan_dir(base_dir, source):
    if not os.path.exists(base_dir):
        return
    for item in os.listdir(base_dir):
        skill_path = os.path.join(base_dir, item, "SKILL.md")
        if os.path.isfile(skill_path):
            desc = ""
            name = item
            try:
                with open(skill_path, "r", encoding="utf-8") as f:
                    content = f.read(1000)
                    m_name = re.search(r"^name:\s*(.+)$", content, re.MULTILINE)
                    m_desc = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
                    if m_name:
                        name = m_name.group(1).strip()
                    if m_desc:
                        desc = m_desc.group(1).strip()
            except Exception:
                pass
            skills[item] = {"name": name, "description": desc, "source": source}

scan_dir(local_skills_dir, "local")
scan_dir(global_skills_dir, "global")

print(f"Total skills found: {len(skills)}")
for k, v in sorted(skills.items()):
    print(f"- {k} ({v['source']}): {v['description'][:100]}")
