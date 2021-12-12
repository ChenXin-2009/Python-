# ======================================================
# 字符串：
#    一对引号：
#        name1 = 'TOM'
#        name2 = "JACK"
#    三对引号：
#        name3 = '''ROSE'''
#        name4 = """BEN"""
#        name5 = '''I am Tom
#                   nice to meet you!'''
#        name6 = """I am Jack
#                   nice to meet you!"""
# =======================================================

a = 'hello world'
print(a)
print(type(a))  # str字符串

b = '''I am Tom'''
print(type(b))

c = """I
am 
Jack"""
# 三引号支持换行
print(type(c))
print(c)
print()


# d = 'I'm Tom << 错误
d = 'I\'m Tom'  # 转义字符解决
print(d)  # I'm Tom


name = input('what is you name？')
print('hello my name is %s' % name)
print(f'hello my name is {name}')
