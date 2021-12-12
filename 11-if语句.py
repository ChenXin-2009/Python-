"""
if 条件:
    条件成立时执行的代码
    ......
"""
t = True
f = False

if t:  # 条件成立
    print('条件成立执行的语句1')
    print('条件成立执行的语句2')
    print('条件成立执行的语句3')

if f:  # 条件不成立
    print('条件成立执行的语句1')  # 不执行
    print('条件成立执行的语句2')
    print('条件成立执行的语句3')
else:
    print('条件不成立执行')

# ===================例====================
print('=============例================')

age = int(input('请输入年龄'))

if age <= 18:
    print(f'你输入的年龄是{age},未成年')
elif 18 < age < 60:
    print(f'你输入的年龄是{age},已成年')
elif age >= 18:
    print(f'你输入的年龄是{age},退休')

# ===================嵌套===================
print('================例2=============')

money = int(input('钱：1有，0没'))
seat  = int(input('座位：1有，0没'))

if money:
    if seat:
        print('ok')
    else:
        print('没位置')
else:
    print('没钱')
