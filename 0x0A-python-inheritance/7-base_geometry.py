#!/usr/bin/python3
""" Write an empty class BaseGeometry. """


class BaseGeometry:
    """ an empty class for the task """
    def area(self):
        """ area() is not implemented """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ def integer_validator(self, name, value): """
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be an integer")
