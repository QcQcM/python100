#   暂停一秒输出

import time

array = ['I', 'want', 'to', 'see', 'my boyfriend']
for i in range(len(array)):
    print(array[i], end=" ")
    time.sleep(1)