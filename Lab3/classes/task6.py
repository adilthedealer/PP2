from math import sqrt
s = input()
mylist = s.split()
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
rtlist = list(filter(lambda x: (x > 1 and all(x % i != 0 for i in range(2, int(sqrt(x)) + 1))), mylist))
for i in rtlist: 
    print(i, end=" ")