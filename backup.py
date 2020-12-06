#!/usr/bin/env python3

# Zip a folder 
import sys
import os
import datetime
import shutil

if len(sys.argv) != 2:
  print ("\nUsage: backup.py <dirname>\n")

dir_name: str = sys.argv[1]

# check if dir_name is a directory
if not os.path.isdir(dir_name):
  print ("The provided argument is not a directory")

output_filename: str = f"aec_uploads_{ datetime.datetime.now(tz=datetime.timezone.utc).strftime('%Y-%m-%d_%H:%M:%SUTC') }" 
shutil.make_archive(output_filename, 'zip', dir_name)
# TODO: calculate checksum and include it in the filename
# TODO: delete older backups beyond a certain number
print (f"Created {output_filename}")
