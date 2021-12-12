# ==================列表推导式================
# 1.while
# 准备一个空列表
l1 = []

# 书写循环数字依次追加到空列表中
i = 0
while i < 10:
    l1.append(i)
    i += 1

print(l1)

# 2.for
l2 = []

for i in range(10):
    l2.append(i)
    i += 1

print(l2)

# 3.列表推导式

l3 = [i for i in range(10)]
print(l3)

# 4.列表推导式·if
# 创建1~10的偶数列表
# 4.1 range步长实现
l4 = [i for i in range(0, 10, 2)]
print(l4)
# 4.2 if实现
l5 = [i for i in range(10) if i % 2 == 0]
print(l5)

# 5 for嵌套
l6 = [(i, j) for i in range(1, 3) for j in range(3)]
print(l6)

# ==================字典推导式================

d1 = {i: i ** 2 for i in range(1, 5)}  # 打印i和i的平方
print(d1)

# 合并列表为字典
li1 = ['name', 'age', 'gender']
li2 = ['Tom', '20', 'man']

di1 = {li1[i]: li2[i] for i in range(len(li1))}
print(di1)

# ==================集合推导式================

lis1 = [1, 1,  2]
se1 = {i ** 2 for i in lis1}
print(se1)
