#!/usr/bin/python3
class Base:
    """Base class for all other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
