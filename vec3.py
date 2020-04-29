import numpy as np
from math import sqrt

class vec3:
    def __init__(self, vals=[0, 0, 0]):
        assert len(vals) == 3
        self._v = np.array(vals)

    def __getitem__(self, i):
        assert i >= 0 and i <= 3
        return self._v[i]

    def __add__(self, other):
        assert type(other) == vec3
        return vec3(self._v + other._v)
    
    def __div__(self, other):
        assert type(other) == int or type(other) == float
        return vec3(self._v / other)

    def __mul__(self, other):
        assert type(other) == int or type(other) == float
        return vec3(self._v * other)

    def __str__(self):
        return str(self._v)

    def length(self):
        return sqrt(np.sum(np.square(self._v)).item())

    def x(self):
        return self[0]

    def y(self):
        return self[1]

    def z(self):
        return self[2]

    def unit_vec(self):
        return vec3(self._v / self.length())
