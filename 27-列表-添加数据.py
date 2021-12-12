# ===================添加数据=======================
# ---------------append 结尾追加数据-----------------
name_list = ['Tom', 'Jack', 'Lily', 'Rose', 'Tom']
name_list.append('CX')
print(name_list)  # 多一个CX
# ---------------extend 结尾追加数据，序列------------
name_list.extend([])
print(name_list)
# 多出了 'hello', 'HELLO'
# ---------------insert 指定位置增加数据--------------
name_list.insert(1, 'xiaoming')
# 在下标1多处了一个xiaoming
print(name_list)
