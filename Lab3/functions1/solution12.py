def histogram(lst):
    ct = list()
    for i in range(len(lst)):
        ct.append("*" * lst[i])
    return ct
s = input()
mylist = s.split()
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
print(mylist)
arr = histogram(mylist)
for i in arr:
    print(i)
