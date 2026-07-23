import json
import os

def make_rect(id_val, x, y, w, h, strokeColor, backgroundColor, fillStyle="solid", strokeWidth=2, strokeStyle="solid", roundness=None):
    return {
        "id": id_val,
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": strokeColor,
        "backgroundColor": backgroundColor,
        "fillStyle": fillStyle,
        "strokeWidth": strokeWidth,
        "strokeStyle": strokeStyle,
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": roundness,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False
    }

def make_text(id_val, x, y, w, h, text, fontSize, strokeColor="#1e1e1e", textAlign="center", verticalAlign="top", containerId=None):
    return {
        "id": id_val,
        "type": "text",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": strokeColor,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
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
        "text": text,
        "fontSize": fontSize,
        "fontFamily": 1,
        "textAlign": textAlign,
        "verticalAlign": verticalAlign,
        "containerId": containerId,
        "originalText": text,
        "lineHeight": 1.25
    }

def make_arrow(id_val, x, y, points, strokeColor, strokeStyle="solid", strokeWidth=2, startArrowhead=None, endArrowhead="arrow"):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    w = max(xs) - min(xs) if xs else 0
    h = max(ys) - min(ys) if ys else 0
    return {
        "id": id_val,
        "type": "arrow",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": strokeColor,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": strokeWidth,
        "strokeStyle": strokeStyle,
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 2},
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "points": points,
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": startArrowhead,
        "endArrowhead": endArrowhead
    }

def make_diamond(id_val, x, y, w, h, strokeColor, backgroundColor, fillStyle="solid"):
    return {
        "id": id_val,
        "type": "diamond",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": strokeColor,
        "backgroundColor": backgroundColor,
        "fillStyle": fillStyle,
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False
    }

def make_line(id_val, x, y, points, strokeColor, strokeStyle="dashed", strokeWidth=2):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    w = max(xs) - min(xs) if xs else 0
    h = max(ys) - min(ys) if ys else 0
    return {
        "id": id_val,
        "type": "line",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": strokeColor,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": strokeWidth,
        "strokeStyle": strokeStyle,
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "points": points,
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": None
    }

elements = []

# Title
elements.append(make_text("title", 50, 20, 1120, 40, "Application Security Architecture & Perimeters", 28, strokeColor="#1e1e1e"))

# Container 1: Client Zone (External / Untrusted)
elements.append(make_rect("c1", 50, 140, 220, 480, "#1971c2", "#e7f5ff", roundness={"type": 3}))
elements.append(make_text("c1-title", 50, 155, 220, 30, "1. Client Zone\n(Untrusted External)", 18, strokeColor="#1971c2"))

# Sibling cards in C1
# Card 1: Legit Client
elements.append(make_rect("c1-legit", 70, 210, 180, 100, "#1971c2", "#a5d8ff", roundness={"type": 3}))
elements.append(make_text("c1-legit-txt", 70, 220, 180, 80, "Legitimate Client\n- Browser / Mobile App\n- Valid cookie / session token\n- HTTPS encrypted transport", 13, strokeColor="#1e1e1e", containerId="c1-legit"))

# Card 2: Attacker
elements.append(make_rect("c1-attack", 70, 390, 180, 100, "#c92a2a", "#ffe3e3", roundness={"type": 3}))
elements.append(make_text("c1-attack-txt", 70, 400, 180, 80, "Threat Actor / Bots\n- SQL Injection scripts\n- Credential stuffing tools\n- Volumetric DDoS attacks", 13, strokeColor="#c92a2a", containerId="c1-attack"))


# Container 2: Perimeter Defense Zone
elements.append(make_rect("c2", 340, 140, 240, 480, "#f59f00", "#fff9db", roundness={"type": 3}))
elements.append(make_text("c2-title", 340, 155, 240, 30, "2. Perimeter Security\n(Edge & Gateways)", 18, strokeColor="#f59f00"))

