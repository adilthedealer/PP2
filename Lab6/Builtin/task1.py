from functools import reduce
import operator

def mlt_list(mylist):
    if len(mylist) == 0:
        return 0
    else:
        return reduce(operator.mul, mylist)
mylist = [6, 5, 13, 17, 24, 19]
res = mlt_list(mylist)
print(res)