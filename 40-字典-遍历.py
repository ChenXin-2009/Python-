dict1 = {'name': 'Tom', 'age': '20', 'gender': '男'}

# 1.键key
for key in dict1.keys():
    print(key, end=' ')

print()

# 2.值values
for values in dict1.values():
    print(values, end=' ')

print()
# 3.键值对items
for items in dict1.items():
    print(items, end=' ')

print()
# 4.遍历键值对
for key,values in dict1.items():
    print(f'{key} = {values}')
