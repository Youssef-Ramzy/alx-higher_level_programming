#!/usr/bin/python3
"""Square class with size"""


class Square:
    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
