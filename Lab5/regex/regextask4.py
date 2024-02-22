import re
st = input()
p = re.compile("[A-Z][a-z]+")
r = p.match(st)
print(r)