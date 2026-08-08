import shutil
import os

target = r"d:\AI-OS\brain-aios\wiki\research\skills-library\mattpocock-skills"
if os.path.exists(target):
    shutil.rmtree(target)
    print("SUCCESS: Deleted " + target)
else:
    print("ALREADY_DELETED: " + target)
