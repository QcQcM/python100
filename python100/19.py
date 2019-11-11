#   一个数如果恰好等于它的因子之和，这个数就称为"完数"。
#   例如6=1＋2＋3.编程找出1000以内的所有完数。
from pip._vendor.distlib.compat import raw_input
from functools import reduce


for num in range(2, 1001):
    factor = [1]
    i = 2
    while i <= num-1:
        if num % i == 0:
            factor.append(i)
        i = i + 1
    if reduce(lambda x, y: x + y, factor) == num:
        print(num)
