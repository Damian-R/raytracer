from vec3 import vec3
from math import sqrt

class colour(vec3):
    def __init__(self, vals=[0, 0, 0]):
        if type(vals) == list:
            super().__init__(vals)
        elif type(vals) == vec3:
            self._v = vals._v
        else:
            raise 'Colour must be initalized with vec3 or list'

    def r(self):
        return self[0]

    def g(self):
        return self[1]
    
    def b(self):
        return self[2]

    def write_colour(self, samples_per_pixel):
        scale = 1.0 / samples_per_pixel # antialiasing setting
        r = int(256 * sqrt(self.r() * scale))
        g = int(256 * sqrt(self.g() * scale))
        b = int(256 * sqrt(self.b() * scale))

        print('{} {} {}'.format(min(r, 256), min(g, 256), min(b, 256)))

