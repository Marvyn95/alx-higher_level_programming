#!/usr/bin/python3
"""integer adition"""


def add_integer(a, b=98):
    """return addition of two numbers

    Raises:
        TypeError: if a or b arent integersand not floats
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
