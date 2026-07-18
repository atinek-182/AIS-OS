const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Set viewport to fixed 1920x1080 design stage size
  await page.setViewportSize({ width: 1920, height: 1080 });
  
  // Track console errors
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(`[Console Error] ${msg.text()}`);
    }
  });

  page.on('pageerror', exception => {
    consoleErrors.push(`[Page Exception] ${exception.toString()}`);
  });

  // Ensure screenshot folder exists
  const ssDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(ssDir)) {
    fs.mkdirSync(ssDir, { recursive: true });
  }

  // Generate file:// URL for presentation.html
  const fileUrl = 'file:///' + path.join(__dirname, '..', 'presentation.html').replace(/\\/g, '/');
  console.log(`Loading local page URL: ${fileUrl}`);
  await page.goto(fileUrl);
  
  // Wait for font assets to load fully in browser memory
  await page.evaluate(() => document.fonts.ready);
  
  // Get count of slides
  const slideCount = await page.evaluate(() => document.querySelectorAll('.slide').length);
  console.log(`Verified slide deck with ${slideCount} slides.`);

  // Map slide indices to target filenames
  const targets = {
    0: '01_cover.png',
    1: '02_font_directory.png',
    2: '03_route_a_vibe.png',
    3: '04_route_a_logo.png',
    4: '05_route_a_card.png',
    5: '06_route_a_poster.png',
    6: '07_route_b_vibe.png',
    7: '08_route_b_logo.png',
    8: '09_route_b_card.png',
    9: '10_route_b_poster.png',
    10: '11_route_c_vibe.png',
    11: '12_route_c_logo.png',
    12: '13_route_c_card.png',
    13: '14_route_c_poster.png',
    14: '15_route_d_vibe.png',
    15: '16_route_d_logo.png',
    16: '17_route_d_card.png',
    17: '18_route_d_poster.png',
    18: '19_voting_dashboard.png',
    19: '20_mega_intro.png',
    20: '21_mega_a_b.png',
    21: '22_mega_c_d.png',
    22: '23_mega_nuqun_logo.png',
    23: '24_rounded_poster_a.png',
    24: '25_rounded_poster_b.png',
    25: '26_refined_hybrid.png',
    26: '27_refined_logo_b.png',
    27: '28_refined_logo_d.png',
    28: '29_refined_poster_b.png',
    29: '30_refined_poster_d.png',
    30: '31_newmix_footer.png',
    31: '32_editorial_analysis.png',
    32: '33_editorial_cover.png',
    33: '34_newsletter_stats.png'
  };

  // Traverse through each slide and capture screenshot
  for (let i = 0; i < slideCount; i++) {
    await page.evaluate((idx) => {
      presentation.showSlide(idx);
    }, i);
    
    // Allow animation transitions (600ms opacity transition) to finish
    await page.waitForTimeout(650);

    const filename = targets[i] || `slide_${i + 1}.png`;
    const ssPath = path.join(ssDir, filename);
    await page.screenshot({ path: ssPath });
    console.log(`Captured slide ${i + 1}/${slideCount} -> qa/screenshots/${filename}`);
  }

  await browser.close();

  // Print results
  console.log('\n--- PLAYWRIGHT AUDIT RESULTS ---');
  if (consoleErrors.length > 0) {
    console.error(`Errors encountered during presentation rendering:`);
    consoleErrors.forEach(err => console.error(err));
    process.exit(1);
  } else {
    console.log('Success! All slides rendered cleanly with zero console errors/exceptions.');
    process.exit(0);
  }
})();
