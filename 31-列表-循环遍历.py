name_list = ['Tom', 'Jack', 'Rose', 'Lily']

i = 0  # 下标从0开始
lens = len(name_list)  # lens等于列表的长度
while i < lens:
    print(name_list[i], end=' ')
    i += 1

print()

for i in name_list:
    print(i, end=' ')
