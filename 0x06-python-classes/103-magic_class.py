#!/usr/bin/python3
"""classes that defines the magicclass"""

import math


class MagicClass:
    """classes that defines magicclass"""

    def __init__(self, radius=0):
        """Initializes the radius of a circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area a circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return the length of  circle"""
        return (2 * math.pi * self.__radius)
