import urllib.request
import re
import json

def fetch_url(url):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Test Aceternity UI
acet_html = fetch_url("https://ui.aceternity.com/components")
acet_links = set(re.findall(r'href=["\'](/components/[a-zA-Z0-9\-]+)["\']', acet_html))
print(f"Found {len(acet_links)} Aceternity component links:")
for l in sorted(acet_links)[:15]:
    print(" ", l)

# Test Forge UI
forge_html = fetch_url("https://forgeui.in/components/")
forge_links = set(re.findall(r'href=["\'](/components/[a-zA-Z0-9\-]+)["\']', forge_html))
print(f"\nFound {len(forge_links)} Forge UI component links:")
for l in sorted(forge_links)[:15]:
    print(" ", l)

# Test Vengence UI
veng_html = fetch_url("https://www.vengenceui.com/components")
veng_r_json = set(re.findall(r'https?://[^\s"\'<>]+/r/[a-zA-Z0-9\-]+\.json', veng_html))
print(f"\nFound {len(veng_r_json)} Vengence UI CLI json links:")
for l in sorted(veng_r_json)[:15]:
    print(" ", l)

# Test Animate UI
anim_html = fetch_url("https://animate-ui.com/docs/components")
anim_links = set(re.findall(r'href=["\'](/docs/[a-zA-Z0-9\-/]+)["\']', anim_html))
print(f"\nFound {len(anim_links)} Animate UI doc links:")
for l in sorted(anim_links)[:15]:
    print(" ", l)
