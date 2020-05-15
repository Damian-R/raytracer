import sys
import random
from ray import ray
from vec3 import vec3
from tqdm import tqdm
from hittable import hittable
from colour import colour

class scene:
    def __init__(self, camera):
        self.cam = camera
        self.objects = []
        self.max_depth = 50 
    
    def add_object(self, obj):
        assert issubclass(type(obj), hittable)
        self.objects.append(obj)

    def background(self, ray):
        unit_dir = ray.unit_direction()
        
        t = 0.5*(unit_dir.y() + 1.0) # scale y direction to [0, 1.0]
        white_grad = vec3([1, 1, 1])*t
        blue_grad = vec3([0.5, 0.7, 1.0])*(1.0 - t)
        return white_grad + blue_grad # linear interpolation blue/white

    def get_closest_obj_intersection(self, ray):
        closest_object = float('inf')
        closest_rec = None

        for obj in self.objects:
            hit_rec = obj.hit(ray, t_min=0.0001, t_max=closest_object)
            if hit_rec:
                closest_object = hit_rec.t
                closest_rec = hit_rec
        return closest_rec

    def get_ray_colour(self, r, rem_depth):
        if rem_depth == 0:
            return colour([0, 0, 0])

        closest_object = self.get_closest_obj_intersection(r)

        if closest_object:
            scattered_rec = closest_object.mat.scatter(r, closest_object)
            if scattered_rec:
                return colour(scattered_rec.colour * self.get_ray_colour(scattered_rec.scattered, rem_depth-1))
            return colour([0, 0, 0])

        return self.background(r)
    
    def random(self):
        if self.cam.samples_per_pixel > 1:
            return random.random()
        else:
            return 0

    def draw_scene(self):
        for i in tqdm(range(self.cam.height)):
            for j in range(self.cam.width):
                pixel = vec3([0, 0, 0])
                for s in range(self.cam.samples_per_pixel):
                    u = (j + self.random()) / (self.cam.width-1)
                    v = (self.cam.height - i + self.random()) / (self.cam.height-1)
                    r = self.cam.get_ray(u, v) 

                    pixel += self.get_ray_colour(r, self.max_depth)
                colour(pixel).write_colour(self.cam.samples_per_pixel)



