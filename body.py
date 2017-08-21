class Body(object):

    def __init__(self, x, y, char='#'):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coor(self):
        return self.x, self.y
