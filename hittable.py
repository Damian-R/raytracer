from vec3 import vec3

class hittable(vec3):
    def hit(self):
        raise NotImplementedError
