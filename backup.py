#!/usr/bin/env python3

# Zip a folder
# requires python > 3.6 for types
import sys
import os
import datetime
import shutil
import hashlib
BUFFER_SIZE = 65536 

if len(sys.argv) != 2:
  print ("\nUsage: backup.py <dirname>\n")
  exit()

dir_name: str = sys.argv[1]

# check if dir_name is a directory
if not os.path.isdir(dir_name):
  print ("The provided argument is not a directory")
  exit()

output_filename: str = f"aec_uploads_{ datetime.datetime.now(tz=datetime.timezone.utc).strftime('%Y-%m-%d_%H:%M:%SUTC') }" 
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
