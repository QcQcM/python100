#   求s=a+aa+aaa+aaaa+aa...a的值，
#   其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
from pip._vendor.distlib.compat import raw_input
s = 0
a = raw_input('a:')
count = int(raw_input('count:'))
for i in range(count):
    temp = int(a*(i + 1))
    s += temp
print("和为%d" %s)
