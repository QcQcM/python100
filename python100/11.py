#   古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
#   小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
from pip._vendor.distlib.compat import raw_input


def function(m):
    if m == 1 or m == 2:
        return 1
    else:
        return function(m-1)+function(m-2)


month = int(raw_input('month:'))
print('该月份兔子的数量为%d' % function(month))