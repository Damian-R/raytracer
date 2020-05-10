import sys
from ray import ray
from vec3 import vec3
from tqdm import tqdm
from hittable import hittable
from colour import colour

class scene:
    def __init__(self, camera):
        self.cam = camera
        self.objects = []
    
    def add_object(self, obj):
        assert issubclass(type(obj), hittable)
        self.objects.append(obj)

    def background(self, ray):
        unit_dir = ray.unit_direction()
        
        t = 0.5*(unit_dir.y() + 1.0) # scale y direction to [0, 1.0]
        white_grad = vec3([1, 1, 1])*t
        blue_grad = vec3([0.5, 0.7, 1.0])*(1.0 - t)
        return colour(white_grad + blue_grad) # linear interpolation blue/white

    def get_closest_obj_intersection(self, ray):
        closest_object = float('inf')
        closest_rec = None

        for obj in self.objects:
            hit_rec = obj.hit(ray, t_min=0, t_max=closest_object)
            if hit_rec:
                closest_object = hit_rec.t
                closest_rec = hit_rec
        return closest_rec


    def get_ray_colour(self, ray):
        closest_object = self.get_closest_obj_intersection(ray)
         
        if closest_object:
            return colour((closest_object.norm + vec3([1, 1, 1]))*0.5)

        return self.background(ray)
        

    def draw_scene(self):
        for i in tqdm(range(self.cam.height)):
            for j in range(self.cam.width):
                u = (self.cam.width - j) / self.cam.width
                v = i / self.cam.height
                r = ray(self.cam.origin, self.cam.screen['ll_corner'] + self.cam.screen['hor']*u + self.cam.screen['vert']*v)

                colour = self.get_ray_colour(r)
                colour.write_colour()
