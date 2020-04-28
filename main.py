IMG_WIDTH = 200
IMG_HEIGHT = 100

# ppm header
print('P3 {} {} {}'.format(IMG_WIDTH, IMG_HEIGHT, 255))

for i in reversed(range(IMG_HEIGHT)):
    for j in range(IMG_WIDTH):
        r = i / IMG_HEIGHT
        g = j / IMG_WIDTH
        b = 0.2

        ir = int(256*r)
        ig = int(256*g)
        ib = int(256*b)

        print('{} {} {}'.format(ir, ig, ib))
