from math import sqrt
from hittable import hittable, hit_record

class sphere(hittable):
    def __init__(self, vals=[0, 0, 0], r=0):
        super().__init__(vals)
        self.r = r

    def hit(self, ray, t_min=0, t_max=float('inf')):
        origin_to_center = ray.origin - self

        a = ray.direction.length_sq()
        h_b = ray.direction.dot(origin_to_center)
        c = origin_to_center.length_sq() - self.r ** 2

        discriminant = h_b*h_b - a*c
        if discriminant > 0:
            # one or two roots, return closest intersection to camera (first intersection)
            root1 = ((-h_b - sqrt(discriminant))/a).item()
            root2 = ((-h_b + sqrt(discriminant))/a).item()

            if root1 > t_min and root1 < t_max:
                hit_rec = hit_record(ray(root1), (ray(root1) - self) / self.r, root1)
                hit_rec.set_intersection_direction(ray)
                return hit_rec
            if root2 > t_min and root2 < t_max:
                hit_rec = hit_record(ray(root2), (ray(root2) - self) / self.r, root2)
                hit_rec.set_intersection_direction(ray)
                return hit_rec 
        else:
            # no roots, ray missed
            return False
