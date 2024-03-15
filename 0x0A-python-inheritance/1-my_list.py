#!/usr/bin/python3
""" Module that contains a class MyList that inherits from list """


class Mylist(list):
    """ class that inherate from list """
    def print_sorted(self):
        """ method that print lists in sorted """
        print(sorted(self))
