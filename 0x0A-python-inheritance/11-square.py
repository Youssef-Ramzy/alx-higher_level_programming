#!/usr/bin/python3
""" Module for defining a Square class which inherits from Rectangle. """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
	""" 
	Square class that inherits from Rectangle.
	
	Attributes:
		__size (int): size of the square.
	"""
	
	def __init__(self, size):
		""" 
		Initialize Square instance with size. 
		
		Args:
			size (int): size of the square.
		"""
		self.integer_validator("size", size)
		self.__size = size

	def area(self):
		""" 
		Calculate and return the area of the square. 
		
		Returns:
			int: The area of the square.
		"""
		return (self.__size * self.__size)

	def __str__(self):
		""" 
		Define the print() representation of a Square instance. 
		
		Returns:
			str: A string representation of the square.
		"""
		return ("[Square] {}/{}".format(self.__size, self.__size))
