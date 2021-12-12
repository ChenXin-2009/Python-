def num():
    return 1000
    print(2000)


a = num()
print(a)
num()


# 函数返回值后面的语句不会执行

def sum_num(b, c):
    return b + c


num2 = sum_num(1, 2)
print(num2)
