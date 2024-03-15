#!/usr/bin/python3
""" module to check 4-inherits_from.py """


def inherits_from(obj, a_class):
    """ method to check if the obj is calss """

    return type(obj) != a_class and isinstance((obj), a_class)
