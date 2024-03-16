#!/usr/bin/python3
""" Write an empty class BaseGeometry. """


class BaseGeometry:
    """ an empty class for the task """
    def area(self):
        """ area() is not implemented """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ def integer_validator(self, name, value): """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
