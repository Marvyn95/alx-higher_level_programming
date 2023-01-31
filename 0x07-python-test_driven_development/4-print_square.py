#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """prints a square with #

    Args:
        size (int): square edges length
    Raises:
        TypeError: if size aint integer
        ValueError: if value is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
