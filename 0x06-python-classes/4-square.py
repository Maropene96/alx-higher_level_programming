#!/usr/bin/python3

"""Classes that define the size of a square.
"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """It initializes the size of a square object
        """
        self.size = size

    @property
    def size(self):
        """it returns the value of a square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """it returns the now size of a square object"""
        return (self.__size * self.__size)
