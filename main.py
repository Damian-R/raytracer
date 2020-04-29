from tqdm import tqdm
from colour import colour
from camera import camera
from scene import scene

cam = camera()

# ppm header
print('P3 {} {} {}'.format(cam.width, cam.height, 255))

main_scene = scene(cam)

main_scene.draw_scene()
