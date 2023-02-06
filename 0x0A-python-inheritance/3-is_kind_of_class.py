#!/usr/bin/python3
"""checks if object is subclass """


def is_kind_of_class(obj, a_class):
    """checks if obj was inherited

    Args:
        obj (any): object to check
        a_class (type): class to match
    Returns:
        true or false
    """
    if isinstance(obj, a_class):
        return True
    return False
