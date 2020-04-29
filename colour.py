from vec3 import vec3

class colour(vec3):
    def __init__(self, vals=[0, 0, 0]):
        if type(vals) == list:
            super().__init__(vals)
            self._v = (self._v * 256).astype(int)
        elif type(vals) == vec3:
            self._v = vals._v.astype(int)
        else:
            raise "Colours must be initialized with either a list or vec3"
    
    def r(self):
        return self[0]

    def g(self):
        return self[1]
    
    def b(self):
        return self[2]

    def write_colour(self):
        print('{} {} {}'.format(self.r(), self.g(), self.b()))
