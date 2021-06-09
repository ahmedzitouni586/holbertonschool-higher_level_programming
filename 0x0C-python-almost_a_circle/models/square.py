#!/usr/bin/python3
"""module to define rectangle class"""


from rectangle import Rectangle


class Square(Rectangle):
    """ define square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ square class """
        super().__init__(id, size, x, y)

    def __str__(self):
        """ return square details """
        S = "[Square]"
        S += "({}) {}/{}".format(self.id, self.__x, self.__y)
        S += " - {}".format(self.__width)
        return S
