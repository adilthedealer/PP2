import re
def splitUpper(s):
    mylist = re.findall('[A-Z][^A-Z]*', s)
    return ' '.join(mylist)
st = input()
print(splitUpper(st))