#!/usr/bin/python
# -*- encoding: utf-8 -*-

#About: Randomly shuffle my newly collected words in a file named 'xxx.html', and save in file 'xxx-1.html'.
# The file has the format as below:
# <html><head><meta http-equiv="content-type" content="text/html;charset=UTF-8"/></head><body> <pre>
# envoie
# autour
# </pre> </body> </html>

# Chunis Deng (chunchengfh@gmail.com)


import random
import sys, os

fname = sys.argv[1]
base, ext = fname.split('.')[0:2]
newname = base + '-1.' + ext
print "save to file '%s'..." %newname
if os.path.exists(newname):
    print "Error. file '%s' exists already!" %newname
    sys.exit()

f = open(fname)
lines = f.readlines()

mylst = []
for ln in lines:
    line = ln.strip()
    if line.startswith('<'):
        continue
    if line.strip() == '':
        continue
    mylst.append(line)

random.shuffle(mylst)

f = open(newname, 'w')
f.write(lines[0])
f.write('\n')
f.write('\n'.join(mylst))
f.write('\n\n')
f.write(lines[-1])
print 'done'
