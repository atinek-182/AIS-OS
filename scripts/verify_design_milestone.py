import os
import sys
import json
import datetime
import subprocess

# Force UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

root_dir = r"d:\AI-OS"
output_qa_dir = os.path.join(root_dir, "audits", "visual-qa")
os.makedirs(output_qa_dir, exist_ok=True)

VIEWPORTS = [
    {"name": "desktop", "width": 1920, "height": 1080},
    {"name": "laptop", "width": 1440, "height": 900},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "mobile", "width": 375, "height": 812},
    {"name": "fold", "width": 280, "height": 653},
]

def generate_node_playwright_script(target_url, run_dir):
    node_script_path = os.path.join(run_dir, "run_qa.js")
    
    js_code = f"""
const {{ chromium }} = require('playwright');
const fs = require('fs');
const path = require('path');

const viewports = {json.dumps(VIEWPORTS)};
const targetUrl = {json.dumps(target_url)};
const outputDir = {json.dumps(run_dir)};

(async () => {{
    const browser = await chromium.launch({{ headless: true }});
    const results = [];

    for (const vp of viewports) {{
        const page = await browser.newPage();
        await page.setViewportSize({{ width: vp.width, height: vp.height }});
        
        const consoleLogs = [];
        page.on('console', msg => consoleLogs.push(`[${{msg.type()}}] ${{msg.text()}}`));

        try {{
            await page.goto(targetUrl, {{ waitUntil: 'networkidle', timeout: 15000 }});
        }} catch (e) {{
            await page.goto(targetUrl, {{ waitUntil: 'load', timeout: 15000 }});
        }}

        // Check horizontal overflow
        const overflow = await page.evaluate(() => {{
            return document.documentElement.scrollWidth > window.innerWidth;
        }});

        const shotPath = path.join(outputDir, `shot_${{vp.name}}_${{vp.width}}x${{vp.height}}.png`);
        await page.screenshot({{ path: shotPath, fullPage: true }});

        results.push({{
            viewport: vp.name,
            width: vp.width,
            height: vp.height,
            screenshot: shotPath,
            hasHorizontalOverflow: overflow,
            consoleErrors: consoleLogs.filter(l => l.includes('error'))
        }});

        await page.close();
    }}

    await browser.close();
    fs.writeFileSync(path.join(outputDir, 'qa_summary.json'), JSON.stringify(results, null, 2));
    console.log('[OK] Visual QA sweep complete!');
}})();
"""
    with open(node_script_path, "w", encoding="utf-8") as f:
        f.write(js_code)
    return node_script_path

def run_visual_qa(target_file_or_url):
    print("==================================================")
    print(" ZORIXEL AIOS: UNIVERSAL 5-VIEWPORT VISUAL QA ")
    print("==================================================")

    if not target_file_or_url.startswith("http://") and not target_file_or_url.startswith("https://"):
        abs_p = os.path.abspath(target_file_or_url).replace("\\", "/")
        target_url = f"file:///{abs_p}"
    else:
        target_url = target_file_or_url

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(output_qa_dir, f"qa_run_{timestamp}")
    os.makedirs(run_dir, exist_ok=True)

    print(f"[STATUS] Target URL: {target_url}")
    print(f"[STATUS] QA Output Directory: {run_dir}")

    node_script = generate_node_playwright_script(target_url, run_dir)

    # Execute Node Playwright runner relative to project node_modules directory
    # per Rule: Playwright Execution Context Path
    pw_node_modules = os.path.join(root_dir, "projects", "font-showcase", "node_modules")
    env = os.environ.copy()
    env["NODE_PATH"] = pw_node_modules

    try:
        res = subprocess.run(
            ["node", node_script],
            cwd=os.path.dirname(node_script),
            env=env,
            capture_output=True,
            text=True,
            timeout=45,
            encoding="utf-8",
            errors="replace"
        )
        print(res.stdout)
        if res.returncode != 0 and res.stderr:
            print(f"[ERROR] Playwright stderr: {res.stderr}")

        summary_json_path = os.path.join(run_dir, "qa_summary.json")
        if os.path.exists(summary_json_path):
            with open(summary_json_path, "r", encoding="utf-8") as f:
                qa_data = json.load(f)

            print("\n--- 5-VIEWPORT VISUAL QA RESULTS ---")
            overflow_found = False
            for item in qa_data:
                status_tag = "[FAIL - OVERFLOW]" if item["hasHorizontalOverflow"] else "[PASS]"
                if item["hasHorizontalOverflow"]:
                    overflow_found = True
                print(f"  {status_tag} Viewport: {item['viewport']} ({item['width']}x{item['height']}) -> {os.path.basename(item['screenshot'])}")

            if overflow_found:
                print("\n[SELF-IMPROVING AUTO-FIX SUGGESTION]")
                print("Horizontal scroll overflow detected! Add the following CSS patch to root container:")
                print("`html, body { max-width: 100vw; overflow-x: hidden; }`")

            print(f"\n[SUCCESS] Visual QA artifacts saved to: {run_dir}")

    except Exception as e:
        print(f"[ERROR] Failed to run visual QA sweep: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root_dir, "projects", "Zorixel brand", "zorixel-website", "storm-reports", "zorixel-website-features-competitors-briefing.html")
    run_visual_qa(target)
