from math import pi


def deg_to_rad(degree):
    return degree * pi / 180


degree = int(input())
rad = deg_to_rad(degree)
print(rad)
