import datetime

x = datetime.datetime.now()
if x.day <= 5:
    print(31 + (x.day - 5), x.month - 1, x.year, sep="-")
else:
    print(x.day - 5, x.month, x.year)
