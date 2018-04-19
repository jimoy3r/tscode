#! /usr/bin/env python
"""
Given a circular list of numbers which is constantly increasing
but you don't know where the list begins (ie: 42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21),
find the smallest number in the list.
Program is extendible and flexible as possible.
"""
from circlist import CircList

cl = CircList([42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21])
print "smallest={}".format(cl.min())

