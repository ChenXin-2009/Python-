
# ===================删除数据=======================
# ---------------------del------------------------
"""
del 目标
"""
name_list_2 = ['a', 'b', 'c', 'd', 'e']
'''del name_list_2 删除整个列表
print(name_list_2) 报错'''
del name_list_2[0]  # 删除name_list_2中的下标2
print(name_list_2)

# ----------------------pop------------------------
"""
序列.pop(下标)（如果不指定默认删除最后一个）
"""

name_list_2.pop()  # 删除最后一个:e
print(name_list_2)

# --------------------remove-----------------------
"""
序列.remove(数据)
删除指定数据
"""
name_list_3 = ['a', 'a', 'b', 'c', 'c', 'c', 'd']
print(name_list_3)
name_list_3.remove('c')  # 删除第一个c
print(name_list_3)

# ----------------------clear-----------------------
"""
序列.clear()
清空列表
"""
name_list_3.clear()  # 清空
print(name_list_3)

