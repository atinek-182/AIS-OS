import json

INDEX_FILE = r"d:\AI-OS\premium-frontend-experience-system\source-registries\component-registry-index.json"

with open(INDEX_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

missing_url = 0
missing_cli = 0

for idx, c in enumerate(data["components"], 1):
    if not c.get("url"):
        missing_url += 1
        print(f"Missing URL [{c['library']}]: {c['name']}")
    if not c.get("cli_command"):
        missing_cli += 1
        print(f"Missing CLI [{c['library']}]: {c['name']}")

print(f"\nAudit Results for {len(data['components'])} components:")
print(f"  Missing URLs: {missing_url}")
print(f"  Missing CLI Commands: {missing_cli}")
