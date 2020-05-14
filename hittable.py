from vec3 import vec3

class hit_record:
    def __init__(self, p, norm, t):
        self.p = p
        self.norm = norm.unit_vec()
        self.t = t
    
    def set_intersection_direction(self, ray):
        if ray.direction.dot(self.norm) < 0:
            self.front_face = True
        else:
            self.front_face = False
            self.norm = -self.norm


class hittable(vec3):
    def hit(self, ray, t_min, t_max, hr):
        raise NotImplementedError
