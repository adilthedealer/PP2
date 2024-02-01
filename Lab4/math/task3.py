from math import tan, pi


def a(n, l):
    r = l / (2 * tan(pi / n))
    return 0.5 * r * l * n


n, l = int(input("Input the number of sides: ")), int(input("Input the length of a side: "))
ar = a(n, l)
print("The area of the polygon is:", round(ar))
