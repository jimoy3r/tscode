#! /usr/bin/env python
"""
Purpose: circlist.py contains class definition for working with a circular list
Author: Jim Moyer
"""
from itertools import cycle


class CircList:
    """ Class for Circular linked List """

    def __init__(self, vals):
        """
        Initialize the Circular List
        :param vals: data values for list
        """
        self.size = len(vals)
        self.circ_list = cycle(vals)

    def min(self):
        """
        Return the min value in this circular list
        :return smallest: the minimum value found
        """
        smallest = next(self.circ_list)
        for index in xrange(self.size-1):
            item = next(self.circ_list)
            if item < smallest:
                smallest = item
        return smallest

