#!/usr/bin/python3
""" define a square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size)

    def __str___(self):
        return "[Square] {} {}/{} - {}".format(self.id, self.x, self.y, self.size)
