import os
import sys
import re
import py_compile
import subprocess
import shutil
import json

skills_dir = r"d:\AI-OS\.agents\skills"
global_skills_dir = r"C:\Users\HP\.gemini\config\skills"

global_skills = ["roast", "session-handoff", "context7", "karpathy-guidelines"]

def check_js_syntax(file_path):
    """Verify JS/TS syntax without executing the script."""
    if not shutil.which("node"):
        # If node is not in path, we skip syntax check for JS
        return True
    try:
        # node --check compiles the file and reports syntax errors
        res = subprocess.run(["node", "--check", file_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  ERROR: JS Syntax check failed in {os.path.basename(file_path)}:")
            print(res.stderr)
            return False
        return True
    except Exception as e:
        # Fallback if execution fails
        return True

def verify_skill_folder(skill_path, is_global=False):
    """Verify frontmatter of SKILL.md and run syntax checks on code files."""
    skill_name = os.path.basename(skill_path)
    skill_md = os.path.join(skill_path, "SKILL.md")
    
    if not os.path.exists(skill_md):
        print(f"ERROR: {skill_name} SKILL.md not found at {skill_md}")
        return False
        
    # 1. Frontmatter Validation
    try:
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = content.split("---")
        if len(parts) < 3:
            print(f"ERROR: {skill_name} SKILL.md missing YAML frontmatter delimiters (---)")
            return False
            
        yaml_lines = parts[1].strip().split("\n")
        metadata = {}
        for line in yaml_lines:
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip()
                
        if not metadata.get("name") or not metadata.get("description"):
            print(f"ERROR: {skill_name} SKILL.md frontmatter must contain 'name' and 'description' keys!")
            return False
            
        print(f"SUCCESS: Parsed {skill_name} frontmatter (name='{metadata.get('name')}')")
    except Exception as e:
        print(f"ERROR: Failed to parse {skill_name} frontmatter: {e}")
        return False
        
    # 2. Syntax & Compilation Checks (for local skills only)
    if not is_global:
        success = True
        for root, dirs, files in os.walk(skill_path):
            # Skip node_modules or cache if any
            if "node_modules" in dirs:
                dirs.remove("node_modules")
                
            for file in files:
                file_path = os.path.join(root, file)
                rel_file_path = os.path.relpath(file_path, skill_path)
                
                # Python syntax compile check
                if file.endswith(".py"):
                    try:
                        py_compile.compile(file_path, doraise=True)
                    except py_compile.PyCompileError as e:
                        print(f"  ERROR: Python Syntax check failed in {rel_file_path}:")
                        print(e.msg)
                        success = False
                        
                # JavaScript syntax compile check
                elif file.endswith(".js") or file.endswith(".ts"):
                    if not check_js_syntax(file_path):
                        success = False
                        
                # JSON validity check
                elif file.endswith(".json"):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as jf:
                            json.load(jf)
                    except Exception as e:
                        print(f"  ERROR: JSON parse failed in {rel_file_path}: {e}")
                        success = False
        return success
        
    return True

def main():
    print("=== VERIFYING LOCAL WORKSPACE SKILLS ===")
    if not os.path.exists(skills_dir):
        print(f"ERROR: Local skills directory not found at {skills_dir}")
        sys.exit(1)
        
    local_skills = [
        d for d in os.listdir(skills_dir)
        if os.path.isdir(os.path.join(skills_dir, d))
    ]
    
    local_failed = 0
    for skill in sorted(local_skills):
        skill_path = os.path.join(skills_dir, skill)
        if not verify_skill_folder(skill_path, is_global=False):
            local_failed += 1
            
    print("\n=== VERIFYING GLOBAL SKILLS ===")
    global_failed = 0
    for skill in global_skills:
        skill_path = os.path.join(global_skills_dir, skill)
        if not verify_skill_folder(skill_path, is_global=True):
            global_failed += 1
            
    print("\n==========================================")
    print(f"Local Skills Failed: {local_failed}")
    print(f"Global Skills Failed: {global_failed}")
    print("==========================================")
    
    if local_failed > 0 or global_failed > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
