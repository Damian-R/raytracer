from vec3 import vec3

class camera:
    def __init__(self, origin=[0, 0, 0], width=200, height=100):
        self.width = width
        self.height = height
        self.origin = vec3(origin)
        self.screen = {
            'll_corner': self.origin + vec3([-2, -1, -1]),
            'hor': vec3([4, 0, 0]),
            'vert': vec3([0, 2, 0]),
        }
