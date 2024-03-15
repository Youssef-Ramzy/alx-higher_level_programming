#!/usr/bin/python3
""" 
This module contains a class MyList that inherits from the built-in list class in Python.
"""

class Mylist(list):
    """ 
    This class inherits from the built-in list class in Python. 
    It has an additional method print_sorted.
    """
    def print_sorted(self):
        """ 
        This method prints the elements of the MyList instance sorted in ascending order.
        It uses the built-in sorted function in Python which returns a new sorted list 
        and leaves the original list unaffected.
        """
        print(sorted(self))
