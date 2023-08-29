#!/usr/bin/python3

"""classes that define a square size"""


class Square:
    """initialize the square object."""

    def __init__(self, size=0):
        """Initialize a new square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the square of an object."""
        return (self.__size * self.__size)
