# 对10个数进行排序
# 写一个冒泡排序吧！
list = [2, 1, 10, 5, 8, 3, 4, 6, 8, 0]
# for i in range(0, 9):  # 第一轮代表要进行n-1次比较
#     for j in range(0, 10-i-1):  # 第i轮已经有i个数字被比较出来了，所以不需参加比较，每一轮需要比较的就是n-1-i
#         if list[j] > list[j + 1]:   # 升序排列
#             temp = list[j]
#             list[j] = list[j + 1]
#             list[j + 1] = temp
# print(list)


#   再写一个快排吧
def quickSort(low, high, list):
    if low >= high:
        return
    begin = low
    end = high
    pivot = list[low]
    while low <= high:
        while low <= high and list[high] >= pivot:
            high -= 1
        if low <= high:
            list[low] = list[high]
            low += 1
        while low <= high and list[low] <= pivot:
            low += 1
        if low <= high:
            list[high] = list[low]
            high -= 1
    list[low] = pivot
    quickSort(begin, low - 1, list)
    quickSort(low + 1, end, list)


quickSort(0, len(list)-1, list)
print(list)