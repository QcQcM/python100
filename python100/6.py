#   斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34
def fib(num):
    if num == 1:
        return 0
    else:
        if num == 2:
            return 1
        else:
            return fib(num-1)+fib(num-2)
for i in range(1,11):
    print(fib(i))