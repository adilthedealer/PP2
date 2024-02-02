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
        print(sqrt(pow(self.x - x1, 2) + pow(self.y - y1, 2)))
s = input()
mlst = s.split()
x, y = int(mlst[0]), int(mlst[1])
k = Point(x, y)
s1 = input()
mlstt = s1.split()
x1, y1 = int(mlstt[0]), int(mlstt[1])
k.move(x1, y1)
s2 = input()
mlstt1 = s2.split()
x2, y2 = int(mlstt1[0]), int(mlstt1[1])
k.show()
k.dist(x2, y2)
