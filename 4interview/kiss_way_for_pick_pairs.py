#!/usr/bin/python

# Chunis Deng (chunchengfh@gmail.com)
# About:
#   a set contains some numbers. Pick all pairs whose sum equals to SUM.
#   At first we sort the list, then we walk from 2 ends to the center.
#   It's very simple and stupid, because since we sort the list first,
#   it's not a good idea for large list. Check 'pick_pairs_for_a_sum.py'
#   for a better way to do it using dict.

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

# to sort a large list is very stupid
nums = sorted(list(nums))
print "Sorted nums:"
for x in nums: print x,
print

si = 0  # start index
ei = len(nums)-1  # end index
while True:
    if si >= ei:
        break

    s = nums[si]
    e = nums[ei]
    sum = s + e

    if sum == SUM:
        print "%d, %d" %(s, e)
        si += 1
        ei -= 1
    elif sum < SUM:
        si += 1
    elif sum > SUM:
        ei -= 1

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
