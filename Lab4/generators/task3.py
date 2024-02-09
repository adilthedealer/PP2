def mod3and4(n):
    i = 0
    while i <= n:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1
n = int(input())
mylist = list()
for i in mod3and4(n):
    mylist.append(i)
for i in mylist:
    print(i, end=' ')