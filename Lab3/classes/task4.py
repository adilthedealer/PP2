from math import pow, sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
    def dist(self, x1, y1):
        return sqrt(pow(self.x - x1, 2) + pow(self.y - y1, 2))


