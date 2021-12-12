dict1 = {'name': 'Tom', 'age': '20', 'gender': '男'}
print(dict1)

# del删除指定能内容
# del(dict1)
# print(dict1)  # 报错

del dict1['name']
print(dict1)  # 删除name键

dict1.clear()  # 清空列表
print(dict1)
