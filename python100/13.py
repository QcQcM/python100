#   打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
#   其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100, 1000):
    percentile = int(i / 100)
    very_bit = int((i - percentile*100)/10)
    unit = i % 10
    if percentile**3 + very_bit**3 + unit**3 == i:
        print(i)