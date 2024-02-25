import re
st = input()
p = re.compile(".*a.*b$")
r = p.match(st)
print(r)
