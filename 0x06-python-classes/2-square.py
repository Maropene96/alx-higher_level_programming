#!/usr/bin/python3
"""classes that defines the square of object"""


class Square:
    """ Classes that defines the square of an object
    """
    def __init__(self, size=0):
        """initializes the size of a square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
