"""
公共操作：
运算符
  +         合并                  字符串列表元组
  *         复制                   字符串列表元组
  in        判断是否存在              字符串列表元组字典
"""

# 公共操作之加法运算符
s1 = 'aa'
s2 = 'bb'
l1 = [1, 2]
l2 = [10, 20]
t1 = (1, 2)
t2 = (10, 20)
d1 = {"name": "Python"}
d2 = {"age": 30}

print(s1 + s2)  # aabb
print(l1 + l2)
print(t1 + t2)
# print(d1 + d2)  # 出错

# 公共操作之乘法运算符
ss1 = 'a'
ll1 = ['hello']
tt1 = ('world',)

print(ss1 * 5)  # aaaaa
print('--' * 10)
print(ll1 * 5)
print(tt1 * 5)

# 公共操作之判断参数是否存在

sss1 = 'abcdefg'
lll1 = [10, 20, 30, 40]
ttt1 = (100, 200, 3000)

print('a' in sss1)  # Ture
print(20 not in lll1)
print(300 in lll1)
