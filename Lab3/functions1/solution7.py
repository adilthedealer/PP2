def has_33(lst):
    for i in range(len(lst)):
        if i <= len(lst) - 2 and lst[i] == "3" and lst[i + 1] == "3":
            return True
        else:
            continue
    return False
s = input()
mylist = s.split()
print(has_33(mylist))
