from itertools import permutations
def permt(s):
    perm_t = ["".join(i) for i in permutations(s)]
    return perm_t
s = input()
permsst = permt(s)
for i in permsst:
    print(i)
