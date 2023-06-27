#!/usr/bin/python3

""" class Square defines a square based on 0-square.py)"""


class Square:
    """
    Private instance attribute: size
    """
    def __init__(self, size):
        """
        Instantiation with size (no type/value verification)
        """
        self.__size = size
