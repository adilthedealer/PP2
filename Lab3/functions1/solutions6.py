def reversal(lst):
    ct = list()
    for i in range(len(lst) - 1, -1, -1):
        ct.append(lst[i])
    return ct
s = input()
mylist = s.split()
anslist = reversal(mylist)
for i in anslist:
    print(i, end=' ')
