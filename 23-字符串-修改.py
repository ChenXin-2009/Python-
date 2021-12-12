"""
replace()
替换
语法：
    字符串序列.replace(旧子串,新子串,替换次数)
replace 是返回修改后的字符串而不是修改字符串
说明字符串是不可变类型
"""

print()
str1 = 'hello world and itcast and ithemia and Python'
str2 = str1.replace('and', 'he')
print(str2)
str3 = str1.replace('and', 'he', 1)  # 替换1次
print(str3)

"""
split()
按照指定字符串分割字符串
语法：
    字符串序列.split(分割字符,num)
注意:num表示的是分割字符出现的次数，即将来返回数据的个数为num+1个
分割会丢失分割字符
"""
print()
list1 = str1.split('and')
print(list1)
# ['hello world ', ' itcast ', ' ithemia ', ' Python']
# 转换成列表类型
list2 = str1.split('and', 2)
print(list2)
# ['hello world ', ' itcast ', ' ithemia and Python']
# 只分割两次

"""
join()
合并列表里的字符串数据为一个大字符串
语法：
    字符或子串.join(多字符串组成的序列)
        ^
  连接用的字符或子串
"""
print()
print(' or '.join(list1))
