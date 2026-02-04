import shutil
import sys

usage = shutil.disk_usage("/")

free = usage.free / (1024**3)

print(f"Free Disk: {free:.2f} GB")

if free < 5:
    print("WARNING: Low disk space")
    sys.exit(1)
else:
    print("Disk space is healthy")
