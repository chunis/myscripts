#!/usr/bin/python

import sys

count = {}
f = open(sys.argv[1])
for x in f:
        for w in x.split():
                if not w in count:
                        count[w] = 1
                else:
                        count[w] += 1

for x in count:
        print x, '==>', count[x]
