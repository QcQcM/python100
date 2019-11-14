#   给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
from pip._vendor.distlib.compat import raw_input


num = int(raw_input('num:'))
count = 0
for i in range(1, 6):
    if num / 10 ** i <= 9:      # 49999只有除以10000才会等于个位数，除以1000等于十位数...
        print('它是%d位数' %(i + 1))
        count = i + 1
        break
a = int(num / 10000)
b = int(num % 10000 / 1000)
c = int(num % 1000 / 100)
d = int(num % 100 / 10)
e = int(num % 10)
list = [e, d, c, b, a]      # 把各位上的数字倒序存到列表里
for i in range(count):
    print(list[i], end='')
