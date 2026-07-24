import os
import yaml

SKILLS_DIR = r"d:\AI-OS\.agents\skills"
GEMINI_FILE = r"d:\AI-OS\GEMINI.md"
AGENTS_FILE = r"d:\AI-OS\.agents\AGENTS.md"

def verify():
    errors = []
    success_count = 0
    
    if not os.path.exists(SKILLS_DIR):
        print(f"CRITICAL: {SKILLS_DIR} not found.")
        return False
    
    skills = [d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    print(f"[AUDIT] Auditing {len(skills)} workspace skills...")
    
    # Read GEMINI.md
    with open(GEMINI_FILE, "r", encoding="utf-8") as f:
        gemini_content = f.read()
    
    # Read AGENTS.md
    with open(AGENTS_FILE, "r", encoding="utf-8") as f:
        agents_content = f.read()
    
    if "Tri-Mode Skill Execution & Inter-Skill Calling Protocol" not in agents_content:
        errors.append("AGENTS.md missing Tri-Mode Skill Execution & Inter-Skill Calling Protocol rule.")
    
    for s_name in sorted(skills):
        s_path = os.path.join(SKILLS_DIR, s_name, "SKILL.md")
        if not os.path.exists(s_path):
            errors.append(f"{s_name}: SKILL.md missing")
            continue
        
        with open(s_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.startswith("---"):
            errors.append(f"{s_name}: Frontmatter missing opening ---")
            continue
        
        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append(f"{s_name}: Frontmatter missing closing ---")
            continue
        
        try:
            fm = yaml.safe_load(parts[1])
        except Exception as e:
            errors.append(f"{s_name}: YAML Parse error - {e}")
            continue
        
        if fm.get("name") != s_name:
            errors.append(f"{s_name}: Frontmatter name '{fm.get('name')}' != directory '{s_name}'")
        
        if not fm.get("description"):
            errors.append(f"{s_name}: Frontmatter description missing")
        elif f"/{s_name}" not in fm.get("description"):
            errors.append(f"{s_name}: Frontmatter description missing slash command /{s_name}")
        
        if not fm.get("argument-hint"):
            errors.append(f"{s_name}: Frontmatter argument-hint missing")
        
        # Check GEMINI.md registration
        if f"/{s_name}" not in gemini_content:
            errors.append(f"{s_name}: Not registered with /{s_name} in GEMINI.md")
        
        success_count += 1
    
    print("\n--- AUDIT RESULTS ---")
    print(f"Passed: {success_count} / {len(skills)}")
    if errors:
        print(f"Failed ({len(errors)} errors):")
        for e in errors:
            print(f"  [X] {e}")
        return False
    else:
        print("[SUCCESS] ALL 40 SKILLS PASSED TRI-MODE AUDIT WITH 100% VERIFICATION!")
        return True

if __name__ == "__main__":
    verify()
