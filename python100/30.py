#   一个数字，判断是不是回文数 1221 121
from pip._vendor.distlib.compat import raw_input


num = str(raw_input('num:'))
stack = []      # 栈不是python的内置类型，但是可以用列表模拟栈
for i in range(int(len(num)/2)):
    stack.append(num[i])
if len(num) % 2 == 0:
    low = int(len(num) / 2)
else:
    low = int(len(num) / 2) + 1
j = 0
for j in range(low, int(len(num) - 1)):
    if num[j] != stack.pop(-1):
        print("该数字不是回文数")
        break
if j >= len(num) - 1:
    print("该数字是回文数")




