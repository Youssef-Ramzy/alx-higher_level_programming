#!/usr/bin/python3
""" This is a module for the square project. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id of the square.

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string representation of the square.

        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value
            self.__width = value
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.size = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.size = value
