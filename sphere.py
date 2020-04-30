from hittable import hittable

class sphere(hittable):
    def __init__(self, vals=[0, 0, 0], r=0):
        super().__init__(vals)
        self.r = r

    def hit(self, ray):
        origin_to_center = ray.origin - self

        a = ray.direction.dot(ray.direction)
        b = 2.0 * ray.direction.dot(origin_to_center)
        c = origin_to_center.dot(origin_to_center) - self.r ** 2

        discriminant = b*b - 4*a*c
        return discriminant > 0
