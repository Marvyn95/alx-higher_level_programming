
#!/usr/bin/python3
"""defines rectangle"""


class Rectangle:
    """this is a rectangle"""

    number_of_instances = 0

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

