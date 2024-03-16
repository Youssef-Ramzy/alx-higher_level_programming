#!/usr/bin/python3
""" Write a class Rectangle that inherits from BaseGeometry. """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ a class for the task """
    def __init__(self, size):
        """ instantiation with size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return (self.__size * self.__size)

    def __str__(self):
        """ returns the string representation of the square """
        return ("[Square] {}/{}".format(self.__size, self.__size))
