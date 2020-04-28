from tqdm import tqdm
import vec
from colour import colour

IMG_WIDTH = 200
IMG_HEIGHT = 100

# ppm header
print('P3 {} {} {}'.format(IMG_WIDTH, IMG_HEIGHT, 255))

for i in tqdm(range(IMG_HEIGHT)):
    for j in range(IMG_WIDTH):
        r = (IMG_HEIGHT - i) / IMG_HEIGHT
        g = j / IMG_WIDTH
        b = 0.2

        c = colour([r, g, b])

        c.write_colour()
