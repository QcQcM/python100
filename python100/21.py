#   猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#   以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


def countPeach(day):  # 从第十天到第九天推的一个思路,递归
    if day == 10:
        return 1
    else:
        return (countPeach(day + 1) + 1) * 2


def countPeach1(day):  # 从第十天到第九天推的一个思路,非递归
    allPeach = 1
    while day > 1:
        allPeach = (allPeach + 1) * 2
        day = day - 1
    return allPeach



print(countPeach1(10))
