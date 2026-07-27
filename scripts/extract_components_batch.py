import os
import re
import json
import asyncio
import urllib.parse
from playwright.async_api import async_playwright

SITES_DIR = r"d:\AI-OS\premium-frontend-experience-system\reference-inputs\sites"

TARGET_SITES = [
    "ashley-brooke-cs",
    "champions-4-good",
    "detroit-paris",
    "follow-art",
    "gehry-getty",
    "good-fella",
    "grids-obys-agency",
    "jasmine-gunarto",
    "made-in-evolve",
    "off-menu-design",
    "oryzo-ai",
    "outfit-hello-hello",
    "sondaven",
    "the-line-studio",
    "the-shift-tokyo",
    "tresmares-capital",
    "truck-n-roll",
    "unleashing-best",
    "trionn-agency",
    "resn-corn-revolution",
    "active-theory"
]

DOM_EXTRACTOR_SCRIPT = """() => {
    const nodes = [];
    const selectorList = [
        'nav', 'header', 'footer', 'main', 'section', 'article', 'aside', 'form', 'dialog', 'canvas',
        '[class*="hero"]', '[class*="bento"]', '[class*="card"]', '[class*="nav"]', '[class*="header"]',
        '[class*="footer"]', '[class*="menu"]', '[class*="modal"]', '[class*="slider"]', '[class*="carousel"]',
        '[class*="accord"]', '[class*="scrolly"]', '[class*="grid"]', '[class*="stage"]', '[class*="wrapper"]',
        '[class*="container"]', '[class*="btn"]', '[class*="cta"]'
    ];
    const seenHtml = new Set();
    
    const elements = document.querySelectorAll(selectorList.join(', '));
    elements.forEach((el, idx) => {
        const rect = el.getBoundingClientRect();
        if (el.tagName.toLowerCase() !== 'canvas' && rect.width === 0 && rect.height === 0) return;
        
        const html = el.outerHTML;
        if (!html || html.length < 30 || seenHtml.has(html)) return;
        seenHtml.add(html);

        const tag = el.tagName.toLowerCase();
        const cls = typeof el.className === 'string' ? el.className : '';
        const id = el.id || '';
        const clsLower = cls.toLowerCase();
        const idLower = id.toLowerCase();

        let category = 'misc';
        if (tag === 'nav' || clsLower.includes('nav') || clsLower.includes('menu') || tag === 'header' || clsLower.includes('header')) {
            category = 'nav';
        } else if (clsLower.includes('hero') || idLower.includes('hero') || (tag === 'section' && idx === 0)) {
            category = 'hero';
        } else if (tag === 'footer' || clsLower.includes('footer')) {
            category = 'footers';
        } else if (clsLower.includes('card') || clsLower.includes('bento') || clsLower.includes('tile') || clsLower.includes('item')) {
            category = 'cards';
        } else if (clsLower.includes('scroll') || clsLower.includes('pin') || clsLower.includes('sticky') || clsLower.includes('scrolly')) {
            category = 'scrolly';
        } else if (tag === 'dialog' || clsLower.includes('modal') || clsLower.includes('popup') || clsLower.includes('overlay')) {
            category = 'modals';
        } else if (tag === 'canvas' || clsLower.includes('canvas') || clsLower.includes('webgl') || clsLower.includes('three') || clsLower.includes('stage')) {
            category = '3d';
        } else if (tag === 'section' || tag === 'article' || tag === 'main' || clsLower.includes('section')) {
            category = 'sections';
        } else if (tag === 'form' || tag === 'button' || clsLower.includes('btn') || clsLower.includes('cta') || clsLower.includes('slider') || clsLower.includes('accord')) {
            category = 'interactive';
        }

        nodes.push({
            idx: idx + 1,
            tag: tag,
            className: cls,
            id: id,
            category: category,
            html: html,
            text: (el.innerText || '').slice(0, 300).trim(),
            width: Math.round(rect.width),
            height: Math.round(rect.height)
        });
    });
    return nodes;
}"""

def html_to_jsx(html_str):
    jsx = html_str
    jsx = re.sub(r'\bclass=', 'className=', jsx)
    jsx = re.sub(r'\bfor=', 'htmlFor=', jsx)
    jsx = re.sub(r'\btabindex=', 'tabIndex=', jsx)
    jsx = re.sub(r'\bautocomplete=', 'autoComplete=', jsx)
    jsx = re.sub(r'\bsrcset=', 'srcSet=', jsx)
    jsx = re.sub(r'\bclip-path=', 'clipPath=', jsx)
    jsx = re.sub(r'\bstroke-width=', 'strokeWidth=', jsx)
    jsx = re.sub(r'\bstroke-linecap=', 'strokeLinecap=', jsx)
    jsx = re.sub(r'\bstroke-linejoin=', 'strokeLinejoin=', jsx)
    jsx = re.sub(r'\bfill-rule=', 'fillRule=', jsx)
    jsx = re.sub(r'<(img|input|br|hr|source|meta|link)([^>]*?)(?<!/)>', r'<\1\2 />', jsx)
    return jsx

