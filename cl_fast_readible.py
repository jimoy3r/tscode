#! /usr/bin/env python
"""
Given a circular list of numbers which is constantly increasing
but you don't know where the list begins (ie: 42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21),
find the smallest number in the list.
Program is readable and fast as possible.
"""
from itertools import cycle

# Define values for circular list
c = [42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21]
size = len(c)
circular_list = cycle(c)

# Find smallest value in it
smallest = next(circular_list)
for index in xrange(size-1):
    item = next(circular_list)
    if item < smallest:
        smallest = item

print "smallest={}".format(smallest)

