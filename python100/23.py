#   打印出如下图案（菱形）:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#    前4行和后3行的规律不同
#    前4行 第n行打印出第2n-1个，一共有7个位置，所空了8-2n个位置，左右各空4-n个位置
#    后三行，n又从1算起，每一行的左右各空n个位置，每一行打印7-2n个*
for i in range(5):
    for j in range(7):
        if 0 <= j <= 3-i:
            print(' ', end='')
        else:
            if 4-i <= j <= 2 + i:
                print('*', end='')
    print()
for i in range(1, 4):
    for j in range(7):
        if 0 <= j <= i-1:
            print(' ', end='')
        else:
            if i <= j < 7-i:
                print('*', end='')
    print()