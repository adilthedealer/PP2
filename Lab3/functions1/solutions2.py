def fahr_to_celc(fahr):
    C = (5 / 9) * (fahr - 32)
    return C
fahr = int(input())
print(fahr_to_celc(fahr))
exit()
