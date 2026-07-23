import os
import sys
import time
import subprocess
import threading
import http.server
import socketserver
from playwright.sync_api import sync_playwright

PORT = 8082
BASE_DIR = "./web-optimizer" if os.path.exists("./web-optimizer") else "."
SITE_DIR = os.path.join(BASE_DIR, "target_site")
RESULTS_PATH = os.path.join(BASE_DIR, "results.tsv")

class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def start_server(httpd):
    httpd.serve_forever()

def benchmark_page_load(url):
    runs = 10
    durations = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for i in range(runs):
            page = browser.new_page()
            
            # Direct measurement of navigation performance
            start_time = time.perf_counter()
            page.goto(url, wait_until="load")
            duration_ms = (time.perf_counter() - start_time) * 1000
            
            durations.append(duration_ms)
            page.close()
        browser.close()
        
    # Sort and return the median load time
    durations.sort()
    median_time = durations[runs // 2]
    return median_time

def main():
    # 1. Run train.py to generate minified page index.min.html
    train_script = "./web-optimizer/train.py" if os.path.exists("./web-optimizer/train.py") else "./train.py"
    subprocess.run(["python", train_script], check=True)
    
    # 2. Start HTTP server inside target_site folder
    original_cwd = os.getcwd()
    os.chdir(SITE_DIR)
    
    handler = SilentHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    server_thread = threading.Thread(target=start_server, args=(httpd,))
    server_thread.daemon = True
    server_thread.start()
    
    print("Serving target site for load-time benchmarking...")
    time.sleep(1) # Wait for server to bind
    
    try:
        # Check size of output asset
        minified_file = "index.min.html"
        if not os.path.exists(minified_file):
            print("ERROR: index.min.html not found.")
            file_size_bytes = 100000 # Penalty size
        else:
            file_size_bytes = os.path.getsize(minified_file)
            
        # Benchmark median load time
        url = f"http://localhost:{PORT}/index.min.html"
        median_load_time_ms = benchmark_page_load(url)
        
        # 3. Calculate Performance Score (lower size and load times = higher score)
        # Baseline score starts at 2000. We deduct points for size and load time.
        # Deduct 1 point per 2ms of load time, and 1 point per 5 bytes.
        size_penalty = file_size_bytes // 5
        speed_penalty = int(median_load_time_ms // 2)
        score = max(1, 2000 - size_penalty - speed_penalty)
        
        print(f"\n--- Benchmark Results ---")
        print(f"Median Load Time: {median_load_time_ms:.2f} ms")
        print(f"Minified File Size: {file_size_bytes} bytes")
        print(f"Combined Score: {score}/2000")
        
        # Write results
        with open("../results.tsv", "a") as f:
            f.write(f"{int(time.time())}\t{score}\t2000\n")
            
    except Exception as e:
        print(f"Benchmarking Error: {str(e)}")
        score = 0
    finally:
        # Stop local server and restore working directory
        httpd.shutdown()
        httpd.server_close()
        os.chdir(original_cwd)
        
    print(f"Web speed evaluation complete. Score logged: {score}/2000")

if __name__ == "__main__":
    main()
