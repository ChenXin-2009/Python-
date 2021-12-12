help(len)


# def 函数名(参数):
#     """说明文档的位置"""
#     代码
#     ......

def sum_num(a, b):
    """
    return a+b
    返回 a 与 b 的和
    如果a = 1，b = 2 则返回3
    """
    return a + b


help(sum_num)
num = sum_num(1, 2)
print(num)
