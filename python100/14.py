#   题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
from pip._vendor.distlib.compat import raw_input
import math
from functools import reduce

def isPrime(num):
    if num == 1 or num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

num = int(raw_input('num:'))
nowNum = num
primeFactor = [1]
while True:
    if isPrime(num):
        primeFactor.append(num)
        print('%d = 1' % num, end="")
        for item in primeFactor:
            print('* %d' % item, end="")
        break
    i = 2
    while i <= nowNum:
        if nowNum % i == 0 and isPrime(i):
            primeFactor.append(i)
            nowNum = nowNum / i
            i = 2
        else:
            i = i + 1
        if reduce(lambda x, y: x * y, primeFactor) == num:
            print('%d = %d' % (num, primeFactor[1]), end="")
            for j in range(2, len(primeFactor)):
                print('* %d' % primeFactor[j], end="")
            break
