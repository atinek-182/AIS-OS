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
    0: '01_opt_a_hero.png',
    1: '02_opt_a_about.png',
    2: '03_opt_a_dashboard.png',
    3: '04_opt_a_poster.png',
    4: '05_opt_a_footer.png',
    5: '06_opt_b_hero.png',
    6: '07_opt_b_about.png',
    7: '08_opt_b_dashboard.png',
    8: '09_opt_b_poster.png',
    9: '10_opt_b_footer.png',
    10: '11_opt_c_hero.png',
    11: '12_opt_c_about.png',
    12: '13_opt_c_dashboard.png',
    13: '14_opt_c_poster.png',
    14: '15_opt_c_footer.png',
    15: '16_opt_d_hero.png',
    16: '17_opt_d_about.png',
    17: '18_opt_d_dashboard.png',
    18: '19_opt_d_poster.png',
    19: '20_opt_d_footer.png'
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
