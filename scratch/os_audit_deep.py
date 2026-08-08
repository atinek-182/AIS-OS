import os
import glob
import json

root_dir = r"d:\AI-OS"

def run_deep_audit():
    findings = []
    
    # 1. Truncation check
    gemini_path = os.path.join(root_dir, "GEMINI.md")
    agents_path = os.path.join(root_dir, "AGENTS.md")
    
    with open(gemini_path, "r", encoding="utf-8") as f:
        gem_lines = f.readlines()
    
    with open(agents_path, "r", encoding="utf-8") as f:
        ag_lines = f.readlines()
        
    print(f"GEMINI.md total lines: {len(gem_lines)}")
    print(f"AGENTS.md total lines: {len(ag_lines)}")
    
    # Check if files in GEMINI.md exist
    missing_paths = []
    path_pattern = re.compile(r'\[.*?\]\((file:///[^\)]+)\)')
    for idx, line in enumerate(gem_lines):
        matches = path_pattern.findall(line)
        for m in matches:
            clean_p = m.replace("file:///", "").replace("/", "\\")
            if not os.path.exists(clean_p):
                missing_paths.append((idx+1, clean_p))
                
    print(f"\nMissing paths in GEMINI.md: {len(missing_paths)}")
    for line_no, p in missing_paths[:10]:
        print(f"  Line {line_no}: {p}")
        
    # Check skills count and validity
    skills_dir = os.path.join(root_dir, ".agents", "skills")
    skill_folders = [f for f in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, f))]
    valid_skills = 0
    invalid_skills = []
    for sf in skill_folders:
        skill_md = os.path.join(skills_dir, sf, "SKILL.md")
        if os.path.exists(skill_md):
            valid_skills += 1
        else:
            invalid_skills.append(sf)
            
    print(f"\nTotal Skills in .agents/skills: {len(skill_folders)}")
    print(f"Valid (contains SKILL.md): {valid_skills}")
    print(f"Invalid skills missing SKILL.md: {invalid_skills}")
    
    # Check unmapped top-level directories in AGENTS.md / GEMINI.md
    top_dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and not d.startswith('.')]
    print(f"\nTop level directories: {top_dirs}")
    
    # Check key knowledge stores
    k_stores = {
        "brain-aios": os.path.exists(os.path.join(root_dir, "brain-aios")),
        "second-brain-zorixel": os.path.exists(os.path.join(root_dir, "second-brain-zorixel")),
        "zorixel-brand-os": os.path.exists(os.path.join(root_dir, "zorixel-brand-os")),
        "context": os.path.exists(os.path.join(root_dir, "context")),
        "references": os.path.exists(os.path.join(root_dir, "references")),
        "MEMORY.md": os.path.exists(os.path.join(root_dir, "MEMORY.md")),
        "WORKSPACE_MAP.md": os.path.exists(os.path.join(root_dir, "WORKSPACE_MAP.md")),
        "decisions/log.md": os.path.exists(os.path.join(root_dir, "decisions", "log.md"))
    }
    print(f"\nKnowledge stores present: {json.dumps(k_stores, indent=2)}")

import re
run_deep_audit()
