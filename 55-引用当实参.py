def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))


b = 100
test1(b)  # 不同
c = [11, 22]
test1(c)  # 相同
