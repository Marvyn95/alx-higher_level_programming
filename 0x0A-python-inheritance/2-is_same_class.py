#!/usr/bin/python3
"""defines a function that checks a class"""


def is_same_class(obj, a_class):
    """checks if object is in certain class

    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        True or False
"""

    if type(obj) == a_class:
        return True
    return False