#   输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string
from pip._vendor.distlib.compat import raw_input


s = raw_input('请输入字符串：')
letter = 0
space = 0
number = 0
others = 0
for char in s:
    if char.isalpha():
        letter += 1
    else:
        if char.isspace():
            space += 1
        else:
            if char.isdigit():
                number += 1
            else:
                others += 1
print("中英文字母有%d个，空格有%d个，数字有%d个，其他字符有%d个" %(letter, space, number, others))
