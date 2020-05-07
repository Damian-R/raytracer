from vec3 import vec3

class hit_record:
    def __init__(self, p, norm, t):
        self.p = p
        self.norm = norm
        self.t = t


class hittable(vec3):
    def hit(self, ray, min_t, max_t, hr):
        raise NotImplementedError
