import re
def spUp(s):
    parts = re.findall('[A-Z][^A-Z]*', s)
    return parts
st = input()
print(spUp(st))