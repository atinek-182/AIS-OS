import sys
import os
import asyncio
import urllib.parse
import re
from playwright.async_api import async_playwright

VIEWPORTS = [
    {"name": "desktop_1920", "width": 1920, "height": 1080},
    {"name": "laptop_1440", "width": 1440, "height": 900},
    {"name": "tablet_1024", "width": 1024, "height": 768},
    {"name": "tablet_768", "width": 768, "height": 1024},
    {"name": "mobile_375", "width": 375, "height": 812},
]

INIT_SHADER_HOOK_SCRIPT = """
window.__extractedShaders = [];
(function() {
    function hookGL(proto) {
        if (!proto) return;
        var origShaderSource = proto.shaderSource;
        proto.shaderSource = function(shader, source) {
            try {
                window.__extractedShaders.push({
                    type: this.getShaderParameter(shader, this.SHADER_TYPE) === this.VERTEX_SHADER ? 'vertex' : 'fragment',
                    source: source
                });
            } catch(e) {}
            return origShaderSource.apply(this, arguments);
        };
    }
    if (window.WebGLRenderingContext) hookGL(window.WebGLRenderingContext.prototype);
    if (window.WebGL2RenderingContext) hookGL(window.WebGL2RenderingContext.prototype);
})();
"""

def safe_path(base_folder, filename):
    clean_filename = os.path.basename(filename)
    clean_filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', clean_filename)
    if not clean_filename:
        clean_filename = "asset.bin"
    target = os.path.abspath(os.path.join(base_folder, clean_filename))
    base = os.path.abspath(base_folder)
    if not target.startswith(base):
        raise ValueError(f"Security Warning: Path traversal blocked for {filename}")
    return target

