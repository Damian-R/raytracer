import numpy as np
import random
from math import sqrt, pi, cos, sin

class vec3:
    def __init__(self, vals=[0, 0, 0]):
        assert len(vals) == 3
        self._v = np.array(vals)

    def __getitem__(self, i):
        assert i >= 0 and i <= 3
        return self._v[i].item()

    def __add__(self, other):
        assert type(other) == vec3
        return vec3(self._v + other._v)

    def __sub__(self, other):
        assert issubclass(type(other), vec3)
        return vec3(self._v - other._v)
    
    def __truediv__(self, other):
        assert type(other) == int or type(other) == float
        return vec3(self._v / other)

    def __mul__(self, other):
        assert type(other) == int or type(other) == float
        return vec3(self._v * other)

    def __str__(self):
        return str(self._v)

    def __neg__(self):
        return vec3(self._v * -1)

    def length(self):
        return sqrt(np.sum(np.square(self._v)).item())

    def length_sq(self):
        return self.length()**2

    def x(self):
        return self[0]

    def y(self):
        return self[1]

    def z(self):
        return self[2]

    def dot(self, other):
        assert type(other) == vec3
        return np.dot(self._v, other._v)

    def unit_vec(self):
        return vec3(self._v / self.length())

    @staticmethod
    def random(v_min, v_max):
        return vec3([ random.uniform(v_min, v_max), random.uniform(v_min, v_max), random.uniform(v_min, v_max) ])

    @staticmethod
    def random_in_unit_sphere():
        a = random.uniform(0, 2*pi)
        z = random.uniform(-1, 1)
        r = sqrt(1 - z**2)
        return vec3([ r*cos(a), r*sin(a), z ])

