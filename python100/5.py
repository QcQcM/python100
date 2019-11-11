#   输入三个整数x,y,z，请把这三个数由小到大输出
from pip._vendor.distlib.compat import raw_input

list = []
for i in range(3):
    x = int(raw_input('number:'))
    list.append(x)
print(sorted(list))
