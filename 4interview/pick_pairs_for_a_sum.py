#!/usr/bin/python

# Chunis Deng (chunchengfh@gmail.com)
# About:
#   a set contains some numbers. Pick all pairs whose sum equals to SUM.

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import random

SUM = 40

BEGIN = -5
END = 50
NUM = 30

# very strange, below statement produces a set with elements sorted
# but it won't impact our implementation
nums = {random.randint(BEGIN, END) for x in range(NUM)}
print "The set contains these numbers:"
for x in nums: print x,
print

mydic = {x:SUM-x for x in nums}
resultdic = {}
# for (k, v) in mydic: print k, ',', v

for k in nums:
    if mydic[k] in nums:
        if k != mydic[k]:  # let's skip pair like 'X, X'
            resultdic[k] = mydic[k]
            #print "pair: %d, %d" %(k, mydic[k])

# if we don't care pairs like (A, B) and (B, A) both included, below is enough:
print "\nAll pairs, both (A, B) and (B, A) are included:"
for k in resultdic:
    print "%d, %d" %(k, resultdic[k])
print

# there are even elements in resultdic. We just need the first half
sorted_k = sorted(resultdic.keys())
half_k = sorted_k[:len(sorted_k)/2]
print "All keys sorted:", sorted_k
print "The smaller halp keys:", half_k
print "Now we've discarded the duplicate pairs:"
for k in half_k:
    print "%d, %d" %(k, resultdic[k])

