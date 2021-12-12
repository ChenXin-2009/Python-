# 键+值 没有顺序需求
def user_info(name, age, gender):
    print(f'你多名字{name}，你的年龄{age}，性别{gender}')


user_info('xiaomin', '20', '男')
user_info(age=20, gender='男', name='小明')
