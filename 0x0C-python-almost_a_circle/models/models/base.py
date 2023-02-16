#!/usr/bin/python3
"defines a base class"

class Base:
    """a base class model

    Attributes:
    __nb_objects (int): number of object instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new base
        
        Args:
        id (int): identity of new instance for this class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_ibjects += 1
            self.id = Base.__nb_objects