#   一球从100米高度自由落下，每次落地后反跳回原高度的一半；
#   再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
import math


def function(times):
    if times == 1:
        return 100.0
    else:
        return function(times - 1) + 100.0 * pow(2, 2-times)
if __name__ == '__main__':
    print("第%d经过的总路程长度为%f,反弹高度为%f" %(10, function(10.0), 100.0 * pow(2, -10)))