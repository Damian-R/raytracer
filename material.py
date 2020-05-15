from ray import ray
from hittable import hit_record
from colour import colour
from vec3 import vec3

class material:
    def scatter(self, r: ray, hit_rec: hit_record, attenuation: colour) -> dict:
        raise NotImplementedError

class diffuse(material):
    def __init__(self, col: colour):
        self.attenuation = col

    def scatter(self, r: ray, hit_rec: hit_record) -> hit_record:
        scattered_dir = hit_rec.norm + vec3.random_in_unit_sphere()
        scattered = ray(hit_rec.p, scattered_dir)
        hit_rec.colour = self.attenuation
        hit_rec.scattered = scattered
        return hit_rec

