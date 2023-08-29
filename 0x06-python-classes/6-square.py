#!/usr/bin/python3

"""classes that define the size of a square."""


class Square:
    """classes that define the size of as square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of a square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """it returns the size of a square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of a value."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the cureent square value of an object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the # charecter according to the size of the value."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
