class Shape:
    def ar(self):
        print(self.area)
class Square(Shape):
        def __init__(self, l):
            self.area = l ** 2
l = int(input())
myarea = Square(l)
myarea.ar()