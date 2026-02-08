import shutil
import sys

usage = shutil.disk_usage("/")

free = usage.free / (1024**3)

print(f"Free Disk: {free:.2f} GB")

if free < 5:
    print("WARNING: Low disk space")
    sys.exit(1)import shutil
import sys
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("disk_check.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Starting disk space check...")

usage = shutil.disk_usage("/")
free = usage.free / (1024**3)

logging.info(f"Free Disk Space: {free:.2f} GB")

THRESHOLD = 5

if free < THRESHOLD:
    logging.error("Disk space below threshold! Failing the pipeline.")
    sys.exit(1)
else:
    logging.info("Disk space is healthy.")

else:
    print("Disk space is healthy")

