import os
import re

def parse_simple_yaml(text):
    """
    A simple custom YAML-like parser for carousel specs to avoid PyYAML dependency.
    Supports key-value pairs, simple lists (e.g. PreviewCards), and multi-line strings (e.g. Code).
    """
    properties = {}
    lines = text.strip().split('\n')
    
    current_key = None
    multiline_accum = []
    in_multiline = False
    
    # Nested object tracking (e.g. BeforeCard, AfterCard)
    current_nested_key = None
    nested_obj = {}
    
    # List tracking (e.g. PreviewCards)
    current_list_key = None
    list_items = []

    for line in lines:
        if not line.strip():
            continue
            
        # Check for indent
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        # Handle multiline accumulation
        if in_multiline:
            if indent > 0:
                multiline_accum.append(line[indent:])
                continue
            else:
                properties[current_key] = '\n'.join(multiline_accum)
                in_multiline = False
                multiline_accum = []

        # Handle list item
        if stripped.startswith('-'):
            list_val = stripped[1:].strip()
            # Handle list item with sub-key e.g., "- Text: Value"
            if list_val.startswith('Text:'):
                list_val = list_val[5:].strip()
            list_items.append({'Text': list_val})
            continue
        else:
            # If we transitioned away from a list, store it
            if current_list_key and list_items:
                properties[current_list_key] = list_items
                current_list_key = None
                list_items = []

        # Key-Value match
        match = re.match(r'^([\w\d_]+)\s*:\s*(.*)$', stripped)
        if match:
            key, val = match.groups()
            
            # Reset nested object if we are at root level (indent == 0)
            if indent == 0 and current_nested_key:
                properties[current_nested_key] = nested_obj
                current_nested_key = None
                nested_obj = {}

            if val == '|':
                current_key = key
                in_multiline = True
                multiline_accum = []
            elif indent > 0 and current_nested_key is not None:
                # Inside a nested key
                nested_obj[key] = val
            elif val == '':
                # Might be a list or a nested object starting
                if key == 'PreviewCards':
                    current_list_key = key
                    list_items = []
                else:
                    current_nested_key = key
                    nested_obj = {}
            else:
                properties[key] = val

    # Final sweep
    if in_multiline and current_key:
        properties[current_key] = '\n'.join(multiline_accum)
    if current_nested_key and nested_obj:
        properties[current_nested_key] = nested_obj
    if current_list_key and list_items:
        properties[current_list_key] = list_items

    return properties

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get general style
    style_match = re.search(r'^Style:\s*(.*)$', content, re.MULTILINE | re.IGNORECASE)
    style = style_match.group(1).strip() if style_match else 'dark'

    # Split into slide blocks
    slides_raw = re.split(r'^##\s+Slide\s+', content, flags=re.MULTILINE)[1:]
    slides = []

    for i, slide_raw in enumerate(slides_raw):
        lines = slide_raw.strip().split('\n')
        header = lines[0].strip() # e.g. "1: Hook" or "3: Rule 1"
        slide_num = i + 1

        body = '\n'.join(lines[1:])
        properties = parse_simple_yaml(body)

        if 'Layout' not in properties:
            properties['Layout'] = 'editorial-quote'

        properties['slide_num'] = slide_num
        slides.append(properties)

    return style, slides

def generate_dots(total, active_idx):
    dots = []
    for idx in range(total):
        active_class = "active" if idx == active_idx else ""
        dots.append(f'<div class="carousel-dot {active_class}"></div>')
    return '\n'.join(dots)

