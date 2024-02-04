import datetime

x = datetime.datetime.now()
if x.day == 1:
    if x.month in [2, 4, 6, 8, 9, 11]:
        print(31, x.month - 1, x.year, sep="-")
    elif x.month in [5, 7, 10, 12]:
        print(30, x.month - 1, x.year, sep="-")
    elif x.month == 3:
        print(28, x.month - 1, x.year, sep="-")
    else:
        print(31, 12, x.year - 1, sep="-")
else:
    print(x.day - 1, x.month, x.year, sep="-")
print(x.day, x.month, x.year, sep="-")
if x.day <= 30 and x.month in [1, 3, 5, 7, 8, 10, 12]:
    print(x.day + 1, x.month, x.year, sep="-")
elif x.day == 30 and x.month in [4, 6, 9, 11]:
    print(1, x.month + 1, x.year, sep="-")
elif x.day == 28 and x.month == 2:
    print(1, x.month + 1, x.year, sep="-")
else:
    print(x.day + 1, x.month, x.year, sep="-")
