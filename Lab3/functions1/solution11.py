def palindrome(st):
    for i in range(round(len(st) / 2)):
        if st[i] == st[len(st) - 1 - i]:
            continue
        else:
            return False
    return True
st = input()
print(palindrome(st))
