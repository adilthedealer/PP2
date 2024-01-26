def unique_list(lst):
    ct = list()
    for i in range(len(lst)):
        if ct.count(lst[i]) == 0:
            ct.append(lst[i])
    return ct
s = input()
mylist = s.split()
listt = unique_list(mylist)
for i in listt:
    print(i, end=" ")
