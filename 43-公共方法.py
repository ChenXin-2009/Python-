"""
len()                       计算容器中元素个数
del 或 del()                 删除
max()                       返回容器中最大值
min()                       返回容器中最小值
range(start,end,step)       供for循环使用的遍历
enumerate()                 将数据对象组合成一个索引序列，同时列出数据和下标，一般用在for循环当中
"""
sss1 = 'abcdefg'
lll1 = [10, 20, 30, 40, 50, 60]
ttt1 = (100, 200, 300, 400, 500, 600)

print(len(sss1))
del sss1
# print(sss1)  # 报错
print(max(ttt1))
print(min(ttt1))
for i in range(1, 10):  # 1 ~ 9不包括结束
    print(i)
for i in enumerate(lll1, start=1):  # start 默认为0
    print(i)
