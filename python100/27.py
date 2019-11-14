#   利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
from pip._vendor.distlib.compat import raw_input
string = str(raw_input('s:'))


def reverse(s):
    if len(s) != 1:
        reverse(s[1:])
    print(s[0], end='')
    return


reverse(string)