async def mirror_site(url, site_slug):
    # Sanitize site_slug to prevent directory traversal
    site_slug = re.sub(r'[^a-zA-Z0-9_\-]', '', site_slug)
    base_dir = os.path.join(r"d:\AI-OS\premium-frontend-experience-system\reference-inputs\sites", site_slug)
    mirror_dir = os.path.join(base_dir, "mirror")
    assets_dir = os.path.join(base_dir, "assets")
    code_dir = os.path.join(base_dir, "code-extracts")
    
    os.makedirs(mirror_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(os.path.join(code_dir, "components"), exist_ok=True)
    os.makedirs(os.path.join(code_dir, "animations"), exist_ok=True)
    os.makedirs(os.path.join(code_dir, "shaders"), exist_ok=True)
    os.makedirs(os.path.join(code_dir, "styles"), exist_ok=True)

    print(f"[MIRROR] Starting Upgraded Ultimate Mirror for {url} -> {site_slug}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # Inject WebGL GLSL Shader Interceptor
        await page.add_init_script(INIT_SHADER_HOOK_SCRIPT)

        # Intercept and save network responses with security validation
        async def handle_response(response):
            try:
                res_url = response.url
                status = response.status
                if status >= 400:
                    return
                parsed = urllib.parse.urlparse(res_url)
                
                # Block non-http/https schemes
                if parsed.scheme not in ["http", "https"]:
                    return
                    
                path = parsed.path
                if not path or path == "/":
                    filename = "index.html"
                else:
                    filename = os.path.basename(path)
                    if not filename or "." not in filename:
                        filename = path.strip("/").replace("/", "_") + ".html"
                
                mime = response.headers.get("content-type", "")
                buffer = await response.body()

                if "javascript" in mime or filename.endswith(".js"):
                    save_path = safe_path(os.path.join(mirror_dir, "js"), filename)
                elif "css" in mime or filename.endswith(".css"):
                    save_path = safe_path(os.path.join(mirror_dir, "css"), filename)
                elif any(ext in filename for ext in [".woff2", ".woff", ".ttf", ".otf"]):
                    save_path = safe_path(os.path.join(mirror_dir, "fonts"), filename)
                elif any(ext in filename for ext in [".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"]):
                    save_path = safe_path(os.path.join(assets_dir, "images"), filename)
                elif any(ext in filename for ext in [".mp4", ".webm", ".ogv"]):
                    save_path = safe_path(os.path.join(assets_dir, "videos"), filename)
                elif any(ext in filename for ext in [".glb", ".gltf", ".splat", ".ply", ".obj", ".buf", ".riv", ".wasm"]):
                    save_path = safe_path(os.path.join(assets_dir, "3d"), filename)
                elif filename.endswith(".html") or "html" in mime:
                    save_path = safe_path(mirror_dir, filename)
                else:
                    save_path = safe_path(os.path.join(mirror_dir, "misc"), filename)

                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, "wb") as f:
                    f.write(buffer)
            except Exception as e:
                pass

        page.on("response", handle_response)

        try:
            print(f"Loading {url}...")
            await page.goto(url, wait_until="domcontentloaded", timeout=45000)
            await asyncio.sleep(3)

            # Scroll to trigger lazy loaded assets, GSAP animations & shader initializations
            print("Scrolling page to trigger lazy assets, GLSL shaders & GSAP timelines...")
            for _ in range(10):
                await page.evaluate("window.scrollBy(0, 800)")
                await asyncio.sleep(0.5)
            await page.evaluate("window.scrollTo(0, 0)")
            await asyncio.sleep(1)

            # Save main page HTML
            html_content = await page.content()
            with open(os.path.join(mirror_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Saved full index.html ({len(html_content)} bytes)")

            # Extract inline CSS and scripts
            scripts = await page.eval_on_selector_all("script", "scripts => scripts.map(s => s.textContent)")
            full_inline_js = "\n\n// --- INLINE SCRIPT ---\n\n".join([s for s in scripts if s])
            with open(os.path.join(code_dir, "animations", "inline-scripts.js"), "w", encoding="utf-8") as f:
                f.write(full_inline_js)

            styles = await page.eval_on_selector_all("style", "styles => styles.map(s => s.textContent)")
            full_inline_css = "\n\n/* --- INLINE STYLE --- */\n\n".join([st for st in styles if st])
            with open(os.path.join(code_dir, "styles", "inline-styles.css"), "w", encoding="utf-8") as f:
                f.write(full_inline_css)

            # Extract GLSL Shaders from Runtime Interceptor Hook
            shaders = await page.evaluate("window.__extractedShaders || []")
            print(f"Intercepted {len(shaders)} GLSL shaders from browser runtime.")
            for idx, sh in enumerate(shaders, 1):
                stype = sh.get("type", "fragment")
                src = sh.get("source", "")
                if src:
                    sh_path = os.path.join(code_dir, "shaders", f"shader_{idx:02d}_{stype}.glsl")
                    with open(sh_path, "w", encoding="utf-8") as f:
                        f.write(f"// GLSL {stype.upper()} SHADER #{idx}\n// Target: {url}\n\n{src}")

            # Unbounded Component Extractor Logic
            print("Executing Unbounded Component Extractor for DOM elements...")
            dom_elements = await page.evaluate("""() => {
                const nodes = [];
                const selectors = ['nav', 'header', 'main', 'section', 'footer', 'aside', '.hero', '.bento', '.card', 'canvas'];
                selectors.forEach(sel => {
                    document.querySelectorAll(sel).forEach((el, idx) => {
                        nodes.push({
                            tag: el.tagName.toLowerCase(),
                            className: el.className || '',
                            id: el.id || '',
                            selector: sel,
                            html: el.outerHTML.slice(0, 1500),
                            text: (el.innerText || '').slice(0, 300)
                        });
                    });
                });
                return nodes;
            }""")
            
            print(f"Extracted {len(dom_elements)} structural DOM element candidates for React .tsx components.")

        except Exception as e:
            print(f"Page loading error: {e}")

        # Capture 5 Viewports
        print("Capturing 5 viewports...")
        for vp in VIEWPORTS:
            try:
                await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
                await asyncio.sleep(1)
                vp_path = os.path.join(assets_dir, f"{vp['name']}.png")
                await page.screenshot(path=vp_path)
                print(f"Saved viewport: {vp_path}")
            except Exception as e:
                print(f"Error capturing viewport {vp['name']}: {e}")

        await browser.close()
        print(f"[SUCCESS] Upgraded Ultimate Mirror Complete for {site_slug}!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scrape_full_site_mirror.py [URL] [SITE_SLUG]")
        sys.exit(1)
    target_url = sys.argv[1]
    slug = sys.argv[2]
    asyncio.run(mirror_site(target_url, slug))

