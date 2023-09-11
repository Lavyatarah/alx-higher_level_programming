#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
<<<<<<< HEAD
        self.__size = size
=======
        self.__size = size
>>>>>>> 53ceee224eea9badc22325c09efb0bb2e857c357
