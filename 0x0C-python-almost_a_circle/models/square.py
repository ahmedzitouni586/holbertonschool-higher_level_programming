#!/usr/bin/python3
"""module to define rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ define square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ square constractor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return square details """
        S = "[Square]"
        S += "({}) {}/{}".format(self.id, self.x, self.y)
        S += " - {}".format(self.width)
        return S

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, name):
        """ size setter """
        self.width = name
        self.height = name

    def update(self, *args, **kwargs):
        """ assign attributes to square class """
        if args and len(args) != 0:
            try:
                if args[0] != None:
                    self.id = args[0]
            except IndexError:
                return
            try:
                if args[1] != None:
                    self.size = args[1]
            except IndexError:
                return
            try:
                if args[2] != None:
                    self.x = args[2]
            except IndexError:
                return
            try:
                if args[3] != None:
                    self.y = args[3]
            except IndexError:
                return
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k  == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ dicionnary representaion of the square """
        s = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return s
