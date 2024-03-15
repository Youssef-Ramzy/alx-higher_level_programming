#!/usr/bin/python3
"""Module for lookup method"""


class Mylist(list):
    """ class that inherate from list """
    def print_sorted(self):
        """ method that print lists """
        print(sorted(self))