def build_slide_html(slide, style, total_slides, base_template_path):
    layout = slide.get('Layout', 'editorial-quote')
    slide_num = slide.get('slide_num', 1)
    
    # Progress dots for value slides
    dots_html = generate_dots(total_slides, slide_num - 1)

    # Format-specific variable substitution
    layout_content = ""

    if layout == 'hook':
        title = slide.get('Title', 'Hook Title')
        subtitle = slide.get('Subtitle', '')
        subtitle_html = f'<div class="hook-subtitle">{subtitle}</div>' if subtitle else ""
        
        cards = slide.get('PreviewCards', [])
        cards_html = ""
        for c in cards:
            text = c.get('Text', '')
            is_premium = "premium" if "pinterest" not in text.lower() else ""
            cards_html += f'<div class="preview-card {is_premium}">{text}</div>\n'
            
        footnote = slide.get('Footnote', '')
        layout_content = f"""
        <div class="canvas-container theme-{style}">
          <div class="layout-hook">
            <div class="hook-badge">✻ ZORIXEL</div>
            <div class="hook-title">{title}</div>
            {subtitle_html}
            <div class="hook-preview-cards">
              {cards_html}
            </div>
            <div class="hook-footnote"><span>{footnote}</span></div>
          </div>
        </div>
        """

    elif layout == 'split-comparison':
        rule_num = slide_num - 2  # Assuming Slide 1 is Hook, Slide 2 is Payoff, Slide 3 is Rule 1
        if rule_num < 1:
            rule_num = 1
            
        title = slide.get('Title', 'Comparison Title')
        subtitle = slide.get('Subtitle', '')
        
        before = slide.get('BeforeCard', {})
        before_text = before.get('Text', 'Before Text')
        before_caption = before.get('Caption', 'Generic')
        
        after = slide.get('AfterCard', {})
        after_text = after.get('Text', 'After Text')
        after_caption = after.get('Caption', 'Optimized')

        layout_content = f"""
        <div class="canvas-container theme-{style}">
          <div class="carousel-header-overlay">
            <div class="carousel-header-text">RULE {rule_num}</div>
            <div class="carousel-header-text">ADARSHXDESIGN</div>
            <div class="carousel-header-text">GRAPHIC DESIGN</div>
          </div>
          
          <div class="layout-split-comparison">
            <div class="comparison-header">
              <div class="comparison-badge">Rule - {rule_num}</div>
              <div class="comparison-title">{title}</div>
              <div class="comparison-subtitle">{subtitle}</div>
            </div>
            
            <div class="comparison-grid">
              <div class="comparison-column">
                <div class="column-label before">Before</div>
                <div class="comparison-card">
                  <div style="font-family: var(--font-code); font-size:12px; color:var(--color-body-light); margin-bottom:12px; font-weight:600; text-transform:uppercase; letter-spacing:1px;">Too Small & Muted</div>
                  <div style="font-family: var(--font-body); font-size:22px; font-weight:400; color:var(--color-body-light); line-height:1.4; max-width:90%;">{before_text}</div>
                </div>
                <div class="comparison-caption">{before_caption}</div>
              </div>
              <div class="comparison-column">
                <div class="column-label after">After</div>
                <div class="comparison-card after-card">
                  <div style="font-family: var(--font-code); font-size:12px; color:var(--color-primary); margin-bottom:12px; font-weight:600; text-transform:uppercase; letter-spacing:1px;">✻ Big & Bold</div>
                  <div style="font-family: var(--font-display); font-size:32px; font-weight:500; color:var(--color-ink); line-height:1.25; max-width:90%;">{after_text}</div>
                </div>
                <div class="comparison-caption">{after_caption}</div>
              </div>
            </div>
          </div>

          <div class="carousel-footer-overlay">
            <div class="carousel-dots">
              {dots_html}
            </div>
          </div>
        </div>
        """

    elif layout == 'editorial-quote':
        title = slide.get('Title', 'Quote content goes here')
        author = slide.get('Author', 'Zorixel')
        layout_content = f"""
        <div class="canvas-container theme-{style}">
          <div class="carousel-header-overlay">
            <div class="carousel-header-text">STEP {slide_num:02d}</div>
            <div class="carousel-header-text">ADARSHXDESIGN</div>
            <div class="carousel-header-text">GRAPHIC DESIGN</div>
          </div>
          
          <div class="layout-editorial-quote">
            <div class="editorial-mark">“</div>
            <div class="editorial-quote-text">{title}</div>
            <div class="editorial-author">— {author}</div>
          </div>

          <div class="carousel-footer-overlay">
            <div class="carousel-dots">
              {dots_html}
            </div>
          </div>
        </div>
        """

    elif layout == 'code-showcase':
        tag = slide.get('Tag', 'CODE')
        title = slide.get('Title', 'Code Showcase')
        code = slide.get('Code', '// No code snippet')
        layout_content = f"""
        <div class="canvas-container theme-{style}">
          <div class="carousel-header-overlay">
            <div class="carousel-header-text">STEP {slide_num:02d}</div>
            <div class="carousel-header-text">ADARSHXDESIGN</div>
            <div class="carousel-header-text">GRAPHIC DESIGN</div>
          </div>
          
          <div class="layout-code-showcase">
            <div class="showcase-header" style="margin-top: var(--spacing-xl);">
              <div class="showcase-tag">{tag}</div>
              <div class="showcase-title">{title}</div>
            </div>
            <div class="code-window">
              <div class="code-window-header">
                <div class="window-dots">
                  <div class="window-dot" style="background-color:#ff5f56;opacity:1;"></div>
                  <div class="window-dot" style="background-color:#ffbd2e;opacity:1;"></div>
                  <div class="window-dot" style="background-color:#27c93f;opacity:1;"></div>
                </div>
              </div>
              <pre class="code-content"><code>{code}</code></pre>
            </div>
          </div>

          <div class="carousel-footer-overlay">
            <div class="carousel-dots">
              {dots_html}
            </div>
          </div>
        </div>
        """

    elif layout == 'bento-features':
        title = slide.get('Title', 'Bento Box')
        subtitle = slide.get('Subtitle', '')
        
        card1 = slide.get('Card1', {})
        card1_title = card1.get('Title', 'Feature 1')
        card1_body = card1.get('Body', '')
        
        card2 = slide.get('Card2', {})
        card2_title = card2.get('Title', 'Feature 2')
        card2_body = card2.get('Body', '')
        
        layout_content = f"""
        <div class="canvas-container theme-{style}">
          <div class="carousel-header-overlay">
            <div class="carousel-header-text">STEP {slide_num:02d}</div>
            <div class="carousel-header-text">ADARSHXDESIGN</div>
            <div class="carousel-header-text">GRAPHIC DESIGN</div>
          </div>
          
          <div class="layout-bento-features">
            <div class="bento-header" style="margin-top: var(--spacing-xl);">
              <div class="bento-title">{title}</div>
              <div class="bento-subtitle">{subtitle}</div>
            </div>
            <div class="bento-grid">
              <div class="bento-card">
                <div class="bento-card-title">{card1_title}</div>
                <div class="bento-card-body">{card1_body}</div>
              </div>
              <div class="bento-card" style="background:var(--color-surface-soft);">
                <div class="bento-card-title">{card2_title}</div>
                <div class="bento-card-body">{card2_body}</div>
              </div>
            </div>
          </div>

          <div class="carousel-footer-overlay">
            <div class="carousel-dots">
              {dots_html}
            </div>
          </div>
        </div>
        """

    elif layout == 'cta':
        tag = slide.get('Tag', 'CTA')
        title = slide.get('Title', 'Comment to download')
        description = slide.get('Description', '')
        button = slide.get('Button', 'Comment')
        layout_content = f"""
        <div class="canvas-container theme-{style}">
          <div class="layout-cta">
            <div class="cta-tag">{tag}</div>
            <div class="cta-title">{title}</div>
            <div class="cta-description">{description}</div>
            <div class="cta-card">
              <span class="cta-button-text">{button}</span>
            </div>
            <div style="font-family:var(--font-body);font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--color-muted);margin-top:50px;font-weight:600;">
              A D A R S H X D E S I G N
            </div>
          </div>
        </div>
        """

    # Load base template
    with open(base_template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Substitute content placeholder
    html = html.replace('<!-- LAYOUT_CONTENT_PLACEHOLDER -->', layout_content)
    
    # Point styles to local folder copy
    html = html.replace('styles.css', 'styles.css')

    return html

def main():
    copy_path = r"d:\AI-OS\brainstorms\temp_carousel\copy.md"
    base_template_path = r"d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\template-base.html"
    styles_css_path = r"d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\styles.css"
    output_dir = r"d:\AI-OS\brainstorms\temp_carousel"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Copy styles.css to output directory so references work locally
    with open(styles_css_path, 'r', encoding='utf-8') as sf:
        with open(os.path.join(output_dir, 'styles.css'), 'w', encoding='utf-8') as df:
            df.write(sf.read())

    style, slides = parse_markdown(copy_path)
    total_slides = len(slides)

    for i, slide in enumerate(slides):
        slide_html = build_slide_html(slide, style, total_slides, base_template_path)
        out_filename = f"slide_{i+1:02d}.html"
        out_path = os.path.join(output_dir, out_filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(slide_html)
        print(f"Generated: {out_path}")

if __name__ == "__main__":
    main()
