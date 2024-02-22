import re
def upper(s):
    return s.group(0).upper()[1::]
st = input()
print(re.sub('_[a-z]', upper, st))