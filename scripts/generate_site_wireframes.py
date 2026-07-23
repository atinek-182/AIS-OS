import os
import json

def create_excalidraw_wireframe(site_slug, title, sections):
    elements = []
    
    # 1. Root Browser Shell (1200 x 900)
    root_id = "root_frame"
    elements.append({
        "id": root_id,
        "type": "rectangle",
        "x": 50, "y": 50,
        "width": 1100, "height": 900,
        "angle": 0,
        "strokeColor": "#343a40",
        "backgroundColor": "#f8f9fa",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3},
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False
    })
    
    # Header Title
    elements.append({
        "id": "title_text",
        "type": "text",
        "x": 70, "y": 70,
        "width": 1060, "height": 35,
        "angle": 0,
        "strokeColor": "#1971c2",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "text": f"WIREFRAME ARCHITECTURE — {title.upper()}",
        "fontSize": 24,
        "fontFamily": 1,
        "textAlign": "left",
        "verticalAlign": "top",
        "containerId": None,
        "originalText": f"WIREFRAME ARCHITECTURE — {title.upper()}",
        "lineHeight": 1.25
    })
    
    # Render Layout Blocks
    curr_y = 120
    for idx, sec in enumerate(sections):
        sec_h = sec.get("height", 140)
        sec_bg = sec.get("bg", "#e7f5ff")
        sec_stroke = sec.get("stroke", "#1971c2")
        
        # Section Box
        sec_id = f"sec_{idx}"
        elements.append({
            "id": sec_id,
            "type": "rectangle",
            "x": 70, "y": curr_y,
            "width": 1060, "height": sec_h,
            "angle": 0,
            "strokeColor": sec_stroke,
            "backgroundColor": sec_bg,
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 3},
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False
        })
        
        # Section Label
        elements.append({
            "id": f"sec_label_{idx}",
            "type": "text",
            "x": 90, "y": curr_y + 15,
            "width": 1020, "height": 25,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False,
            "text": sec["title"],
            "fontSize": 18,
            "fontFamily": 1,
            "textAlign": "left",
            "verticalAlign": "top",
            "containerId": None,
            "originalText": sec["title"],
            "lineHeight": 1.25
        })
        
        # Section Details
        elements.append({
            "id": f"sec_desc_{idx}",
            "type": "text",
            "x": 90, "y": curr_y + 45,
            "width": 1020, "height": 40,
            "angle": 0,
            "strokeColor": "#495057",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False,
            "text": sec.get("desc", ""),
            "fontSize": 14,
            "fontFamily": 1,
            "textAlign": "left",
            "verticalAlign": "top",
            "containerId": None,
            "originalText": sec.get("desc", ""),
            "lineHeight": 1.25
        })
        
        curr_y += sec_h + 15
        
    excalidraw_doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff"
        },
        "files": {}
    }
    
    out_dir = os.path.join(r"d:\AI-OS\premium-frontend-experience-system\reference-inputs\sites", site_slug, "assets")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "wireframe.excalidraw")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(excalidraw_doc, f, indent=2)
    print(f"[WIREFRAME] Saved {out_file}")

# 1. Sondaven Wireframe
create_excalidraw_wireframe("sondaven", "Sondaven Luxury Resort", [
    {"title": "NAVBAR & PRELOADER", "desc": "Fixed minimalist header, language switcher (EN/RO), acoustic visualizer, visit detection", "height": 90, "bg": "#e7f5ff", "stroke": "#1971c2"},
    {"title": "HERO STAGE (FULLSCREEN)", "desc": "Full-bleed hero typography, kinetic word reveal stagger, 3D cloud terrain WebGL canvas stage", "height": 160, "bg": "#fff9db", "stroke": "#f59f00"},
    {"title": "PARALLAX SCROLLESTELLING & ACCORDION", "desc": "Lenis smooth scroll inertia, interactive benefit morphing cards, marquee velocity text", "height": 160, "bg": "#d3f9d8", "stroke": "#2f9e44"},
    {"title": "DRAG-ALONG-PATH SVG SEASON SLIDER", "desc": "Seasonal experience slider tracking getPointAtLength() SVG curve math", "height": 130, "bg": "#f3d9fa", "stroke": "#862e9c"},
    {"title": "180° CARD FLIP FORM & FOOTER", "desc": "Interactive reservation modal with 180° Y-axis card flip submit animation", "height": 130, "bg": "#ffe3e3", "stroke": "#c92a2a"}
])

