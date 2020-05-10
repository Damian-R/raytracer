from tqdm import tqdm
from colour import colour
from camera import camera
from scene import scene
from sphere import sphere
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--width', type=int)
parser.add_argument('--height', type=int)
parser.add_argument('--spp', type=int) 

args = parser.parse_args()

CAM_WIDTH = args.width or 400
CAM_HEIGHT = args.height or 200
SAMPLES_PER_PIXEL = args.spp or 1

cam = camera(width=CAM_WIDTH, height=CAM_HEIGHT, samples_per_pixel=SAMPLES_PER_PIXEL)

# ppm header
print('P3 {} {} {}'.format(cam.width, cam.height, 255))

main_scene = scene(cam)
s1 = sphere([0, 0, -1], 0.5)
s2 = sphere([0, -100.5, -2], 100)
main_scene.add_object(s1)
main_scene.add_object(s2)

main_scene.draw_scene()
