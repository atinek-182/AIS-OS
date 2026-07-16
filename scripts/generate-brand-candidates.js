const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUTPUT_FILE = path.join(__dirname, '..', 'second-brain-zorixel', 'wiki', 'brand', 'candidates.md');

async function run() {
  console.log('Launching Playwright...');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const brandCandidates = {
    fonts: [],
    palettes: []
  };

  // ==========================================
  // 1. EXTRACT FONT PAIRINGS FOR ZORIXEL
  // ==========================================
  try {
    console.log('Navigating to Typeface Picker...');
    await page.goto('http://localhost:3000/tool-typeface-picker.html');

    // Fill out brand info
    console.log('Filling brand details...');
    await page.fill('#brandName', 'ZORIXEL');
    await page.selectOption('#industry', 'Education');
    await page.selectOption('#audience', 'Creatives');
    await page.selectOption('#brandTone', 'Inspirational');

    // Click brand personalities: Friendly, Creative, Bold
    console.log('Selecting brand personalities...');
    await page.click('#personalityTags [data-value="Friendly"]');
    await page.click('#personalityTags [data-value="Creative"]');
    await page.click('#personalityTags [data-value="Bold"]');

    // Click search button
    console.log('Triggering font pairings logic...');
    await page.click('button:has-text("Find Font Pairings")');

    // Extract recommendations
    await page.waitForSelector('.tool-font-card');
    const cards = await page.$$('.tool-font-card');
    
    console.log(`Discovered ${cards.length} font pairing recommendations.`);

    for (const card of cards) {
      const name = await card.$eval('strong', el => el.textContent);
      const match = await card.$eval('span[style*="color: var(--accent)"]', el => el.textContent);
      const fonts = await card.$eval('div[style*="font-size: var(--text-sm)"]', el => el.textContent);
      const tags = await card.$$eval('.tool-font-meta-tag', els => els.map(el => el.textContent));

      brandCandidates.fonts.push({
        name,
        match,
        fonts,
        tags
      });
    }
  } catch (err) {
    console.error('Error running Typeface Picker:', err.message);
  }

  // ==========================================
  // 2. GENERATE COLOR PALETTES FOR ZORIXEL
  // ==========================================
  const strategies = [
    { id: 'analogous', label: 'Analogous (Color Theory)' },
    { id: 'monochromatic', label: 'Monochromatic (Color Theory)' },
    { id: '70s', label: '1970s Vintage (Decades & Eras)' },
    { id: 'desert-dusk', label: 'Desert Dusk (Nature)' },
    { id: 'bauhaus', label: 'Bauhaus Bold (Art & Culture)' }
  ];

  try {
    console.log('Navigating to Palette Generator...');
    await page.goto('http://localhost:3000/tool-palette-generator.html');

    for (const strat of strategies) {
      console.log(`Generating palette for: ${strat.label}...`);
      await page.selectOption('#strategySelect', strat.id);
      await page.click('#generateBtn');

      // Add a tiny delay to ensure transition completes
      await page.waitForTimeout(200);

      // Extract colors
      const colors = await page.$$eval('#paletteRow .palette-color-hex', els => els.map(el => el.textContent));
      
      brandCandidates.palettes.push({
        strategy: strat.label,
        colors
      });
    }
  } catch (err) {
    console.error('Error running Palette Generator:', err.message);
  }

  // Close browser
  await browser.close();

  // ==========================================
  // 3. WRITE CANDIDATES MARKDOWN FILE
  // ==========================================
  console.log(`Writing candidate assets to: ${OUTPUT_FILE}`);
  fs.mkdirSync(path.dirname(OUTPUT_FILE), { recursive: true });

  let mdContent = `# Zorixel Brand Styling Candidates

Generated programmatically from Jordan's Archives local design tools on ${new Date().toISOString().split('T')[0]}.

---

## Recommended Font Pairings

These fonts match Zorixel's target profile: **Education** industry, **Creatives** audience, **Inspirational** tone, and **Friendly, Creative, Bold** personalities.

| Pairing Style | Match Rating | Fonts | Matches Keywords |
|---|---|---|---|
`;

  brandCandidates.fonts.forEach(f => {
    mdContent += `| **${f.name}** | ${f.match} | ${f.fonts} | \`${f.tags.join('`, `')}\` |\n`;
  });

  mdContent += `
---

## Candidate Color Palettes

These palettes were generated using different harmonizing strategies from the Jordan Archives color engine.

`;

  brandCandidates.palettes.forEach(p => {
    mdContent += `### 🎨 ${p.strategy}\n`;
    mdContent += `*   **Hex codes:** ${p.colors.map(c => `\`${c}\``).join(', ')}\n`;
    
    // Draw visual markdown block colors
    mdContent += `*   **Visual Preview:** `;
    p.colors.forEach(c => {
      // Create colored squares using styled HTML in markdown
      mdContent += `<span style="background-color: ${c}; border: 1px solid #1a2d14; display: inline-block; width: 30px; height: 15px; margin-right: 4px; border-radius: 2px;"></span> `;
    });
    mdContent += `\n\n`;
  });

  mdContent += `
---

## Next Steps

1. Review these candidates to select the final **Zorixel** typography and color scheme.
2. Log the final styling decisions in \`decisions/log.md\` and \`second-brain-zorixel/wiki/brand/index.md\`.
`;

  fs.writeFileSync(OUTPUT_FILE, mdContent);
  console.log('Candidates file created successfully!');
}

run();
