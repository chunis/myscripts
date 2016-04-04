#!/usr/bin/python

# Chunis Deng (chunchengfh@gmail.com)
#
# About: This script can convert a single .webp file to jpg format
# Require: Under Linux, needs libwebp and PIL.
# Install: # apt-get install libwebp-dev; pip install pillow
#
# To convert all files under a folder, first 'cd folder', then run:
#       $ for f in `/bin/ls`; do ./test.py $f; done


import sys
from PIL import Image

oldname = sys.argv[1]
newname = oldname.replace('webp', 'jpg')
print "convert: %s --> %s" %(oldname, newname)

im = Image.open(oldname).convert('RGB')
im.save(newname, 'jpeg')
