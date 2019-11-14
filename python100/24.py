#   有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
#   先求当前的分子、再求当前的分母、然后累加
formerDen = 1   # 前一项分母等于1
den = 2     # 当前分母等于2
num = 3     # 当前分子等于3
addSum = 2 + num / den      # 累计加和初始为0
for i in range(18):
    num += den
    temp = den      # 保存现在分母的值
    den += formerDen
    formerDen = temp
    addSum += num / den
    print("%d / %d" %(num, den))
print(addSum)