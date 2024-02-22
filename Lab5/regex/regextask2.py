import re
st = input()
p = re.compile('ab{2,3}')
r = p.match(st)
print(r)