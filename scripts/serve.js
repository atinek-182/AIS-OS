const http = require('http');
const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = process.argv[2] 
  ? path.resolve(process.argv[2]) 
  : path.join(__dirname, '..', 'second-brain-zorixel', 'wiki', 'research', 'seo-audit-reference'); // Fallback to renamed folder or default
const PORT = process.argv[3] ? parseInt(process.argv[3], 10) : 3000;

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.woff2': 'font/woff2',
  '.json': 'application/json',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  console.log(`${req.method} ${req.url}`);

  // Default to index.html
  let filePath = req.url === '/' ? '/index.html' : req.url;
  // Strip query parameters
  filePath = filePath.split('?')[0];
  
  // Resolve path safely
  const absolutePath = path.resolve(PUBLIC_DIR, filePath.startsWith('/') ? filePath.slice(1) : filePath);

  // Security check: ensure path is inside public dir
  const relative = path.relative(PUBLIC_DIR, absolutePath);
  const isSafe = !relative.startsWith('..') && !path.isAbsolute(relative);
  if (!isSafe && absolutePath !== PUBLIC_DIR) {
    res.statusCode = 403;
    res.end('Access Denied');
    return;
  }

  fs.readFile(absolutePath, (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.statusCode = 404;
        res.end('Not Found');
      } else {
        res.statusCode = 500;
        res.end('Internal Server Error');
      }
      return;
    }

    const ext = path.extname(absolutePath).toLowerCase();
    res.setHeader('Content-Type', MIME_TYPES[ext] || 'application/octet-stream');
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}/`);
  console.log(`Serving files from: ${PUBLIC_DIR}`);
});
