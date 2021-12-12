# 拆包
def yuanzhu():
    return 100, 200


a1, a2 = yuanzhu()
print(a1)
print(a2)

# 交换变量值

# 方法1
a = 20
b = 10

c = a
a = b
b = c

print(a, b)

# 方法2
aa = 20
bb = 10
aa, bb = bb, aa
print(aa, bb)
