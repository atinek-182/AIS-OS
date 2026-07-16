const fs = require('fs');
const path = require('path');

const TARGET_DIR = path.join(__dirname, '..', 'second-brain-zorixel', 'wiki', 'research', 'jordan-watkins-reference');
const BASE_URL = 'https://jordanwatkins.xyz/';

const RESOURCES = [
  // Core pages
  'index.html',
  'tools.html',
  'about.html',
  'products.html',

  // Styles
  'base.css',
  'style.css',
  'tools-page.css',

  // JS Modules
  'pixel-canvas.js',
  'paper-texture.js',
  'character-rotate.js',
  'floating-icons.js',
  'hub-float.js',
  'cursor-trail.js',
  'app.js',

  // Images
  'character-1.png',
  'character-2.png',
  'character-3.png',
  'character-4.png',
  'tools-header.png',
  'icon-logo.png',

  // Fonts
  'fonts/AwesomeSerif-LightRegular.woff2',
  'fonts/AwesomeSerif-Regular.woff2',
  'fonts/AwesomeSerif-MediumRegular.woff2',
  'fonts/AwesomeSerif-BoldRegular.woff2',
  'fonts/trip-sans.woff2',
  'fonts/trip-sans-medium.woff2',
  'fonts/trip-sans-bold.woff2',
  'fonts/trip-sans-ultra.woff2',
  'fonts/trip-sans-mono-regular.woff2',

  // Tools
  'tool-partnerships-calculator.html',
  'tool-palette-generator.html',
  'tool-qr-generator.html',
  'tool-cvg.html',
  'tool-content-plan.html',
  'tool-typeface-picker.html',
  'tool-visual-identity-formula.html',
  'tool-palette-collection.html',
  'tool-contrast-checker.html',
  'tool-color-converter.html',
  'tool-glyph-browser.html',
  'tool-bio-optimizer.html',
  'tool-background-remover.html',
  'tool-svg-optimizer.html',
  'tool-image-converter.html',
  'tool-image-tracer.html',
  'tool-pdf-preflight.html'
];

async function downloadFile(resource) {
  const url = `${BASE_URL}${resource}`;
  const destPath = path.join(TARGET_DIR, resource);

  // Ensure directory exists
  fs.mkdirSync(path.dirname(destPath), { recursive: true });

  console.log(`Downloading ${url} -> ${destPath}...`);

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    // Check if the response is binary or text
    const buffer = Buffer.from(await response.arrayBuffer());
    fs.writeFileSync(destPath, buffer);
    console.log(`Successfully saved ${resource}`);
  } catch (error) {
    console.error(`Failed to download ${resource}:`, error.message);
  }
}

async function run() {
  console.log(`Starting download mirror to ${TARGET_DIR}...`);
  for (const resource of RESOURCES) {
    await downloadFile(resource);
    // Add small delay to avoid hitting request limits
    await new Promise((resolve) => setTimeout(resolve, 300));
  }
  console.log('All downloads completed!');
}

run();
