#!/usr/bin/python3
""" define a square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size)

    @property
    def size(self):
        """getter"""
        return self.size

    @size.setter
    def size(self, size):
        """setter"""
        self.width = size
        self.height = size

    def __str___(self):
        return "[Square] {} {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Assigns a key/value argument to each attribute """
        if len(args):
            i = 1
            for value in args:
                if i == 1:
                    self.id = value
                if i == 2:
                    self.size = value
                if i == 3:
                    self.x = value
                if i == 4:
                    self.y = value
                i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}