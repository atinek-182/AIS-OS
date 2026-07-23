#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import threading
import http.server
import socketserver

def start_static_server(directory, port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)
        def log_message(self, format, *args):
            pass # Suppress logging noise

    server = socketserver.TCPServer(("", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server

def run_build(project_dir):
    print(">>> Running npm run build...")
    # Check if package.json exists
    if not os.path.exists(os.path.join(project_dir, 'package.json')):
        print("Error: No package.json found in the target directory.")
        return False
    
    # Run npm run build
    result = subprocess.run('npm run build', shell=True, cwd=project_dir, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error: Build failed!")
        print(result.stderr)
        return False
    print(">>> Build successful!")
    return True

def detect_build_dir(project_dir):
    candidates = ['dist', 'build', 'out', '.next/server/pages', 'public']
    for candidate in candidates:
        full_path = os.path.join(project_dir, candidate)
        if os.path.exists(full_path) and os.path.isdir(full_path):
            return full_path
    return project_dir

def execute_playwright_audit(project_dir, port):
    qa_dir = os.path.join(project_dir, 'qa')
    os.makedirs(qa_dir, exist_ok=True)
    
    temp_js_path = os.path.join(project_dir, 'temp_audit.js')
    
    js_content = f"""
const {{ chromium }} = require('playwright');
const path = require('path');

(async () => {{
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  const consoleErrors = [];
  page.on('console', msg => {{
    if (msg.type() === 'error') {{
      consoleErrors.push(msg.text());
    }}
  }});
  
  page.on('pageerror', err => {{
    consoleErrors.push(err.message);
  }});

  console.log('>>> Auditing http://localhost:{port} ...');
  try {{
    await page.goto('http://localhost:{port}', {{ waitUntil: 'networkidle' }});
  }} catch (e) {{
    console.error('Failed to load page:', e.message);
    await browser.close();
    process.exit(1);
  }}

  const viewports = [
    {{ name: 'mobile_small', width: 360, height: 640 }},
    {{ name: 'mobile_large', width: 390, height: 844 }},
    {{ name: 'tablet', width: 768, height: 1024 }},
    {{ name: 'laptop', width: 1024, height: 768 }},
    {{ name: 'desktop', width: 1440, height: 900 }}
  ];

  for (const vp of viewports) {{
    await page.setViewportSize({{ width: vp.width, height: vp.height }});
    // Wait briefly for layout adjustment/animation
    await page.waitForTimeout(500);
    const imgPath = path.join('{qa_dir.replace('\\\\', '/')}', `screenshot_${{vp.name}}.png`);
    await page.screenshot({{ path: imgPath, fullPage: true }});
    console.log(`Saved screenshot: ${vp.name} (${vp.width}x${vp.height}) -> ${{imgPath}}`);
  }}

  await browser.close();
  
  if (consoleErrors.length > 0) {{
    console.log('--- CONSOLE ERRORS FOUND ---');
    consoleErrors.forEach(err => console.log('ERROR:', err));
    process.exit(2);
  }} else {{
    console.log('>>> [GStack QA Audit] Visual QA complete: 0 console errors found across all 5 viewports.');
    process.exit(0);
  }}
}})().catch(err => {{
  console.error('Fatal error during Playwright execution:', err);
  process.exit(1);
}});
"""
    
    with open(temp_js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    try:
        # Run node temp_audit.js using npx playwright to ensure dependencies are loaded
        result = subprocess.run('node temp_audit.js', shell=True, cwd=project_dir, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode
    finally:
        if os.path.exists(temp_js_path):
            os.remove(temp_js_path)

def main():
    project_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    project_dir = os.path.abspath(project_dir)
    
    print(f"Starting visual and console QA audit in: {project_dir}")
    
    if not run_build(project_dir):
        sys.exit(1)
        
    build_dir = detect_build_dir(project_dir)
    print(f"Serving build folder: {build_dir}")
    
    port = 9099
    server = start_static_server(build_dir, port)
    
    try:
        exit_code = execute_playwright_audit(project_dir, port)
        if exit_code == 0:
            print(">>> SUCCESS: Milestone visual QA verification passed successfully.")
        elif exit_code == 2:
            print(">>> WARNING: Audits complete, but console errors were detected. Clean up console output.")
            sys.exit(2)
        else:
            print(">>> ERROR: Audit failed during Playwright run.")
            sys.exit(1)
    finally:
        print(">>> Shutting down static server...")
        server.shutdown()

if __name__ == '__main__':
    main()
