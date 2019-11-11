# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
from pip._vendor.distlib.compat import raw_input

profit = int(raw_input("input"))
print("input profit is %d w" % profit)
threshold = [100, 60, 40, 20, 10, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
i = 0
money = 0
while i <= len(threshold)-1:
    if threshold[i] <= profit:
        money = money + (profit-threshold[i])*rate[i]
        profit = threshold[i]
    i = i + 1
print(money)
