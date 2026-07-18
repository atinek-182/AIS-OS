const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const fontsDir = path.join(__dirname, 'fonts');
  const targetDir = __dirname;
  const artifactDir = 'C:\\Users\\HP\\.gemini\\antigravity-ide\\brain\\c890bf99-ca4e-49da-9939-9c0c96b28570';

  console.log('Generating high-resolution 2000x2000 PNG & vector SVG logos in Nuqun font...');

  // Read Nuqun font buffer for base64 embedding
  const fontPath = path.join(fontsDir, 'Nuqun-Regular.otf');
  const fontBuffer = fs.readFileSync(fontPath);
  const fontBase64 = fontBuffer.toString('base64');

  // 1. RENDER HTML PNG STYLES
  const htmlContent = `
<!DOCTYPE html>
<html>
<head>
<style>
    @font-face {
        font-family: 'Nuqun';
        src: url('data:font/opentype;base64,${fontBase64}') format('opentype');
    }
    body {
        margin: 0;
        width: 2000px;
        height: 2000px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: transparent;
        overflow: hidden;
    }
    .logo-container {
        font-family: 'Nuqun';
        font-size: 340px;
        text-transform: lowercase;
        letter-spacing: 0.05em;
        text-align: center;
        font-weight: bold;
    }
    .aberration {
        color: #ffffff;
        text-shadow: -6px 0px 0px rgba(0, 245, 255, 0.95), 6px 0px 0px rgba(255, 60, 0, 0.95);
    }
    .solid-white {
        color: #ffffff;
    }
    .solid-dark {
        color: #111111;
    }
</style>
</head>
<body>
    <div id="logo" class="logo-container aberration">zorixel</div>
</body>
</html>
`;

  // Write temporary renderer page
  const tempHtmlPath = path.join(__dirname, 'temp_nuqun_renderer.html');
  fs.writeFileSync(tempHtmlPath, htmlContent, 'utf-8');

  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Set viewport to exactly 2000x2000
  await page.setViewportSize({ width: 2000, height: 2000 });

  await page.goto(`file:///${tempHtmlPath.replace(/\\\\/g, '/')}`);
  await page.waitForTimeout(1000); // Allow extra time for font loading and rendering

  // PNG 1: Transparent Chromatic Aberration
  const p1 = path.join(targetDir, 'zorixel_logo_transparent.png');
  const a1 = path.join(artifactDir, 'zorixel_logo_transparent.png');
  await page.screenshot({ path: p1, omitBackground: true });
  fs.copyFileSync(p1, a1);
  console.log(`Saved transparent chromatic aberration logo: ${p1}`);

  // PNG 2: Black Background Chromatic Aberration
  await page.evaluate(() => {
    document.body.style.backgroundColor = '#0c0d12';
  });
  await page.waitForTimeout(200);
  const p2 = path.join(targetDir, 'zorixel_logo_background.png');
  const a2 = path.join(artifactDir, 'zorixel_logo_background.png');
  await page.screenshot({ path: p2 });
  fs.copyFileSync(p2, a2);
  console.log(`Saved background chromatic aberration logo: ${p2}`);

  // Reset background
  await page.evaluate(() => {
    document.body.style.backgroundColor = 'transparent';
  });

  // PNG 3: Solid White (Transparent Background)
  await page.evaluate(() => {
    const el = document.getElementById('logo');
    el.className = 'logo-container solid-white';
  });
  await page.waitForTimeout(200);
  const p3 = path.join(targetDir, 'zorixel_logo_solid_white.png');
  const a3 = path.join(artifactDir, 'zorixel_logo_solid_white.png');
  await page.screenshot({ path: p3, omitBackground: true });
  fs.copyFileSync(p3, a3);
  console.log(`Saved solid white logo: ${p3}`);

  // PNG 4: Solid Dark (Transparent Background)
  await page.evaluate(() => {
    const el = document.getElementById('logo');
    el.className = 'logo-container solid-dark';
  });
  await page.waitForTimeout(200);
  const p4 = path.join(targetDir, 'zorixel_logo_solid_dark.png');
  const a4 = path.join(artifactDir, 'zorixel_logo_solid_dark.png');
  await page.screenshot({ path: p4, omitBackground: true });
  fs.copyFileSync(p4, a4);
  console.log(`Saved solid dark logo: ${p4}`);

  // Clean up temp html file
  fs.unlinkSync(tempHtmlPath);

  // 2. VECTOR SVG GENERATION VIA OPENTYPE.JS IN BROWSER
  console.log('Generating vector SVG files via opentype.js...');
  
  // Inject opentype.js
  await page.goto('about:blank');
  await page.addScriptTag({ url: 'https://cdnjs.cloudflare.com/ajax/libs/opentype.js/1.3.4/opentype.min.js' });

  // Read Nuqun font buffer (reused from outer scope)

  const pathData = await page.evaluate(async (base64Font) => {
    const binaryString = atob(base64Font);
    const len = binaryString.length;
    const bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    const arrayBuffer = bytes.buffer;

    const font = opentype.parse(arrayBuffer);
    
    // Calculate path for text "zorixel"
    const text = 'zorixel';
    const fontSize = 180;
    
    // Get glyphs and spacing
    const glyphs = font.stringToGlyphs(text);
    let textWidth = 0;
    for (let i = 0; i < glyphs.length; i++) {
      const glyph = glyphs[i];
      if (glyph.advanceWidth) {
        textWidth += glyph.advanceWidth;
      }
      if (i < glyphs.length - 1) {
        textWidth += font.getKerningValue(glyph, glyphs[i + 1]);
      }
    }
    
    // Scale textWidth
    const scale = 1 / font.unitsPerEm * fontSize;
    const width = textWidth * scale;
    
    // Center it in a 1000x1000 viewport
    const x = (1000 - width) / 2;
    const y = 500 + (fontSize * 0.35); // offset baseline to center

    const path = font.getPath(text, x, y, fontSize);
    return path.toPathData();
  }, fontBase64);

  // Write SVGs with stroke expansion to match synthetic bolding
  const svgWhite = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="100%" height="100%">
  <path d="${pathData}" fill="#ffffff" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" />
</svg>
  `.trim();

  const svgDark = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="100%" height="100%">
  <path d="${pathData}" fill="#111111" stroke="#111111" stroke-width="5" stroke-linejoin="round" />
</svg>
  `.trim();

  const svgAberration = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="100%" height="100%">
  <!-- Cyan shift (left) -->
  <path d="${pathData}" fill="#00f5ff" stroke="#00f5ff" stroke-width="5" stroke-linejoin="round" transform="translate(-3, 0)" opacity="0.9" />
  <!-- Red shift (right) -->
  <path d="${pathData}" fill="#ff3c00" stroke="#ff3c00" stroke-width="5" stroke-linejoin="round" transform="translate(3, 0)" opacity="0.9" />
  <!-- Center White -->
  <path d="${pathData}" fill="#ffffff" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" />
</svg>
  `.trim();

  // Save SVG files
  const svgFiles = {
    'zorixel_logo_solid_white.svg': svgWhite,
    'zorixel_logo_solid_dark.svg': svgDark,
    'zorixel_logo_aberration.svg': svgAberration
  };

  for (const [filename, content] of Object.entries(svgFiles)) {
    const filePath = path.join(targetDir, filename);
    const artPath = path.join(artifactDir, filename);
    fs.writeFileSync(filePath, content, 'utf-8');
    fs.copyFileSync(filePath, artPath);
    console.log(`Saved SVG file: ${filePath}`);
  }

  await browser.close();
  console.log('Successfully generated all Nuqun logo assets!');
})();
