import numpy as np

class vec:
    def __init__(self, vals=[0, 0, 0]):
        assert len(vals) == 3
        self._v = np.array(vals)

    def __getitem__(self, i):
        assert i >= 0 and i <= 3
        return self._v[i]

    def __add__(self, other):
        assert type(other) == vec
        return self._v + other._v
    
    def __str__(self):
        return str(self._v)
