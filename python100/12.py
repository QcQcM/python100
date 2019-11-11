#   判断101-200之间有多少个素数，并输出所有素数
import math


def isPrime(num):
    if num == 1 or num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True


count = 0
for j in range(101, 201):
    if isPrime(j):
        print(j)
        count = count + 1
print(count)
