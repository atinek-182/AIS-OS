#!/usr/bin/env python3
"""
ZORIXEL AIOS Global Error Prevention Rules Synchronizer
Synchronizes living error rules between references/GLOBAL_ERROR_PREVENTION_RULES.md,
AGENTS.md, and GEMINI.md to ensure 100% inline presence in system prompts across all chat sessions.
"""

import os
import sys

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_RULES_PATH = os.path.join(WORKSPACE_ROOT, "references", "GLOBAL_ERROR_PREVENTION_RULES.md")
AGENTS_PATH = os.path.join(WORKSPACE_ROOT, "AGENTS.md")
GEMINI_PATH = os.path.join(WORKSPACE_ROOT, "GEMINI.md")

START_MARKER = "<!-- BEGIN INLINE GLOBAL ERROR PREVENTION RULES -->"
END_MARKER = "<!-- END INLINE GLOBAL ERROR PREVENTION RULES -->"

def load_rules_content():
    if not os.path.exists(REF_RULES_PATH):
        print(f"[ERROR] Global rules reference file not found: {REF_RULES_PATH}")
        sys.exit(1)
    with open(REF_RULES_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

def update_file_with_rules(target_path, rules_text):
    if not os.path.exists(target_path):
        print(f"[WARN] Target file not found: {target_path}. Skipping.")
        return False
        
    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    block = f"{START_MARKER}\n{rules_text}\n{END_MARKER}"
    
    if START_MARKER in content and END_MARKER in content:
        start_idx = content.find(START_MARKER)
        end_idx = content.find(END_MARKER) + len(END_MARKER)
        new_content = content[:start_idx] + block + content[end_idx:]
    else:
        new_content = content.rstrip() + "\n\n" + block + "\n"
        
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"[OK] Synchronized global rules into: {target_path}")
    return True

def sync_all():
    print("========================================================")
    print("ZORIXEL AIOS: Global Error Prevention Rules Synchronizer")
    print("========================================================\n")
    
    rules_text = load_rules_content()
    update_file_with_rules(AGENTS_PATH, rules_text)
    update_file_with_rules(GEMINI_PATH, rules_text)
    
    print("\n========================================================")
    print("GLOBAL RULES SYNCHRONIZATION COMPLETE!")
    print("========================================================\n")

if __name__ == "__main__":
    sync_all()
