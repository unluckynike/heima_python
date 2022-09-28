'''
@Project ：PythonDeom 
@File    ：infer.py
@Author  ：hailin
@Date    ：2022/9/27 17:40 
@Info    :  推导式 生产式  更加复合python代码风格 化简代码量
  列表推导式
  字典推导式
  集合推导式
'''
# 需求:创建一个0-10的列表。
# while
list = []
i = 0
while i <= 10:
    list.append(i)
    i += 1
print(list)

# for
list = []
for i in range(0, 11, 1):
    list.append(i)
print(list)

# 列表推导式实现
list1 = [i for i in range(11)]
print(list1)

# 带if的列表推导式
# 需求：0-10偶数数据的列表
list2 = [i for i in range(0, 11, 2)]
print('range : ', list2)

# if 实现
list3 = [i for i in range(11) if i % 2 == 0]
print('if : ', list3)

# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 数据1 ： 1 和 2  range(1,3)
# 数据2 ：0 1 2  range(3)
list4 = []
for i in range(1, 3):
    for j in range(5):
        list4.append((i, j))
print(list4)

# 推导式
list5 = [(i, j) for i in range(1, 3) for j in range(3)]  # 循环嵌套
print(list5)

"""
字典推导式
"""
# 创建字典 key是1-5的数字，v是这个数字的平方
# dict1 = {k: v for i in range(1, 5)}
dict = {i: i ** 2 for i in range(1, 5)}
print(dict)

# 合并字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}  # 注意rang范围写法 取列表短短遍历
print(dict1)

# 1. 需求：提取电脑台数大于等于200
# 获取所有键值对数据，判断v值大于等于200 返回  字典
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict5 = {k: v for k, v in counts.items() if v >= 200}
print(dict5)

# 需求:创建⼀个集合，数据为下方列列表的2次方。
list1 = [1, 1, 2]
set = {list1[i] ** 2 for i in range(len(list1))}
print(set)
set1 = {i ** 2 for i in list1}
print(set1)
