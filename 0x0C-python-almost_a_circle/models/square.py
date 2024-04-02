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
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
