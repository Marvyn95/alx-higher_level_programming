#!/usr/bin/python3
"""prints my name"""


def say_my_name(first_name, last_name):
    """prints your name

    Args:
    first_name (str): first name
    last_name (str): last name

    Raise:
        TypeError: if args areant strigs
    Returns: a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
