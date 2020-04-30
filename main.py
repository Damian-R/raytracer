from tqdm import tqdm
from colour import colour
from camera import camera
from scene import scene
from sphere import sphere

cam = camera()

# ppm header
print('P3 {} {} {}'.format(cam.width, cam.height, 255))

main_scene = scene(cam)
s1 = sphere([0, 0, -1], 0.5)
main_scene.add_object(s1)

main_scene.draw_scene()
