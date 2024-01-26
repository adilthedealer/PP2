def spy_game(lst):
    for i in range(len(lst)):
        if i <= len(lst) - 3 and lst[i] == '0' and lst[i + 1] == '0' and lst[i + 2] == '7':
            return True
        else:
            continue
    return False
s = input()
mylist = s.split()
print(spy_game(mylist))