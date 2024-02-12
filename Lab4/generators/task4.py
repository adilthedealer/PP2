def sq_gen(a, b):
    while a <= b:
        yield a ** 2
        a += 1
a, b = int(input()), int(input())
for i in sq_gen(a, b):
    print(i, end=" ")