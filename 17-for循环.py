"""
for 临时变量 in 序列:
    重复执行1
    重复执行2
    ......
"""

str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in str1:
    print(i, end='')
print()
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# range函数
for i in range(11):
    print(i, end=' ')
# 1 2 3 4 5 6 7 8 9 10

str2 = 'abcdefg'
print()
for i in str2:
    if i == 'e':
        print('不打印e', end='\t')
        continue
    print(i, end=' ')

str3 = 'abcdefg'
print()
for i in str3:
    if i == 'e':
        print('遇到e，不打印e，停止打印')
        break
    print(i, end=' ')


