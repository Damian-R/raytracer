from vec import vec

class colour(vec):
    def __init__(self, vals=[0, 0, 0]):
        super().__init__(vals)
        self._v = (self._v * 256).astype(int)
    def write_colour(self):
        print('{} {} {}'.format(self[0], self[1], self[2]))

c = colour()
