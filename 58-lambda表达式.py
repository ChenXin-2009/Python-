def fn1():
    return 600


result = fn1()
print(result)

fn2 = lambda: 100
print(fn2)
print(fn2())

# === === === === === === === === 一个参数 === === === === === === === === ===
f1 = lambda a: a
print(f1('hello,world'))
# === === === === === === === === 默认参数 === === === === === === === === ===
f2 = lambda a, b, c=100: a + b + c
print(f2(10, 1))
# === === === === === === === === 可变参数*args=== === === === === === === ===
f3 = lambda *args: args
print(f3(10, 20, 30))
# === === === === === === === === 可变参数**kwargs === === === === === === ===
f4 = lambda **kwargs: kwargs
print(f4(name='python', age=20))
# === ==== === ==== === ==== ===  带判断的lambda   === ==== === ==== === =====
f5 = lambda a, b: a if a > b else b
print(f5(100, 200))
print(f5(1000, 500))

