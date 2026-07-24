import json
import sys
import os
import subprocess

# Ensure UTF-8 output encoding for Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

INDEX_FILE = r"d:\AI-OS\premium-frontend-experience-system\source-registries\component-registry-index.json"

def load_registry():
    if not os.path.exists(INDEX_FILE):
        print(f"Error: Registry file not found at {INDEX_FILE}")
        sys.exit(1)
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def list_favorites(data):
    print("\n--- FAVORITE COMPONENTS ---")
    favs = [c for c in data["components"] if c.get("is_favorite")]
    for idx, c in enumerate(favs, 1):
        cmd_or_url = c['cli_command'] if c['cli_command'] else c['url']
        print(f"{idx:2d}. [{c['library']}] {c['name']} ({c['category']}) -> {cmd_or_url}")
    print(f"Total Favorites: {len(favs)}\n")

def search_components(data, query):
    query_lower = query.lower()
    matches = [c for c in data["components"] if query_lower in c['name'].lower() or query_lower in c['category'].lower() or query_lower in c['library'].lower()]
    print(f"\n--- Search Results for '{query}' ({len(matches)} found) ---")
    for idx, c in enumerate(matches, 1):
        fav_mark = " [FAV]" if c.get("is_favorite") else ""
        cmd_or_url = c['cli_command'] if c['cli_command'] else c['url']
        print(f"{idx:2d}. [{c['library']}] {c['name']}{fav_mark} [{c['category']}] -> {cmd_or_url}")
    print()

def main():
    data = load_registry()
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python component_registry_cli.py favs          # List all favorite components")
        print("  python component_registry_cli.py search <query> # Search components by name/category/library")
        print("  python component_registry_cli.py stats         # Show catalog stats")
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "favs":
        list_favorites(data)
    elif cmd == "search" and len(sys.argv) > 2:
        search_components(data, sys.argv[2])
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
