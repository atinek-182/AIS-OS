# Phase 0.5 Reference: Sitemap & Shared Architecture Scaffolding

## 🗺️ Multi-Page Sitemap Specification

Before writing individual page components, establish a clean site tree:

```json
{
  "site_title": "Project Name",
  "base_url": "https://example.com",
  "routes": [
    {
      "path": "/",
      "name": "Home",
      "layout": "RootLayout",
      "purpose": "Hero narrative, core value proposition, key feature highlights, CTA"
    },
    {
      "path": "/about",
      "name": "About / Story",
      "layout": "RootLayout",
      "purpose": "Brand story, team/origin narrative, philosophy, visual timeline"
    },
    {
      "path": "/features",
      "name": "Features / Product Matrix",
      "layout": "RootLayout",
      "purpose": "Deep product breakdown, interactive feature tabs, comparison matrix"
    },
    {
      "path": "/pricing",
      "name": "Pricing / Plans",
      "layout": "RootLayout",
      "purpose": "Tiered pricing cards, feature toggle (monthly/annual), FAQ accordion"
    },
    {
      "path": "/contact",
      "name": "Contact / Demo",
      "layout": "RootLayout",
      "purpose": "Interactive booking form, direct channels, office location visual"
    }
  ]
}
```

---

## 🏗️ Master `RootLayout` Standards

Every multi-page site generated MUST use a shared master `RootLayout` component wrapping child pages:

1. **Persistent Header Navigation (`<Navbar>`)**:
   - Logo anchor on top-left (Nuqun brand font or clean geometric SVG).
   - Centered route navigation links with active state indicator styling (`aria-current="page"`).
   - Primary action CTA button on top-right ("Get Started", "Book Demo").
   - Responsive Mobile Hamburger menu overlay with smooth fade/slide transitions.

2. **Persistent Global Footer (`<Footer>`)**:
   - Brand mission statement & copyright.
   - Categorized sitemap links matching the route tree.
   - Newsletter signup or primary contact trigger.
   - Social links & legal policy anchors.

3. **SEO Meta Inheritance**:
   - Each sub-page inherits `<title>` and `<meta name="description">` overrides dynamically via route props or Next.js metadata API.
