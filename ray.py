from vec3 import vec3
from colour import colour

class ray(vec3):
    def __init__(self, o, d):
        assert type(o) == vec3 and type(d) == vec3
        self.origin = o
        self.direction = d

    def __call__(self, t):
        assert type(t) == float or type(t) == int
        return self.origin + self.direction*t

    def unit_direction(self):
        return self.direction.unit_vec()
