from vec3 import vec3
from colour import colour

class ray(vec3):
    def __init__(self, o, d):
        assert type(o) == vec3 and type(d) == vec3
        self.origin = o
        self.direction = d

    def __call__(self, t):
        assert type(t) == float
        return o + d*t

    def unit_direction(self):
        return self.direction.unit_vec()

    def calc_colour(self):
        unit_dir = self.unit_direction()
        t = 0.5*(unit_dir.y() + 1.0).item()
        white_grad = colour([1, 1, 1])*(1.0 - t)
        blue_grad = colour([0.5, 0.7, 1]) * t
        return colour(white_grad + blue_grad)
