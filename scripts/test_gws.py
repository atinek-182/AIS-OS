import subprocess
import json
import sys

def main():
    print("Testing gws CLI execution...")
    # Test simple gws drive files list
    res = subprocess.run(["gws", "drive", "files", "list", "--params", "{\"pageSize\": 2}"], shell=True, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    print("Return code:", res.returncode)

if __name__ == "__main__":
    main()
