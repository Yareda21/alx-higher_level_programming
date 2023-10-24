#!/usr/bin/python3
"""Definition of class Square."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Constructs a new Square.

        Parameters:
            size (int): The dimension of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
