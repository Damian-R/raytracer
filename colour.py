from vec3 import vec3

class colour(vec3):
    def __init__(self, vals=[0, 0, 0]):
        if type(vals) == list:
            super().__init__(vals)
            self._v = self._v * 256
        elif type(vals) == vec3:
            self._v = vals._v * 256
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
        r = int(self.r() * scale)
        g = int(self.g() * scale)
        b = int(self.b() * scale)

        print('{} {} {}'.format(min(r, 256), min(g, 256), min(b, 256)))

