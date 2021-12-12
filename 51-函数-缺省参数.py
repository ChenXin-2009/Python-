# 缺省参数也叫默认参数，位置参数必须在关键字参数的前面
def user_info(name, age, gender='男'):
    print(f'你的名字是{name}，你是年龄是{age}，你的性别是{gender}')


user_info('小明', '20')
user_info('小红', '20', '女')
