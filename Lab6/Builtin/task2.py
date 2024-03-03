s = input()
cntu, cntl = 0, 0
for letter in s:
    if letter.isupper():
        cntu += 1
    elif letter.islower():
        cntl += 1
    else:
        continue
print(cntu, cntl, sep="\n")