# Sibling cards in C2
# Card 1: DDoS protection
elements.append(make_rect("c2-ddos", 360, 210, 200, 80, "#f59f00", "#ffe066", roundness={"type": 3}))
elements.append(make_text("c2-ddos-txt", 360, 220, 200, 60, "DDoS Protection & CDN\n- Volumetric rate limits\n- Threat intelligence lookup", 13, strokeColor="#1e1e1e", containerId="c2-ddos"))

# Card 2: WAF
elements.append(make_rect("c2-waf", 360, 310, 200, 80, "#f59f00", "#ffe066", roundness={"type": 3}))
elements.append(make_text("c2-waf-txt", 360, 320, 200, 60, "Web App Firewall (WAF)\n- Blocks OWASP Top 10\n- Inspects payload signatures", 13, strokeColor="#1e1e1e", containerId="c2-waf"))

# Card 3: API Gateway
elements.append(make_rect("c2-gw", 360, 410, 200, 100, "#f59f00", "#ffe066", roundness={"type": 3}))
elements.append(make_text("c2-gw-txt", 360, 420, 200, 80, "API Gateway / TLS\n- TLS session termination\n- API key & CORS checks\n- Route management", 13, strokeColor="#1e1e1e", containerId="c2-gw"))


# Container 3: Application Security Zone
elements.append(make_rect("c3", 640, 140, 240, 480, "#2f9e44", "#d3f9d8", roundness={"type": 3}))
elements.append(make_text("c3-title", 640, 155, 240, 30, "3. App Logic Security\n(Internal Trust Zone)", 18, strokeColor="#2f9e44"))

# Sibling cards in C3
# Card 1: AuthN / AuthZ
elements.append(make_rect("c3-auth", 660, 210, 200, 80, "#2f9e44", "#b2f2bb", roundness={"type": 3}))
elements.append(make_text("c3-auth-txt", 660, 220, 200, 60, "AuthN & AuthZ check\n- JWT signature verification\n- Role/Attribute RBAC checks", 13, strokeColor="#1e1e1e", containerId="c3-auth"))

# Card 2: Input validation
elements.append(make_rect("c3-input", 660, 310, 200, 80, "#2f9e44", "#b2f2bb", roundness={"type": 3}))
elements.append(make_text("c3-input-txt", 660, 320, 200, 60, "Input Validation\n- JSON schema constraint\n- Input sanitization & escaping", 13, strokeColor="#1e1e1e", containerId="c3-input"))

# Card 3: Runtime Security
elements.append(make_rect("c3-run", 660, 410, 200, 100, "#2f9e44", "#b2f2bb", roundness={"type": 3}))
elements.append(make_text("c3-run-txt", 660, 420, 200, 80, "Secure Code & Runtime\n- App-level rate limiting\n- Secure exception handling\n- Dependency vulnerability check", 13, strokeColor="#1e1e1e", containerId="c3-run"))


# Container 4: Data Security Zone
elements.append(make_rect("c4", 940, 140, 240, 480, "#495057", "#f8f9fa", roundness={"type": 3}))
elements.append(make_text("c4-title", 940, 155, 240, 30, "4. Data & Infra Security\n(Isolated Data Zone)", 18, strokeColor="#495057"))

# Sibling cards in C4
# Card 1: DB Firewall
elements.append(make_rect("c4-dbfw", 960, 210, 200, 80, "#495057", "#e9ecef", roundness={"type": 3}))
elements.append(make_text("c4-dbfw-txt", 960, 220, 200, 60, "Database Firewall\n- Restricts port to app subnet\n- IP/VPC subnet whitelisting", 13, strokeColor="#1e1e1e", containerId="c4-dbfw"))

# Card 2: Encryption
elements.append(make_rect("c4-enc", 960, 310, 200, 80, "#495057", "#e9ecef", roundness={"type": 3}))
elements.append(make_text("c4-enc-txt", 960, 320, 200, 60, "Data Encryption\n- At Rest (AES-256)\n- Dynamic column-level crypting", 13, strokeColor="#1e1e1e", containerId="c4-enc"))

