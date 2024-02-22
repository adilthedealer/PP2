import re
def camtosnake(s):
    mylist = re.findall('[A-Z][^A-Z]*', s)
    lowerlist = [word.lower() for word in mylist]
    return '_'.join(lowerlist)
st = input()
print(camtosnake(st))