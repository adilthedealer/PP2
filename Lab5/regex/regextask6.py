import re
st = input()
ptrn = r'[ ,.]'
modst = re.sub(ptrn, ':', st)
print(modst)