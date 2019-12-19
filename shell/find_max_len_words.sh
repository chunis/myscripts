#!/bin/sh

# Chunis Deng (chunchengfh@gmail.com)
#
# About: Find the longest names from your source code in an ugly but workable way


find_cmd=`find . -name '*.[ch]pp'`  # You may need to change this
tmpf=`tempfile`
tmppy=${tmpf}x.py

echo "$find_cmd" | while read f; do cat $f; done \
	| sed 's/[ :<>,{}\.\*\(\);"]/ /g' \
	| sed "s#[/'-=\!&]# #g" \
	| sed 's/[][]/ /g' > $tmpf

cat > $tmppy <<HERE
#!/usr/bin/python

import sys

if len(sys.argv) >= 3:
    #print sys.argv
    cnt = int(sys.argv[2])
else:
    cnt = 10

dic = {}
for x in open(sys.argv[1]):
    for y in x.split():
        if y not in dic:
            dic[y] = len(y)

values = dic.values()
values = list(set(values))
values.sort()
v = values[-cnt:]
print v

for x in dic:
    if dic[x] in v:
        print dic[x], ":", x
HERE

python $tmppy $tmpf 12
rm -f $tmpf $tmppy
