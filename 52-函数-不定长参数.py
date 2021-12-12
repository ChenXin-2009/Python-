# 不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数
# 包裹位置传递
def user_info(*args):
    print(args)


user_info('Tom', '20')


# 包裹关键字传递
def user_info2(**kwargs):
    print(kwargs)


user_info2(name='Tom', age=18, id=110)
