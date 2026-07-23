import os
import re

def minify_css(css):
    # Remove CSS comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove redundant whitespace
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([\{\};:,])\s*', r'\1', css)
    return css.strip()

def minify_js(js):
    # Remove single line comments
    js = re.sub(r'//.*?\n', '\n', js)
    # Remove multi-line comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    # Remove redundant spaces
    js = re.sub(r'\s+', ' ', js)
    return js.strip()

def main():
    base_dir = "./web-optimizer" if os.path.exists("./web-optimizer") else "."
    site_dir = os.path.join(base_dir, "target_site")
    
    html_path = os.path.join(site_dir, "index.html")
    css_path = os.path.join(site_dir, "styles.css")
    js_path = os.path.join(site_dir, "app.js")
    
    # Read files
    with open(html_path, "r") as f:
        html = f.read()
    with open(css_path, "r") as f:
        css = f.read()
    with open(js_path, "r") as f:
        js = f.read()
        
    # Apply minifications
    mini_css = minify_css(css)
    mini_js = minify_js(js)
    
    # Inline stylesheet and javascript file to eliminate separate network roundtrips
    html = re.sub(r'<link rel="stylesheet" href="styles.css">', f'<style>{mini_css}</style>', html)
    html = re.sub(r'<script src="app.js"></script>', f'<script>{mini_js}</script>', html)
    
    # Minify HTML spaces
    html = re.sub(r'\s+', ' ', html)
    html = re.sub(r'>\s+<', '><', html)
    
    # Save optimized result
    out_html = os.path.join(site_dir, "index.min.html")
    with open(out_html, "w") as f:
        f.write(html.strip())
        
    print("HTML/CSS/JS successfully minified and bundled to index.min.html")

if __name__ == "__main__":
    main()
