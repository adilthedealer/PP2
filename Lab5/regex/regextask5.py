import re
st = input()
p = re.compile("a[a-zA-Z0-9='\";\\\\!@#$%^&*/()|-]*b")
r = p.match(st)
print(r)