async def process_site(site_slug, page):
    site_path = os.path.join(SITES_DIR, site_slug)
    mirror_dir = os.path.join(site_path, "mirror")
    code_dir = os.path.join(site_path, "code-extracts")

    # Find main HTML file
    candidates = [
        os.path.join(mirror_dir, "index.html"),
        os.path.join(mirror_dir, "en.html"),
        os.path.join(site_path, "index.html")
    ]
    target_html = None
    for cand in candidates:
        if os.path.exists(cand):
            target_html = cand
            break
            
    if not target_html:
        print(f"[SKIP] No HTML file found for site: {site_slug}")
        return 0, {}

    file_url = f"file:///{target_html.replace('\\', '/')}"
    print(f"\n[BATCH EXTRACT] Processing {site_slug} via {file_url}...")

    try:
        try:
            await page.goto(file_url, wait_until="domcontentloaded", timeout=15000)
        except Exception:
            # Fallback: Read file directly from disk if file:// goto times out
            with open(target_html, "r", encoding="utf-8", errors="ignore") as f:
                raw_html = f.read()
            await page.set_content(raw_html, wait_until="domcontentloaded")
            
        await asyncio.sleep(0.5)

        dom_elements = await page.evaluate(DOM_EXTRACTOR_SCRIPT)
        
        categories_count = {}
        index_metadata = []

        for elem in dom_elements:
            cat = elem["category"]
            cat_dir = os.path.join(code_dir, "components", cat)
            os.makedirs(cat_dir, exist_ok=True)
            
            categories_count[cat] = categories_count.get(cat, 0) + 1
            cat_idx = categories_count[cat]

            raw_name = elem["id"] or (elem["className"].split()[0] if elem["className"] else elem["tag"])
            clean_name = re.sub(r'[^a-zA-Z0-9]', '_', raw_name).strip('_')
            clean_name = ''.join(word.capitalize() for word in clean_name.split('_') if word)
            if not clean_name:
                clean_name = "Component"
            comp_name = f"{cat.capitalize()}_{clean_name}_{cat_idx:02d}"

            jsx_body = html_to_jsx(elem["html"])

            tsx_content = f"""import React from 'react';

/**
 * Component: {comp_name}
 * Target Site: {site_slug}
 * Category: {cat}
 * Tag: <{elem['tag']}> | ID: "{elem['id']}" | Class: "{elem['className']}"
 * Dimensions: {elem['width']}px x {elem['height']}px
 */
export const {comp_name}: React.FC = () => {{
  return (
    <div className="component-container-{cat}">
      {{/* --- Raw Extracted DOM Structure --- */}}
      {jsx_body}
    </div>
  );
}};

export default {comp_name};
"""
            file_path = os.path.join(cat_dir, f"{comp_name}.tsx")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(tsx_content)

            index_metadata.append({
                "name": comp_name,
                "category": cat,
                "file": os.path.join(cat, f"{comp_name}.tsx").replace("\\", "/"),
                "tag": elem["tag"],
                "id": elem["id"],
                "className": elem["className"],
                "width": elem["width"],
                "height": elem["height"]
            })

        index_path = os.path.join(code_dir, "components", "components-index.json")
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(index_metadata, f, indent=2)

        print(f"[SUCCESS] {site_slug}: Generated {len(index_metadata)} components across categories: {categories_count}")
        return len(index_metadata), categories_count

    except Exception as e:
        print(f"[ERROR] Failed extracting components for {site_slug}: {e}")
        return 0, {}

async def main():
    print(f"[BATCH START] Extracting components for {len(TARGET_SITES)} sites...")
    total_components = 0
    all_summaries = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        for site_slug in TARGET_SITES:
            count, cats = await process_site(site_slug, page)
            total_components += count
            all_summaries[site_slug] = {"total": count, "categories": cats}

        await browser.close()

    print("\n" + "="*70)
    print(f"[SUCCESS] BATCH COMPONENT EXTRACTION COMPLETE!")
    print(f"Total Components Extracted Across {len(TARGET_SITES)} Sites: {total_components}")
    print("="*70)
    for site, info in all_summaries.items():
        print(f"- {site:<25}: {info['total']:>4} components | {info['categories']}")

if __name__ == "__main__":
    asyncio.run(main())
