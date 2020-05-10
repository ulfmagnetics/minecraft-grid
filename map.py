from utils import top_left_coordinate

class Map:
    def __init__(self, m, n, size):
        self.m = m
        self.n = n
        self.size = size
        self.top_left = top_left_coordinate(m, n, size)

    # Return the bounds of the map as a four-tuple (x0, y0, x1, y1)
    def bounds(self):
        return (self.top_left[0], self.top_left[1], self.top_left[0] + self.size, self.top_left[1] + self.size)

