# abs  :绝对值计算
print(abs(-10))


# ===

def sum_num(a, b, f):
    return f(a) + f(b)


result = sum_num(-1, 2, abs)
print(result)
# round:四舍五入计算
print(round(5.4))
print(round(5.5))

# map(func, st) 将传入的func作用到st的每个元素中
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(x):
    return x ** 2


r = map(func, l1)
print(list(r))
