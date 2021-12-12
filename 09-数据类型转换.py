"""============================================
                 转换数据类型
============================================"""

"""
int(x)          将x转换为一个整数
float(x)        将x转换为一个浮点数
str(x)          将对象x转换成字符串
eval(str)       用来计算在字符串中有效Python表达式，并返回一个对象
tuple(s)        将序列s转换成一个元组
list(s)         将序列s转换成一个列表
ord(x)          将一个字符转换成一个他的ASCII整数值
"""

# ====================int()==================

print('=========int()==========')
num = input('请输入一个数字')  # 输入的数据全会转换成字符串
print                       (num)
print                 (type(num))  # str

int(num)  # 转换成整型
print            (type(int(num)))  # int

# =====================float()=================

print('\n=======float()========')
num1 = 1
str1 = '10'
print(type(float(num1)))  # float
print      (float(num1))  # 1.0
print      (float(str1))  # 10.0

# =====================str()===================

print('\n=========str()========')
print     (type(str1))
print(type(str(str1)))  # str

# ====================tuple()==================

print('\n=======tuple()========')
list1 = [10, 20, 30]
print       (list1)  # [10, 20, 30]
print (type(list1))
print(tuple(list1))  # (10, 20, 30)

# =====================list()==================

print('\n=======list()=========')
tuple1 = (100, 200, 300)
print      (tuple1)
print(type(tuple1))
print(list(tuple1))

# ======================eval()=================

print('\n=======eval()==========')
str2 = '1'  # int
str3 = '1.1'  # float
str4 = '(1000, 2000, 3000)'  # tuple
str5 = '[1000, 2000, 3000]'  # list
print            (str2)
print(type(eval(str2)))  # int
print            (str3)
print(type(eval(str3)))  # float
print            (str4)
print(type(eval(str4)))  # tuple
print            (str5)
print(type(eval(str5)))  # list


