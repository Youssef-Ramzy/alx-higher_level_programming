#!/usr/bin/python3
""" This is a models base.py for this project """


class Base:
    """This is the base class for all objects in the project.

    Attributes:
        __nb_objects (int): The number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int): The ID of the object (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
