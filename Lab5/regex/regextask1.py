import re
st = input()
p = re.compile('ab*')
r = p.match(st)
print(r)
