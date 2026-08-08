import os
import sys
import re
import json

# Enforce UTF-8 console output encoding on Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

root_dir = r"d:\AI-OS"

PRIMARY_VAULTS = [
    ("zorixel-brand-os", os.path.join(root_dir, "zorixel-brand-os")),
    ("second-brain-zorixel", os.path.join(root_dir, "second-brain-zorixel")),
    ("brain-aios", os.path.join(root_dir, "brain-aios")),
    ("context", os.path.join(root_dir, "context")),
    ("references", os.path.join(root_dir, "references")),
    ("decisions", os.path.join(root_dir, "decisions")),
    ("brainstorms", os.path.join(root_dir, "brainstorms")),
    ("projects", os.path.join(root_dir, "projects")),
]

EXCLUDE_DIRS = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", "graphify-out", 
    ".planning", ".next", ".out", "dist", "build", "coverage", ".cache", 
    ".turbo", ".obsidian/plugins", ".playwright-mcp"
}
EXCLUDE_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip", ".exe", 
    ".cmd", ".otf", ".ttf", ".woff", ".woff2", ".pyc", ".tar", ".gz", 
    ".ico", ".svg", ".mp4", ".mov", ".mp3", ".wav"
}

def search_graphify(query):
    graphify_results = []
    query_lower = query.lower()
    
    hub_paths = {
        "root": os.path.join(root_dir, "graphify-out", "graph.json"),
        "brain": os.path.join(root_dir, "brain-aios", "graphify-out", "graph.json"),
        "zorixel": os.path.join(root_dir, "second-brain-zorixel", "graphify-out", "graph.json"),
        "frontend": os.path.join(root_dir, "premium-frontend-experience-system", "graphify-out", "graph.json"),
    }
    
    for hub_name, gpath in hub_paths.items():
        if os.path.exists(gpath):
            try:
                with open(gpath, "r", encoding="utf-8", errors="ignore") as f:
                    data = json.load(f)
                nodes = data.get("nodes", [])
                for node in nodes:
                    lbl = node.get("label", "") or node.get("id", "")
                    rel_path = node.get("file", "") or lbl
                    if "zorixel-brand-os/second-brain-zorixel" in rel_path:
                        continue
                    if query_lower in lbl.lower() or query_lower in rel_path.lower():
                        graphify_results.append((hub_name, lbl, rel_path[:100]))
                        if len(graphify_results) >= 5:
                            break
            except Exception:
                pass
    return graphify_results

def scan_file_for_query(fpath, query_pattern, max_snippet_len=120):
    try:
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            for line_idx, line in enumerate(f, 1):
                if query_pattern.search(line):
                    clean_line = line.strip()
                    if len(clean_line) > max_snippet_len:
                        clean_line = clean_line[:max_snippet_len] + "..."
                    rel_p = os.path.relpath(fpath, root_dir).replace("\\", "/")
                    return {"file": rel_p, "line": line_idx, "snippet": clean_line}
    except Exception:
        pass
    return None

def deep_search(query, max_matches_per_vault=3):
    query_pattern = re.compile(re.escape(query), re.IGNORECASE)
    primary_results = {}
    searched_files = set()
    
    # 1. Primary Vaults Search
    for vname, vpath in PRIMARY_VAULTS:
        if not os.path.exists(vpath):
            continue
        
        matches = []
        for current_root, dirs, files in os.walk(vpath):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for fname in files:
                _, ext = os.path.splitext(fname)
                if ext.lower() in EXCLUDE_EXTS:
                    continue
                fpath = os.path.join(current_root, fname)
                searched_files.add(os.path.normpath(fpath))
                
                hit = scan_file_for_query(fpath, query_pattern)
                if hit:
                    matches.append(hit)
                    if len(matches) >= max_matches_per_vault:
                        break
            if len(matches) >= max_matches_per_vault:
                break
        if matches:
            primary_results[vname] = matches

    # 2. Universal Workspace Exhaustive Sweep (Scratch, Archives, Audits, Trials, Misc, Root Files)
    exhaustive_results = []
    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fname in files:
            _, ext = os.path.splitext(fname)
            if ext.lower() in EXCLUDE_EXTS:
                continue
            fpath = os.path.join(current_root, fname)
            norm_p = os.path.normpath(fpath)
            if norm_p in searched_files:
                continue
            
            # Avoid recursive junction loops
            rel_p = os.path.relpath(fpath, root_dir).replace("\\", "/")
            if rel_p.count("zorixel-brand-os") > 1 or rel_p.count("second-brain-zorixel") > 1:
                continue
                
            hit = scan_file_for_query(fpath, query_pattern)
            if hit:
                exhaustive_results.append(hit)
                if len(exhaustive_results) >= 8:
                    break
        if len(exhaustive_results) >= 8:
            break

    return primary_results, exhaustive_results

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/aios_deep_search.py <query>")
        sys.exit(1)
        
    query = " ".join(sys.argv[1:])
    print(f"=== AIOS UNIVERSAL DEEP SEARCH SUMMARY FOR: '{query}' ===")
    
    # 1. Graphify AST lookup
    ast_matches = search_graphify(query)
    if ast_matches:
        print("\n--- GRAPHIFY AST NODES & CLUSTERS ---")
        for hub, lbl, fpath in ast_matches:
            print(f"- [{hub.upper()}] Node: {lbl} | Path: {fpath}")
            
    # 2. Primary Vault & Universal Exhaustive Search
    primary_results, exhaustive_results = deep_search(query)
    
    if not primary_results and not exhaustive_results and not ast_matches:
        print(f"\n[INFO] No direct text matches found for '{query}' anywhere in AIOS.")
        print("Tip: Check spelling or try broader keywords.")
        return

    total_found = 0
    if primary_results:
        print("\n--- PRIMARY VAULTS MATCHES ---")
        for vname, items in primary_results.items():
            print(f"\nVault: {vname.upper()} ({len(items)} hits)")
            for item in items:
                total_found += 1
                print(f"  - [{item['file']}#L{item['line']}] : {item['snippet']}")

    if exhaustive_results:
        print("\n--- EXHAUSTIVE SWEEP (OBSCURE / SCRATCH / ARCHIVES / MISC) ---")
        print("Found matching notes in secondary or non-standard locations:")
        for item in exhaustive_results:
            total_found += 1
            print(f"  - [SECONDARY: {item['file']}#L{item['line']}] : {item['snippet']}")
            
    print(f"\nTotal Key References Found: {total_found} (Compressed under ~500 tokens)")

if __name__ == "__main__":
    main()
