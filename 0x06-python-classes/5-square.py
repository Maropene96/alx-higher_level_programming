#!/usr/bin/python3

"""classes that define a square object."""


class Square:
    """classes that define the square of an object ."""

    def __init__(self, size):
        """Initializes the  size of a square object
        """
        self.size = size

    @property
    def size(self):
        """returns the size of a square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square of an object."""
        return (self.__size * self.__size)

    def my_print(self):
        """It prints the charecter # according to its size ."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
