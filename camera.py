from ray import ray
from vec3 import vec3

class camera:
    def __init__(self, width, height, samples_per_pixel, origin=[0, 0, 0]):
        self.width = width
        self.height = height
        self.origin = vec3(origin)
        self.samples_per_pixel = samples_per_pixel # antialiasing
        
        self.ll_corner = self.origin + vec3([-2, -1, -1])
        self.hor = vec3([4, 0, 0])
        self.vert = vec3([0, 2, 0])

    def get_ray(self, u, v):
        return ray(self.origin, self.ll_corner + self.hor*u + self.vert*v)
