from math import pi, pow
def volume(rad):
    return (4 * pi * pow(rad, 3)) / 3
rad = int(input())
print(volume(rad))