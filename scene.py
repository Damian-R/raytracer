from ray import ray
from vec3 import vec3
from tqdm import tqdm

class scene:
    def __init__(self, camera):
        self.cam = camera
        self.objects = []
    
    def add_object(self, obj):
        self.objects += obj

    def draw_scene(self):
        for i in tqdm(range(self.cam.height)):
            for j in range(self.cam.width):
                u = (self.cam.width - i) / self.cam.width
                v = j / self.cam.height
                r = ray(self.cam.origin, self.cam.screen['ll_corner'] + self.cam.screen['hor']*u + self.cam.screen['vert']*v)

                colour = r.calc_colour()
                colour.write_colour()
