import json
import sys
import os
import subprocess
import re

"""
ZORIXEL AIOS Component Registry CLI Script
Integrated into: /website-design-engine, /new-project, /jsmastery-architect, /grill-me, and /roast.
Purpose: Queries 300+ cataloged UI components across 11 libraries (Aceternity UI, Animate UI React, Magic UI, 21st.dev, Motion Primitives, React Bits, Origin UI, Kokonut UI, Uiverse, Forge UI, Vengence UI) for instant installation or adaptation.
"""

# Ensure UTF-8 output encoding for Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

INDEX_FILE = r"d:\AI-OS\premium-frontend-experience-system\source-registries\component-registry-index.json"
SITES_MATRIX_FILE = r"d:\AI-OS\references\23-sites-matrix.json"

def load_registry():
    if not os.path.exists(INDEX_FILE):
        print(f"Error: Registry file not found at {INDEX_FILE}")
        sys.exit(1)
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Merge 23-Site reference components if matrix exists
    if os.path.exists(SITES_MATRIX_FILE):
        try:
            with open(SITES_MATRIX_FILE, "r", encoding="utf-8") as sf:
                sites_data = json.load(sf)
                for site_name, site in sites_data.get("sites", {}).items():
                    for comp in site.get("components", []):
                        data["components"].append({
                            "name": comp["name"],
                            "library": f"23-Ref:{site_name}",
                            "category": comp.get("category", "reference"),
                            "pattern": comp.get("category", "reference"),
                            "url": comp["path"],
                            "cli_command": f"view_file {comp['path']}",
                            "is_favorite": True
                        })
        except Exception as e:
            pass

    return data

def list_favorites(data):
    print("\n--- FAVORITE COMPONENTS ---")
    favs = [c for c in data["components"] if c.get("is_favorite")]
    for idx, c in enumerate(favs, 1):
        cmd_or_url = c['cli_command'] if c['cli_command'] else c['url']
        pattern = f"[{c.get('pattern', 'bento')}]"
        print(f"{idx:2d}. [{c['library']}] {c['name']} {pattern} ({c['category']}) -> {cmd_or_url}")
    print(f"Total Favorites: {len(favs)}\n")

def search_components(data, query):
    query_lower = query.lower()
    matches = [c for c in data["components"] if query_lower in c['name'].lower() or query_lower in c['category'].lower() or query_lower in c['library'].lower() or query_lower in c.get('pattern', '').lower()]
    print(f"\n--- Search Results for '{query}' ({len(matches)} found) ---")
    for idx, c in enumerate(matches, 1):
        fav_mark = " [FAV]" if c.get("is_favorite") else ""
        cmd_or_url = c['cli_command'] if c['cli_command'] else c['url']
        pattern = f"[{c.get('pattern', 'bento')}]"
        print(f"{idx:2d}. [{c['library']}] {c['name']}{fav_mark} {pattern} [{c['category']}] -> {cmd_or_url}")
    print()

def search_pattern(data, pattern_query):
    query_lower = pattern_query.lower()
    matches = [c for c in data["components"] if query_lower == c.get('pattern', '').lower() or query_lower in c.get('pattern', '').lower()]
    print(f"\n--- UX Pattern Matches for '{pattern_query}' ({len(matches)} found) ---")
    for idx, c in enumerate(matches, 1):
        fav_mark = " [FAV]" if c.get("is_favorite") else ""
        cmd_or_url = c['cli_command'] if c['cli_command'] else c['url']
        print(f"{idx:2d}. [{c['library']}] {c['name']}{fav_mark} [{c['category']}] -> {cmd_or_url}")
    print()

def adapt_component(data, query):
    query_lower = query.lower()
    matches = [c for c in data["components"] if query_lower in c['name'].lower() or query_lower in c.get('cli_command', '').lower()]
    if not matches:
        print(f"\nNo component found matching '{query}'. Try running 'python component_registry_cli.py search {query}'.\n")
        return
    c = matches[0]
    print(f"\n========================================================")
    print(f"  COMPONENT AUTO-ADAPTER & CLI INSTALLER")
    print(f"========================================================")
    print(f"Component: {c['name']}")
    print(f"Library  : {c['library']}")
    print(f"Category : {c['category']}")
    print(f"UX Pattern: {c.get('pattern', 'bento')}")
    print(f"Doc URL  : {c.get('url', 'N/A')}")
    print(f"CLI CMD  : {c.get('cli_command', 'N/A')}")
    print(f"--------------------------------------------------------")
    print(f"Tailwind v4 Adaptations Required:")
    print(f" - Ensure @tailwindcss/vite or @tailwindcss/postcss is installed")
    print(f" - Add OKLCH color token definitions to index.css or globals.css")
    print(f" - Ensure lucide-react, framer-motion, and clsx / tailwind-merge are installed")
    print(f"--------------------------------------------------------")
    print(f"Installation Command:")
    print(f"  {c.get('cli_command', 'N/A')}")
    print(f"========================================================\n")

def main():
    data = load_registry()
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python component_registry_cli.py favs                    # List all favorite components")
        print("  python component_registry_cli.py search <query>           # Search components by name/category/library")
        print("  python component_registry_cli.py search-pattern <pattern> # Search by UX pattern (hero, pricing, navigation, bento, etc)")
        print("  python component_registry_cli.py adapt <component_name>  # Generate CLI command & adaptation guide")
        print("  python component_registry_cli.py stats                   # Show catalog stats")
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "favs":
        list_favorites(data)
    elif cmd == "search" and len(sys.argv) > 2:
        search_components(data, sys.argv[2])
    elif cmd == "search-pattern" and len(sys.argv) > 2:
        search_pattern(data, sys.argv[2])
    elif cmd == "adapt" and len(sys.argv) > 2:
        adapt_component(data, sys.argv[2])
    elif cmd == "stats":
        total = len(data["components"])
        favs = len([c for c in data["components"] if c.get("is_favorite")])
        print(f"\nMaster Component Registry Stats:")
        print(f"Total Components: {total}")
        print(f"Favorites: {favs}")
        print(f"Libraries: {', '.join(data['metadata']['libraries'])}\n")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

