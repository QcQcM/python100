#   暂停一秒输出，并格式化当前时间
import datetime
import time
t = datetime.datetime.now()
print(t.strftime('%Y-%m-%d %H:%M:%S'))
time.sleep(1)
t = datetime.datetime.now()
print(t.strftime('%Y-%m-%d %H:%M:%S'))