# Card 3: Secrets & Audit
elements.append(make_rect("c4-vault", 960, 410, 200, 100, "#495057", "#e9ecef", roundness={"type": 3}))
elements.append(make_text("c4-vault-txt", 960, 420, 200, 80, "Secrets & Audit Log\n- Database credential vault\n- Key rotation policy\n- Comprehensive query log", 13, strokeColor="#1e1e1e", containerId="c4-vault"))


# Cross-cutting Identity Provider (IdP) Card
elements.append(make_rect("idp", 640, 20, 240, 90, "#862e9c", "#f3d9fa", roundness={"type": 3}))
elements.append(make_text("idp-txt", 640, 30, 240, 70, "Identity Provider (IdP)\n- Auth0 / Cognito / Keycloak\n- Multi-Factor Auth (MFA)\n- Central user directory", 13, strokeColor="#862e9c", containerId="idp"))


# Trust Boundary Dotted Line
elements.append(make_line("boundary", 305, 80, [[0, 0], [0, 560]], "#868e96", strokeStyle="dashed", strokeWidth=2))
elements.append(make_text("boundary-txt", 255, 85, 100, 30, "Trust Boundary", 12, strokeColor="#868e96"))


# Arrows
# 1. Legit User to DDoS CDN
elements.append(make_arrow("arr-legit-ddos", 250, 260, [[0, 0], [110, -10]], "#1971c2"))
elements.append(make_text("arr-legit-ddos-txt", 250, 230, 110, 20, "HTTPS Request", 12, strokeColor="#1971c2"))

# 2. DDoS CDN to WAF
elements.append(make_arrow("arr-ddos-waf", 460, 290, [[0, 0], [0, 20]], "#f59f00"))

# 3. WAF to Gateway
elements.append(make_arrow("arr-waf-gw", 460, 390, [[0, 0], [0, 20]], "#f59f00"))

# 4. Gateway to Auth
elements.append(make_arrow("arr-gw-auth", 560, 460, [[0, 0], [50, 0], [50, -210], [100, -210]], "#2f9e44"))

# 5. Auth to Input
elements.append(make_arrow("arr-auth-input", 760, 290, [[0, 0], [0, 20]], "#2f9e44"))

# 6. Input to Runtime
elements.append(make_arrow("arr-input-run", 760, 390, [[0, 0], [0, 20]], "#2f9e44"))

# 7. Runtime to DB Firewall
elements.append(make_arrow("arr-run-dbfw", 860, 460, [[0, 0], [50, 0], [50, -210], [100, -210]], "#495057"))

# 8. DB Firewall to Encryption
elements.append(make_arrow("arr-dbfw-enc", 1060, 290, [[0, 0], [0, 20]], "#495057"))

# 9. Encryption to Vault
elements.append(make_arrow("arr-enc-vault", 1060, 390, [[0, 0], [0, 20]], "#495057"))


# Auth verify flow to IdP (Up)
elements.append(make_arrow("arr-auth-idp-up", 730, 210, [[0, 0], [0, -100]], "#862e9c"))
elements.append(make_text("arr-auth-idp-up-txt", 610, 140, 110, 30, "Verify Token\n/ Claims", 11, strokeColor="#862e9c"))

# Auth response from IdP (Down)
elements.append(make_arrow("arr-idp-auth-down", 790, 110, [[0, 0], [0, 100]], "#862e9c"))
elements.append(make_text("arr-idp-auth-down-txt", 805, 140, 110, 30, "Validation\nResult", 11, strokeColor="#862e9c"))


# Attacker Attack Blocked Flow
elements.append(make_arrow("arr-attack-waf", 250, 440, [[0, 0], [60, 0], [60, -90], [110, -90]], "#c92a2a", strokeStyle="dashed"))

# Blocked Badge (Diamond)
elements.append(make_diamond("blocked-badge", 280, 375, 80, 40, "#c92a2a", "#ffe3e3"))
elements.append(make_text("blocked-badge-txt", 280, 385, 80, 20, "BLOCKED!", 11, strokeColor="#c92a2a"))

data = {
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

out_path = "d:/AI-OS/diagrams/apps-security.excalidraw"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Generated diagram successfully at", out_path)
