dict1 = {'name': 'Tom', 'age': '20', 'gender': '男'}

# 1.key
print(dict1['name'])  # name对应Tom，输出Tom
# print(dict1['names'])  # 报错

# 2.函数
# 2.1 get
print(dict1.get('name'))  # Tom
print(dict1.get('names'))  # 不存在返回None
print(dict1.get('name', 'Lily'))

# 2.2 keys
print(dict1.keys())

# 2.3 values
print(dict1.values())

# 2.4 items
print(dict1.items())
