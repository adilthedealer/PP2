import re
st = input()
p = re.compile("[a-z]+_")
r = p.match(st)
print(r)