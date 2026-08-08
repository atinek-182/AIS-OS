import os
import glob
import re

root_dir = r"d:\AI-OS"

def check_path_exists(path_str):
    clean = path_str.replace("file:///", "").replace("/", "\\").strip()
    return os.path.exists(clean)

print("=== CHECK 1 & CHECK 4: ALWAYS-LOADED FILES & ROUTING INTEGRITY ===")
always_loaded = ["AGENTS.md", "GEMINI.md"]
for fname in always_loaded:
    fpath = os.path.join(root_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        lines = len(content.splitlines())
        words = len(content.split())
        bytes_cnt = len(content.encode("utf-8"))
        print(f"File: {fname} | Lines: {lines} | Words: {words} | Bytes: {bytes_cnt}")

print("\n=== CHECKING TOP LEVEL DIRECTORIES vs WORKSPACE_MAP.md ===")
top_dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
print(f"Top level directories ({len(top_dirs)}): {top_dirs}")

print("\n=== SEARCHING FOR KNOWLEDGE MAPS / SYSTEM PROMPT ROUTING ===")
# Let's check MEMORY.md, hot.md, WORKSPACE_MAP.md
for doc in ["MEMORY.md", "hot.md", "WORKSPACE_MAP.md", "decisions/log.md"]:
    p = os.path.join(root_dir, doc)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        print(f"{doc}: {len(content.splitlines())} lines | {len(content.split())} words")
    else:
        print(f"{doc}: MISSING!")
