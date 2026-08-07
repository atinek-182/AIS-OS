import site
import os

print("User site packages:", site.getusersitepackages())
print("Site packages:", site.getsitepackages())

for path in site.getsitepackages() + [site.getusersitepackages()]:
    if os.path.exists(path):
        print(f"\nListing {path}:")
        items = os.listdir(path)
        for i in sorted(items):
            if any(term in i.lower() for term in ['whisper', 'ffmpeg', 'torch', 'imageio']):
                print("  -", i)
