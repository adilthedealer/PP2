from math import sqrt
def primecheck(*mylist):
    plist = []
    for i in range(len(mylist)):
        num = int(mylist[i])
        i = 2
        while i <= int(sqrt(num)):
            if num % i == 0:
                break
            i += 1
        else:
            plist.append(num)
    return plist
s = input()
mylist = s.split()
print(primecheck(*mylist))

