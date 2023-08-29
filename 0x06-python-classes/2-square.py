#!/usr/bin/python3
"""a square that defines an object by its size
"""


class Square;
    """ classes that define a square by its size
    """
    def __init__(self, size = 0):
        """initialize the square object
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("Size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("Size must be an integer")
