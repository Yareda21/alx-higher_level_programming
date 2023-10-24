#!/usr/bin/python3
"""Definition of class Square."""


class Square:
    """A class that represents a square."""

    def __init__(self, size):
        """Constructs a new Square.

        Parameters:
            size (int): The dimension of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter for the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the # character."""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
