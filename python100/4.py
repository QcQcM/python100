#   输入某年某月某日，判断这一天是这一年的第多少天
from pip._vendor.distlib.compat import raw_input
year = int(raw_input("year:"))
month = int(raw_input("month:"))
day = int(raw_input("day:"))
days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
#   判断是不是闰年 能被4整除 但不能被100整除 或者能被400整除
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    r_day = days2
else:
    r_day = days1
for i in range(month-1):
    sum = sum + r_day[i]
sum = sum + day
print(sum)
