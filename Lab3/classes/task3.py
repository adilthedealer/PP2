class Shape:
    def ar(self):
        print(self.area)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width
length, width = int(input()), int(input())
meas1 = Rectangle(length, width)
meas1.ar()
