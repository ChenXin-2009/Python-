"""
在python中，值是靠引用来传递的
我们可以用id()来判断两个变量是否为同一个值的引用。我们可以将id理解为那块内存的地址标识。
"""
# 变量
a = 1
b = a

print(b)  # 1

print(id(a))
print(id(b))

a = 2
print(b)  # 1        说明int为不可变类型
print(id(a))  # 2 此时得到的是2的内存地址

# 列表
aa = [10, 20]
bb = aa

print(id(aa))
print(id(bb))

aa.append(20)
print(bb)  # 10, 20, 30   列表为可变类型

print(id(aa))
print(id(bb))
