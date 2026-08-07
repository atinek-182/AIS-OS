import subprocess
import shutil

print("Node:", shutil.which("node"))
print("Python:", shutil.which("python"))

# Check playwright in python
try:
    import playwright
    print("Playwright Python: INSTALLED")
except ImportError:
    print("Playwright Python: NOT installed")

# Check node playwright
try:
    res = subprocess.run(["node", "-e", "console.log(require('playwright') ? 'Playwright Node INSTALLED' : 'NONE')"], capture_output=True, text=True, cwd=r"d:\AI-OS")
    print("Node Playwright check:", res.stdout.strip() or res.stderr.strip())
except Exception as e:
    print("Node Playwright error:", e)
