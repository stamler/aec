#!/usr/bin/env python3

# Zip a folder
# requires python >= 3.6 for type annotations
import sys
import os
import datetime
import shutil
import hashlib
import glob
from typing import List
BUFFER_SIZE: int = 65536

# Exit if the number of arguments is invalid
if len(sys.argv) != 2:
  print ("\nUsage: backup.py <dirname>\n")
  exit()

# Get the argument for the folder to zip
dir_name: str = sys.argv[1]

# Exit if dir_name is not a directory
if not os.path.isdir(dir_name):
  print ("The provided argument is not a directory")
  exit()

# get the absolute path of the input folder
source = os.path.abspath(dir_name)

# Go up one level
root_dir = os.path.abspath(os.path.join(source,".."))
base_dir = os.path.relpath(source, root_dir)

# zip the folder to a file
now: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)
timestamp: str = now.strftime('%Y-%m-%d_%H:%M:%SUTC')
output_filename: str = f"aec_uploads_{ timestamp }"
print("creating archive...")
shutil.make_archive(output_filename, 'gztar', root_dir, base_dir)

# calculate checksum and include in the filename so that 
# the integrity of transfers can be verified easily
m = hashlib.sha256()
with open(f"{output_filename}.tar.gz", "rb") as f:
    while True:
        data = f.read(BUFFER_SIZE)
        if not data:
            break
        m.update(data)
final_name = f"{output_filename}_{m.hexdigest()}.tar.gz"
os.rename(f"{output_filename}.tar.gz", final_name)
print (f"Created {final_name}")

# keep only the 3 newest archives
archives: List[str] = glob.glob("./aec_uploads_*.tar.gz")
archives.sort() # ascending by date, otherwise reverse=True
for x in archives[:-3]:
  os.remove(x)
