#   两个乒乓球队进行比赛，各出三人。
#   甲队为a,b,c三人，乙队为x,y,z三人。
#   已抽签决定比赛名单。有人向队员打听比赛的名单。
#   a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

#   方法一 ： 先把两个队伍的所有排列组合都求出来，然后从c开始筛选
# from functools import reduce
#
# group = [['a', 'b', 'c'], ['x', 'y', 'z']]
# group_order = []
#
#
# def combination(list1, list2, code=','):
#     return [str(i) + code + str(j) for i in list1 for j in list2]
#
#
# comb = reduce(combination, group)
# for c in comb:
#     if ('a' in c and 'x' in c) is True or ('c' in c and 'x' in c) is True or ('c' in c and 'z' in c) is True:
#         pass
#     else:
#         if 'c' in c:
#             c_combat = c.replace('c,', '')
#         else:
#             group_order.append(c)
# print(group_order)
# for a_order in group_order:
#     if 'a' in a_order:
#         a_order = a_order.replace('a,', '')
#     if a_order != c_combat:
#         a_combat = a_order
#         break
# for b_group in range(ord('x'), ord('z') + 1):
#     if b_group != a_combat and b_group != c_combat:
#         b_combat = chr(b_group)
#         break
# print("比赛顺序为： a vs %s, b vs %s, c vs %s" % (a_combat, b_combat, c_combat))

#   方法二
for i in range(ord('x'), ord('z')+1):
    for j in range(ord('x'), ord('z')+1):
        for k in range(ord('x'), ord('z')+1):
            if i != j and j != k and i != k:
                if i != ord('x') and k != ord('x') and k != ord('z'):
                    print("比赛顺序为： a vs %s, b vs %s, c vs %s" % (chr(i), chr(j), chr(k)))
                    break

