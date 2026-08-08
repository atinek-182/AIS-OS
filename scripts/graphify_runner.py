#!/usr/bin/env python3
"""
AIOS Multi-Vault Graphify Automation Engine
Manages tree-sitter AST knowledge graphs across AIOS root, brain-aios, second-brain-zorixel, and premium-frontend-experience-system.
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

# Enforce UTF-8 console output encoding on Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


# Hub directory registry
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

HUBS = {
    "root": WORKSPACE_ROOT,
    "brain": WORKSPACE_ROOT / "brain-aios",
    "zorixel": WORKSPACE_ROOT / "second-brain-zorixel",
    "frontend": WORKSPACE_ROOT / "premium-frontend-experience-system"
}

def run_command(cmd, cwd=None):
    """Executes a command and returns exit code, stdout, stderr."""
    process = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, encoding='utf-8', errors='replace')
    stdout = process.stdout.strip() if process.stdout else ""
    stderr = process.stderr.strip() if process.stderr else ""
    return process.returncode, stdout, stderr

def build_graph(target_hub="all"):
    """Builds or updates knowledge graph for target hub(s)."""
    targets = HUBS.keys() if target_hub == "all" else [target_hub]
    
    results = {}
    for hub in targets:
        if hub not in HUBS:
            print(f"[ERROR] Unknown hub '{hub}'. Available hubs: {list(HUBS.keys())}")
            continue
            
        hub_path = HUBS[hub]
        if not hub_path.exists():
            print(f"[WARN] Path '{hub_path}' does not exist. Skipping.")
            continue
            
        print(f"\n[GRAPHIFY] Building knowledge graph for [{hub.upper()}] at {hub_path}...")
        code, out, err = run_command(f"graphify update .", cwd=str(hub_path))
        if code == 0:
            print(f"[SUCCESS] [{hub.upper()}] Knowledge graph updated successfully!")
            results[hub] = "SUCCESS"
        else:
            print(f"[FAILURE] [{hub.upper()}] Build failed: {err or out}")
            results[hub] = f"FAILED: {err or out}"
            
    return results

def query_graph(term, target_hub="root"):
    """Queries knowledge graph for specific term."""
    hub_path = HUBS.get(target_hub, WORKSPACE_ROOT)
    print(f"\n[GRAPHIFY QUERY] Hub: [{target_hub.upper()}] | Term: '{term}'")
    code, out, err = run_command(f'graphify query "{term}"', cwd=str(hub_path))
    if code == 0:
        print(out)
    else:
        print(f"[ERROR] Query failed: {err or out}")

def explain_concept(concept, target_hub="root"):
    """Explains concept connections and degree."""
    hub_path = HUBS.get(target_hub, WORKSPACE_ROOT)
    print(f"\n[GRAPHIFY EXPLAIN] Hub: [{target_hub.upper()}] | Concept: '{concept}'")
    code, out, err = run_command(f'graphify explain "{concept}"', cwd=str(hub_path))
    if code == 0:
        print(out)
    else:
        print(f"[ERROR] Explain failed: {err or out}")

def path_between(node_a, node_b, target_hub="root"):
    """Traces shortest path connection between node_a and node_b."""
    hub_path = HUBS.get(target_hub, WORKSPACE_ROOT)
    print(f"\n[GRAPHIFY PATH] Hub: [{target_hub.upper()}] | Path: '{node_a}' -> '{node_b}'")
    code, out, err = run_command(f'graphify path "{node_a}" "{node_b}"', cwd=str(hub_path))
    if code == 0:
        print(out)
    else:
        print(f"[ERROR] Path trace failed: {err or out}")

def check_status():
    """Checks knowledge graph status and freshness across all hubs."""
    print("==========================================================================")
    print("       AIOS MULTI-VAULT KNOWLEDGE GRAPH STATUS REPORT (GRAPHIFY)          ")
    print("==========================================================================")
    
    for hub, path in HUBS.items():
        out_dir = path / "graphify-out"
        graph_json = out_dir / "graph.json"
        
        status_str = "FRESH" if graph_json.exists() else "NOT BUILT"
        file_size = f"{graph_json.stat().st_size / 1024:.1f} KB" if graph_json.exists() else "N/A"
        
        print(f"Hub: [{hub.ljust(8)}] | Status: {status_str.ljust(10)} | Size: {file_size.ljust(10)} | Path: {out_dir}")

def main():
    parser = argparse.ArgumentParser(description="AIOS Multi-Vault Graphify Automation Engine")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # build
    build_parser = subparsers.add_parser("build", help="Build or update graph for target hub")
    build_parser.add_argument("hub", nargs="?", default="all", choices=["all", "root", "brain", "zorixel", "frontend"])
    
    # query
    query_parser = subparsers.add_parser("query", help="Query graph for a term")
    query_parser.add_argument("term", help="Search term or question")
    query_parser.add_argument("--hub", default="root", choices=["root", "brain", "zorixel", "frontend"])
    
    # explain
    explain_parser = subparsers.add_parser("explain", help="Explain concept relationships")
    explain_parser.add_argument("concept", help="Concept name")
    explain_parser.add_argument("--hub", default="root", choices=["root", "brain", "zorixel", "frontend"])
    
    # path
    path_parser = subparsers.add_parser("path", help="Trace shortest path between two nodes")
    path_parser.add_argument("node_a", help="First node")
    path_parser.add_argument("node_b", help="Second node")
    path_parser.add_argument("--hub", default="root", choices=["root", "brain", "zorixel", "frontend"])
    
    # status
    subparsers.add_parser("status", help="Check status across all hubs")
    
    args = parser.parse_args()
    
    if args.command == "build":
        build_graph(args.hub)
    elif args.command == "query":
        query_graph(args.term, args.hub)
    elif args.command == "explain":
        explain_concept(args.concept, args.hub)
    elif args.command == "path":
        path_between(args.node_a, args.node_b, args.hub)
    elif args.command == "status":
        check_status()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
