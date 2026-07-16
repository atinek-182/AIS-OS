const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;
const PUBLIC_DIR = path.join(__dirname, '..', 'second-brain-zorixel', 'wiki', 'research', 'jordan-watkins-reference');

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
  // Strip query parameters (e.g., ?v=2)
  filePath = filePath.split('?')[0];
  
  const absolutePath = path.join(PUBLIC_DIR, filePath);

  // Security check: ensure path is inside public dir
  if (!absolutePath.startsWith(PUBLIC_DIR)) {
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
