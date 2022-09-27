'''
@Project ：PythonDeom 
@File    ：list.py.py
@Author  ：hailin
@Date    ：2022/9/26 23:38 
@Info    :  列表
'''
import random

# [数据1, 数据2, 数据3, 数据4......]
list = ['tom', 'jack', 'alice', 'park', 'rose', 'tom']
print(list[0])
print(list[1])
print(list)

# 列表序列.index(数据, 开始位置下标, 结束位置下标)
print(list.index('alice'))
print(len(list))
print(list.index('jack', 1, 4))

# count():统计指定数据在当前列列表中出现的次数。
print(list.count("tom"))

"""
判断是否存在 in 、not in
"""
print('tom' in list)
print('toms' in list)  # False
print('tom' not in list)

"""
需求：注册邮箱，用户输入一个账号名，判断这个账号名是否存在，如果存在，提示用户，否则提示可以注册
1. 用户输入账号
2. 判断if...else
"""
email = input("please input email： ")
if email in list:
    print(f"email name: {email}")
else:
    print("no email user,please register")

"""
增加
列表序列.append(数据)
"""
list.append(['chris'])  # 列表追加数据的时候，直接在原列列表里面追加了指定数据，即修改了原列表，故列表为可变类型数据。
list.append(123123)
list.append('李芳')
list.append(['chris', 'xiaoming', 'anshor'])  # 如果append()追加的数据是⼀一个序列列，则追加整个序列列到列列表
print(f'append: {list}')

# extend() 追加数据是一个序列，把数据序列里面的数据拆开然后逐一追加到列表的结尾
list.extend('xiao')
print(f'extend : {list}')

# insert():指定位置新增数据。   列表序列.insert(位置下标, 数据)
list.insert(0, 'AA')
print(f'inster: {list}')

"""
删除
"""
# del ⽬标
# del (目标)
del_list = ['sda', 'as', 'fgfg']
print(del_list)
del del_list
# print(del_list) #  name 'del_list' is not defined 已经被删掉

# del 可以删除指定下标的数据
del list[0]  # 删去AA
print(f"del list[0]: {list}")

# 2. pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
del_name = list.pop()
del_name = list.pop(1)
print(del_name)
print(list)

# remove():移除列表中某个数据的第一个匹配项。
list.remove('tom')
print(list)
# clear():清空列表
# list.clear()

"""
修改
"""
name_list = ['Tom', 'Lily', 'Rose']
name_list[0] = 'aaa'
# 结果:['aaa', 'Lily', 'Rose']
print(name_list)

# 逆置:reverse()
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
# 结果:[8, 6, 3, 2, 5, 1]
print(num_list)

# 列表序列.sort( key=None, reverse=False)
# 注意:reverse表示排序规则，reverse = True 降序， reverse = False 升序(默认)
num_list = [1, 5, 2, 3, 6, 8]
num_list.sort(reverse=False)
# 结果:[1, 2, 3, 5, 6, 8]
print(num_list)

# copy 复制
name_list = ['TOM', 'Lily', 'ROSE']
list1 = name_list.copy()

print(list1)
print(name_list)

"""
列表循环
"""

name_list = ['TOM', 'Lily', 'ROSE']
'''
1. 准备表示下标数据
2. 循环while
    条件 i < 3  len()
    遍历：依次按顺序访问到序列的每一个数据 
    i += 1
'''
print("====while : ")
i = 0
while i < len(name_list):  # 条件 没有等于 注意下标
    print(name_list[i])
    i += 1

print("====for : ")  # 实践常用for
for list in name_list:
    print(list)

"""
列表嵌套 多维度 一个列表里面包含了其他的子列表。
"""
name_list = [['TOM', 'Lily', 'Rose'],
             ['张三', '李四', '王五'],
             ['xiaohong', 'xiaoming', 'xiaolv']
             ]
print(name_list)

# 列表嵌套的时候的数据查询
print(name_list[0])
print(name_list[0][1])

"""
列表实践 需求：8位老师，3个办公室， 将8位老师随机分配到3个办公室
步骤：
1. 准备数据
    1.1 8位老师 -- 列表
    1.2 3个办公室 - 列表嵌套

2. 分配老师到办公室
    *** 随机分配
    就是把老师的名字写入到办公室列表 -- 办公室列表追加老师名字数据

3. 验证是否分配成功
    打印办公室详细信息：每个办公室的人数和对应的老师名字
"""

teach = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
office = [[], [], []]
for name in teach:
    num = random.randint(0, 2)
    office[num].append(name)
print(office)

i=1
for off in office:
    print(f'第{i}号办公室老师: ')
    for teacher in off:
        print(teacher)
    i+=1