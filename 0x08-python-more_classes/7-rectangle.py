#!/usr/bin/python3
"""defines rectangle"""


class Rectangle:
    """this is a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """new triangle variables

        Args:
        width (int): rec width
        height (int): rec height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """gets rec width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets rec height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rec"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rec"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the rec with # printed"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """returns string rep of the rectangle"""
        rect = "Rectangle({}, {})".format(self.__width, self.__height)
        return (rect)

    def __del__(self):
        """prints message when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
