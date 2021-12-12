name_list = ['Tom', 'Jack', 'Rose', 'Lily']
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# 1.修改指定下标数据
name_list[0] = 'aaa'
print(name_list)

# 2.逆置 reverse
print(list1)
list1.reverse()
print(list1)

# 3.排序 sort
"""
列表序列.sort(key=None, reverse=False)
reverse=Ture : 降序
reverse=False: 升序（默认）
"""
list2 = [9, 8, 6, 7, 3, 5, 4, 2, 1, 3, 4, 7, 9, 8, 1, 2, 5, 6, 8]
list2.sort()
print(list2)
list3 = [9, 8, 6, 7, 3, 5, 4, 2, 1, 3, 4, 7, 9, 8, 1, 2, 5, 6, 8]
list3.sort(reverse=True)
print(list3)
