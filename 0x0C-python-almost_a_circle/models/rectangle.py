#!/usr/bin/ptyhon3
"""Rectangle module for the project"""
from base import Base


class Rectangle(Base):
    """Rectangle class for the project"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): The x coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute

        Args:
            value (int): The value to set the width attribute to
        """
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute

        Args:
            value (int): The value to set the height attribute to
        """
        self.__height = value
