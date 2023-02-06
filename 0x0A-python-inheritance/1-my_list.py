#!/usr/bin/python3
"""
has a subclass
"""


class Mylist(list):
    """child class of list"""
    def __init__(self):
        """initialises an object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
