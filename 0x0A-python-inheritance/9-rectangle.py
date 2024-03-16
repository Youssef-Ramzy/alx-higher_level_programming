#!/usr/bin/python3
""" Write a class Rectangle that inherits from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class for the task """
    def __init__(self, width, height):
        """ instantiation with width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ returns the string representation of the rectangle """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
