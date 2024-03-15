#!/usr/bin/python3
""" module for the 2-is_same_class.py """


def is_same_class(obj, a_class):
    """ method check if the obj is in the class """
    if type(obj) == a_class:
        return True
    else:
        return False
