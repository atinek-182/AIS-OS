---
name: scrape-carousel
description: Automatically scrape, screenshot, and extract design references from a public Instagram or social media carousel URL.
---

# Scrape Carousel

You are the Zorixel AI Scraper. Your task is to navigate to a public Instagram carousel URL, purge any login popups, and automatically extract clean, cropped screenshots of all individual slides to serve as visual references.

When this skill is invoked via `/scrape-carousel --url <url>`:

1. **Open Browser**: Launch Playwright and navigate to the Instagram post URL.
2. **Resize Viewport**: Set the browser viewport size to `1280` x `960` (desktop view) to ensure layout stability.
3. **Bypass Login Walls**: Evaluate this JavaScript on the page to remove Instagram's login block overlays:
   ```javascript
   document.querySelectorAll('[role="dialog"], [role="presentation"], ._ab1y').forEach(el => el.remove());
   document.body.style.overflow = "auto";
   document.documentElement.style.overflow = "auto";
   ```
4. **Capture Slides Loop**:
   - Establish a loop for each slide (slide index from 1 to 10 max).
   - For each slide:
     - **Find Visible Slide Element**: Evaluate a script to locate the active, visible image in the viewport:
       ```javascript
       const visibleImg = Array.from(document.querySelectorAll('img')).find(img => {
         const rect = img.getBoundingClientRect();
         return rect.width > 400 && rect.x >= 0 && rect.x < window.innerWidth;
       });
       if (visibleImg) {
         visibleImg.id = "active-slide-img";
         true;
       } else {
         false;
       }
       ```
     - **Screenshot Element**: If found, take a screenshot of target `#active-slide-img` and save it to:
       `d:\AI-OS\brainstorms\references\scraped_slide_{index:02d}.png`
     - **Transition to Next**: Find the carousel next button and click it:
       ```javascript
       const nextBtn = Array.from(document.querySelectorAll('button')).find(b => {
         const label = b.getAttribute('aria-label') || '';
         return label.toLowerCase().includes('next') || b.querySelector('svg[aria-label="Next"]');
       });
       if (nextBtn) {
         nextBtn.click();
         true;
       } else {
         false;
       }
       ```
     - **Wait**: Wait 1500ms for slide transition animations to finish.
     - **Break Condition**: If no next button is found, or the page URL remains unchanged after transition, terminate the loop.
5. **Output**: List the file paths of all scraped screenshots.
