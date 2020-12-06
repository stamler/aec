#!/usr/bin/env python3

# Zip a folder
# requires python > 3.6 for types
import sys
import os
import datetime
import shutil
import hashlib
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

# zip the folder to a file
now = datetime.datetime.now(tz=datetime.timezone.utc)
timestamp: str = now.strftime('%Y-%m-%d_%H:%M:%SUTC')
output_filename: str = f"aec_uploads_{ timestamp }" 
shutil.make_archive(output_filename, 'zip', dir_name)

# calculate checksum and include in the filename so that 
# the integrity of transfers can be verified easily
m = hashlib.sha256()
with open(f"{output_filename}.zip", 'rb') as f:
    while True:
        data = f.read(BUFFER_SIZE)
        if not data:
            break
        m.update(data)
final_name = f"{output_filename}_{m.hexdigest()}.zip"
os.rename(f"{output_filename}.zip", final_name)
print (f"Created {final_name}")


# TODO: delete older backups beyond a certain number
