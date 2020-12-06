# Zip a folder 
import sys
import os
import datetime
import shutil

if len(sys.argv) == 2:
  dir_name = sys.argv[1]
  # check if dir_name is a directory
  if os.path.isdir(dir_name):
    output_filename = f"aec_uploads_{ datetime.datetime.now(tz=datetime.timezone.utc).strftime('%Y-%m-%d_%H:%M:%SUTC') }.zip" 
    shutil.make_archive(output_filename, 'zip', dir_name)
    print (f"Created {output_filename}")
  else:
    print ("The provided argument is not a directory")
else:
  print ("\nUsage:  python backup.py <dirname>\n")