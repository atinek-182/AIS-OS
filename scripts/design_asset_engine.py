#!/usr/bin/env python3
"""
AI OS Design & Asset Engine CLI
Query references, asset prompts, component specs, and render dynamic project briefs.
"""

import sys
import json
import argparse
import os

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DB_PATH = r"d:\AI-OS\premium-frontend-experience-system\source-registries\MASTER_REFERENCE_DATABASE.json"
COMPONENT_INDEX_PATH = r"d:\AI-OS\premium-frontend-experience-system\source-registries\component-registry-index.json"

def load_db():
    if not os.path.exists(DB_PATH):
        print(f"Error: Master reference database not found at {DB_PATH}")
        sys.exit(1)
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_component_index():
    if not os.path.exists(COMPONENT_INDEX_PATH):
        return []
    with open(COMPONENT_INDEX_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("components", [])

def search_references(query):
    db = load_db()
    query_lower = query.lower()
    matches = []
    for ref in db.get("all_unique_references", []):
        if query_lower in ref.get("title", "").lower() or query_lower in ref.get("url", "").lower() or query_lower in ref.get("source_file", "").lower():
            matches.append(ref)
    
    print(f"\n--- Reference Search Results for '{query}' ({len(matches)} found) ---")
    for idx, item in enumerate(matches[:20], 1):
        print(f" {idx:2d}. [{item['title']}] -> {item['url']} (Source: {item['source_file']})")
    if len(matches) > 20:
        print(f" ... and {len(matches) - 20} more matches.")
    print()

def get_asset_prompts(prompt_type):
    db = load_db()
    prompts = db.get("asset_prompts", {})
    ptype = prompt_type.lower()
    
    if ptype not in prompts:
        print(f"Unknown prompt type '{prompt_type}'. Available types: {list(prompts.keys())}")
        return
        
    print(f"\n--- Asset Prompts ({ptype.upper()}) ---")
    for idx, item in enumerate(prompts[ptype], 1):
        print(f" {idx}. Name: {item.get('name')}")
        print(f"    Type: {item.get('type')}")
        print(f"    Purpose: {item.get('purpose')}")
        print(f"    Prompt: {item.get('prompt')}")
        if "code_snippet" in item:
            print(f"    Snippet: {item.get('code_snippet')}")
        print()

def render_brief(brief_type):
    db = load_db()
    tokens = db.get("design_math_tokens", {})
    btype = brief_type.lower()
    
    print(f"\n=======================================================")
    print(f"  AI OS DYNAMIC DESIGN BRIEF: {btype.upper()}")
    print(f"=======================================================")
    print(f"System Standard: AI OS Premium Frontend Engine v2.0")
    print(f"Easing Tokens:")
    for k, v in tokens.get("easing_curves", {}).items():
        print(f"  - {k}: {v}")
    print(f"Typography Scale (Ratio: {tokens.get('typography_scales', {}).get('ratio')}):")
    for k, v in tokens.get("typography_scales", {}).items():
        if k != "ratio":
            print(f"  - {k}: {v}")
    print(f"5-Viewport Target Suite:")
    for vp in tokens.get("viewports", []):
        print(f"  - {vp['name']}: {vp['width']}px")
    print(f"=======================================================\n")

def list_sources():
    db = load_db()
    sources = db.get("approved_sources", {})
    print("\n--- Approved UI & Asset Sources ---")
    print("UI Libraries:")
    for lib in sources.get("ui_libraries", []):
        print(f"  - {lib['name']} ({lib['count']} components) -> {lib['cli']}")
    print("\nAnimation Libraries:")
    for anim in sources.get("animation_libraries", []):
        print(f"  - {anim}")
    print("\nShader Sources:")
    for sh in sources.get("shader_sources", []):
        print(f"  - {sh}")
    print("\nDesign Inspiration:")
    for insp in sources.get("design_inspiration", []):
        print(f"  - {insp}")
    print()

def main():
    parser = argparse.ArgumentParser(description="AI OS Design & Asset Engine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    search_parser = subparsers.add_parser("search-ref", help="Search master web references")
    search_parser.add_argument("query", help="Search keyword (e.g. shader, bento, godly, sondaven)")

    prompt_parser = subparsers.add_parser("prompt", help="Get asset prompts")
    prompt_parser.add_argument("type", help="Asset type (shaders, videos, svgs, textures)")

    brief_parser = subparsers.add_parser("brief", help="Render dynamic design brief")
    brief_parser.add_argument("type", help="Brief type (hero, color, layout, typography, landing)")

    sources_parser = subparsers.add_parser("sources", help="List approved sources and registries")

    args = parser.parse_args()

    if args.command == "search-ref":
        search_references(args.query)
    elif args.command == "prompt":
        get_asset_prompts(args.type)
    elif args.command == "brief":
        render_brief(args.type)
    elif args.command == "sources":
        list_sources()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
