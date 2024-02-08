def squareGen(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1


n = int(input())
for i in squareGen(n):
    print(i)
