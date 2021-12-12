"""
1，按经验将不同的变量存储不同类型的数据
2，验证这些数据是什么类型 -- 检测数据类型 -- type(数据)
    函数type返回数据类型
"""

'''

数据类型：
    数值：
        int整型
        float浮点型
    bool布尔型：
        Ture真
        False假
    str字符串
    list列表
    tuple元组
    set集合
    dict字典
    
'''

num1 = 1  # int整型
print(type(num1))  # 输出<class 'int'>

num2 = 1.1  # float浮点型(小数)
print(type(num2))  # 输出<class 'float'>

a = 'hello world'  # str字符串(数据都要带引号)
print(type(a))  # 输出<class 'str'>

b = True  # boll布尔型(判断对错食用，只有两个取值：Ture(真) 和 False(假))
print(type(b))  # 输出<class 'boll'>

c = [10, 20, 30]  # list列表
print(type(c))  # 输出<class 'list'>

d = (10, 20, 30)  # tuple元组
print(type(d))  # 输出<class 'tuple'>

e = {10, 20, 30}  # set集合
print(type(e))  # 输出<class 'set'>

f = {'name': 'TOM', 'age': 18}  # dict字典
print(type(f))  # 输出<class 'dict'>

