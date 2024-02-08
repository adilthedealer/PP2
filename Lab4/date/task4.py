import datetime

mlist = list(map(int, input().split()))
year1, month1, day1 = mlist[2], mlist[1], mlist[0]
year2, month2, day2 = mlist[5], mlist[4], mlist[3]
j = datetime.date(year1, month1, day1)
k = datetime.date(year2, month2, day2)
date1 = k - j
ans = date1.total_seconds()
print(ans)
