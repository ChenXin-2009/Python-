import random  # 电脑出的随机数

while True:
    p = int(input('0石头，1剪刀，2布'))
    c = random.randint(0, 2)

    if p == 0:
        if c == 0:
            print('===========平局')
        elif c == 1:
            print('==========玩家赢了')
        elif c == 2:
            print('=========玩家输了')
    elif p == 1:
        if c == 0:
            print('=========玩家输了')
        elif c == 1:
            print('=========平局')
        elif c == 2:
            print('===========玩家赢了')
    elif p == 2:
        if c == 0:
            print('============玩家赢了')
        elif c == 1:
            print('===========玩家输了')
        elif c == 2:
            print('===============平局')
    print(f'电脑出的是{c}')
