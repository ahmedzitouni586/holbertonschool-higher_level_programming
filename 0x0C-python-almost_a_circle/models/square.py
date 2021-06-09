#!/usr/bin/python3
"""module to define rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ define square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ square constractor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return str() and print() representation of square object """
        S = "[Square]"
        S += "({}) {}/{}".format(self.id, self.x, self.y)
        S += " - {}".format(self.width)
        return S
