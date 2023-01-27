#!/usr/bin/python3
"""a class square"""


class Square:
    """this is a square"""

    def __init__(self, size=0):
        """initialize new square

        Args:
        size (int): size of new square
        """
        self.__size = size

    @property
    def size(self):
        """set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must bee >= 0")
        self.__size = value

    def area(self):
        """returns area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square using #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