# 2. Oryzo AI Wireframe
create_excalidraw_wireframe("oryzo-ai", "Oryzo AI Satirical Physical Hardware", [
    {"title": "NAV & TOP TAGLINE", "desc": "Minimalist dark header, Space Mono utility badges, 'Made for mugs. Built for tables.'", "height": 90, "bg": "#e7f5ff", "stroke": "#1971c2"},
    {"title": "3D GAUSSIAN SPLAT HERO CANVAS", "desc": "Three.js r178 WebGL stage rendering decoded 3D coaster splat model in Web Worker", "height": 160, "bg": "#fff9db", "stroke": "#f59f00"},
    {"title": "60,000px SCROLL CONTAINER & WEARABLE GALLERY", "desc": "GSAP ScrollTrigger scrubber translating 3D model across wrist, shoulder, & bikini mockups", "height": 160, "bg": "#d3f9d8", "stroke": "#2f9e44"},
    {"title": "SATIRICAL MAGAZINE & PROMPT WIDGET", "desc": "Interactive magazine issue cover ticker with active @oryzo AI prompt input box", "height": 140, "bg": "#f3d9fa", "stroke": "#862e9c"},
    {"title": "REVIEWS CAROUSEL & CTA OUTRO", "desc": "Customer review cards with interactive star physics & glowing orange CTA buttons", "height": 120, "bg": "#ffe3e3", "stroke": "#c92a2a"}
])

# 3. The Line Studio Wireframe
create_excalidraw_wireframe("the-line-studio", "The Line Studio London", [
    {"title": "KINETIC LOGO & NAVIGATION HEADER", "desc": "Electric Red dot indicator, status tag (LONDON), email trigger, mobile slide-out nav", "height": 90, "bg": "#e7f5ff", "stroke": "#1971c2"},
    {"title": "FEATURED PROJECT SHOWCASE TICKER", "desc": "Vertical project list with electric red multiply blend overlay and video preview hover", "height": 170, "bg": "#fff9db", "stroke": "#f59f00"},
    {"title": "ABOUT & STUDIO AWARDS GRID", "desc": "DenimWeb variable font layout, client logo wall, BAFTA/Cannes award list links", "height": 150, "bg": "#d3f9d8", "stroke": "#2f9e44"},
    {"title": "MEDIA PLAYER & NEWS LISTING", "desc": "Rotated card player modal with forced aspect ratio video playback and news grid", "height": 140, "bg": "#f3d9fa", "stroke": "#862e9c"},
    {"title": "ROTATED CARD PAGE TRANSITION FOOTER", "desc": "Page transition trigger tilting page 4° with exponential cubic-bezier curve", "height": 120, "bg": "#ffe3e3", "stroke": "#c92a2a"}
])

# 4. Gehry Getty Wireframe
create_excalidraw_wireframe("gehry-getty", "Frank Gehry Archive Getty", [
    {"title": "ARCHIVAL LOGO & HEADER", "desc": "Getty Research Institute header, archival off-white background, 3D Model Explorer badge", "height": 90, "bg": "#e7f5ff", "stroke": "#1971c2"},
    {"title": "3D GLTF ARCHITECTURAL MODEL CANVAS", "desc": "Three.js WebGL orbit stage rendering Frank Gehry 3D form study models (.glb)", "height": 170, "bg": "#fff9db", "stroke": "#f59f00"},
    {"title": "INTERACTIVE 3D HOTSPOT PINS", "desc": "Screen-space vector hotspot pins opening architectural drawer annotations on click", "height": 140, "bg": "#d3f9d8", "stroke": "#2f9e44"},
    {"title": "MULTI-CHAPTER GUIDED AUDIO PLAYER", "desc": "Multi-chapter audio stream player with timecoded JSON transcript subtitles", "height": 140, "bg": "#f3d9fa", "stroke": "#862e9c"},
    {"title": "ARCHIVE FOOTER & CITATION METADATA", "desc": "Storyblok CMS integration, architectural credits, and citation tools", "height": 120, "bg": "#ffe3e3", "stroke": "#c92a2a"}
])
