#   输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#   Monday、Tuesday、Wednesday、Thursday、Friday、Saturday 、Sunday
from pip._vendor.distlib.compat import raw_input


input_week = str(raw_input('first:'))
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
count = 2
while count >= 1:   # count是这个列表里开头是input_week的元素的数量，当列表里不止一个符合条件时循环
    count = 0   # 每次需要归零操作
    maybe = []
    for w in week:  # 如果符合条件，count就加一，并把符合条件的加入输出列表
        if w.find(input_week) != -1:
            count += 1
            maybe.append(w)
    if count > 1:
        input_week += str(raw_input('second:'))
    else:   # 如果只有一个符合条件的说明找到了，输出
        print(maybe[0])
        break





