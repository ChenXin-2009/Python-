# 打印横线图形
def p_l():
    print('-' * 20)


def p(num):
    for i in range(num):
        p_l()


p(5)


# 返回3个数的平均值

def jia(a1, b1, c1):
    return a1 + b1 + c1


def chu(num):
    return num / 3


def pjz(a1, b1, c1):
    return chu(jia(a1, b1, c1))


a = int(input('3个数:'))
b = int(input())
c = int(input())

d = pjz(a, b, c)
print(d)
