def evenGen(n):
    i = 0
    while i <= n:
        yield i
        i += 2


n = int(input())
mylist = list()
for i in evenGen(n):
    mylist.append(i)
for i in range(len(mylist)):
    if i <= len(mylist) - 2:
        print(mylist[i], end=", ")
    else:
        print(mylist[i])