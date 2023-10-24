#!/usr/bin/python3
"""Definition of class Square."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructs a new Square.

        Parameters:
            size (int): The dimension of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter and setter for the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(num) is int for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
            print()

    def __str__(self):
        """Defines the print() representation of a Square."""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]
        for _ in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            result += "\n"
        return result.rstrip("\n")
