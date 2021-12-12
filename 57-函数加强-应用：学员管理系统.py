# ========================定义功能界面函数============================
def info_print():
    print('-' * 20)
    print('1.     添加')
    print('2.     删除')
    print('3.     修改')
    print('4.     查询')
    print('5.     显示')
    print('6.     退出')
    print('-' * 20)


# =====================================================================


info = []


# ==============================添加函数=============================
def add_info():
    """添加学员"""
    # 接受信息
    new_id = input('请输入学号')
    new_name = input('请输入姓名')
    new_tel = input('请输入手机号')

    # 声明info是全局变量
    global info

    # 检测用户输入的姓名是否存在，存在就报错
    for i in info:
        if new_name == i['name']:
            print('错误：学员已经存在')
            return
        elif new_id == i['id']:
            print('错误：序号已存在')
            return
        elif new_tel == i['tel']:
            print('错误：电话已存在')
            return
    # 如果不存在则添加
    info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
    # 追加字典
    # 追加列表
    info.append(info_dict)
    print('添加成功！')
    pass


# ================================================================
# ==========================删除函数===============================
def del_info():
    """删除学员"""
    del_name = input('请输入要删除的学员姓名')

    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('错误：学员不存在')


# =================================================================
# ===========================修改函数===============================


def modify_info():
    """修改函数"""
    modify_name = input('请输入要修改的学员姓名')

    global info

    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号')
            print('修改成功!')
            break


# ===================================================================
# ===========================查询学员=================================


def search_info():
    """查询学员"""
    search_name = input('请输入要修改的学员姓名')

    global info

    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下:')
            print(f"该学员的学号是{i['id']},姓名是{i['name']}，手机号是{i['tel']}")
            break
        else:
            print('错误：学员不存在')


# =====================================================================
# ==============================打印所有学员=============================
def print_all():
    """显示所有学员"""
    print('-'*10)
    print('学号\t姓名')
    for i in info:
        print(f"{i['id']}\t{i['name']}")
    print('-'*10)


# =====================================================================

while True:  # 系统功能需要循环使用
    # 1.显示功能界面
    info_print()
    # 2.用户输入功能序号
    user_num = int(input('请输入序号:'))
    # 3.功能
    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        yes_or_no = input('确定要退出吗？ yes or no?')
        if yes_or_no == 'yes':
            break
        elif yes_or_no == 'no':
            pass
        else:
            print('请输入yes或者no')
    else:
        print('请输入有效的序号')
