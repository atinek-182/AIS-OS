import os

skills_dir = r"d:\AI-OS\.agents\skills"
new_skills = ["plan-day", "review-day", "scrape-competitor", "draft-message", "file-search", "agent-adapt", "grill-me"]

print("=== VERIFYING NEW SKILLS ===")
for skill in new_skills:
    skill_path = os.path.join(skills_dir, skill, "SKILL.md")
    if not os.path.exists(skill_path):
        print(f"ERROR: {skill} SKILL.md not found at {skill_path}")
        continue
    
    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parts = content.split("---")
        if len(parts) >= 3:
            yaml_lines = parts[1].strip().split("\n")
            metadata = {}
            for line in yaml_lines:
                if ":" in line:
                    key, val = line.split(":", 1)
                    metadata[key.strip()] = val.strip()
            print(f"SUCCESS: Parsed {skill}:")
            print(f"  * Name: {metadata.get('name')}")
            print(f"  * Description: {metadata.get('description')}")
            if metadata.get('argument-hint'):
                print(f"  * Argument Hint: {metadata.get('argument-hint')}")
        else:
            print(f"ERROR: {skill} SKILL.md missing frontmatter delimiters")
            
    except Exception as e:
        print(f"ERROR: Failed to parse {skill}: {e}")
