"""Task: 
User inputs a list of integers. After selecting only unique integers, display
the sum and the mirrored input.
"""


def unique_list(lst):
    ct = list()
    for i in range(len(lst)):
        if ct.count(lst[i]) == 0:
            ct.append(lst[i])
    return ct


def reversal(lst):
    ct = list()
    for i in range(len(lst) - 1, -1, -1):
        ct.append(lst[i])
    return ct


s = input()
mylist = s.split()
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
prlist = unique_list(mylist)
finlist = reversal(prlist)
sum = 0
for i in range(len(finlist)):
    sum += finlist[i]
for i in finlist:
    print(i, end=" ")
print()
print(sum)
