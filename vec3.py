import random
from math import sqrt, pi, cos, sin

class vec3:
    def __init__(self, vals=[0, 0, 0]):
        assert type(vals) == list and len(vals) == 3
        self._v = vals

    def __getitem__(self, i):
        assert i >= 0 and i <= 3
        return self._v[i]

    def __add__(self, other):
        assert issubclass(type(other), vec3)
        return vec3([self._v[0] + other._v[0], self._v[1] + other._v[1], self._v[2] + other._v[2]])

    def __sub__(self, other):
        assert issubclass(type(other), vec3)
        return vec3([self._v[0] - other._v[0], self._v[1] - other._v[1], self._v[2] - other._v[2]])
    
    def __truediv__(self, other):
        assert type(other) == int or type(other) == float
        return self * (1/other)
    
    def __mul__(self, other):
        assert type(other) == int or type(other) == float
        return vec3([self._v[0] * other, self._v[1] * other, self._v[2] * other])

    def __neg__(self):
        return self * -1

    def length(self):
        return sqrt(self._v[0]**2 + self._v[1]**2 + self._v[2]**2)

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
        return self._v[0]*other._v[0] + self._v[1]*other._v[1] + self._v[2]*other._v[2]

    def unit_vec(self):
        return self / self.length()

    @staticmethod
    def random(v_min, v_max):
        return vec3([ random.uniform(v_min, v_max), random.uniform(v_min, v_max), random.uniform(v_min, v_max) ])

    @staticmethod
    def random_in_unit_sphere():
        a = random.uniform(0, 2*pi)
        z = random.uniform(-1, 1)
        r = sqrt(1 - z**2)
        return vec3([ r*cos(a), r*sin(a), z ])

