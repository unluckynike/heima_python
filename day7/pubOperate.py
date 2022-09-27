'''
@Project ：PythonDeom 
@File    ：pubOperate.py.py
@Author  ：hailin
@Date    ：2022/9/27 17:18 
@Info    :  公共操作 运算符号 +、 * 、 in 、 not in
                    公共方法 len()、del 或 del()、max()、min()、range(start, end, step)、enumerate()

'''

# +
str1 = 'aa'  # 字符串
str2 = 'bb'

list1 = [1, 2]  # 列表
list2 = [10, 20]

t1 = (1, 2)  # 元组
t2 = (10, 20)

dict1 = {'name': 'Python'}  # 字典
dict2 = {'age': 30}

# +: 合并
print(str1 + str2)
print(list1 + list2)
print(t1 + t2)
# print(dict1 + dict2)  # 报错：字典不支持合并运算

# *
str1 = 'a'
list1 = ['hello']
t1 = ('world',)

# *:复制
print(str1 * 5)

# 打印10个-：
print('-' * 10)
print(list1 * 5)
print(t1 * 5)

# in 或not in
str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (100, 200, 300, 400)
dict1 = {'name': 'Python', 'age': 30}

# in 和 not in
# 1. 字符a是否存在
print('a' in str1)
print('a' not in str1)

# 2. 数据10是否存在
print(10 in list1)
print(10 not in list1)

# 3. 100是否存在
print(100 not in t1)
print(100 in t1)

# 4. name是否存在
print('name' in dict1)
print('name' not in dict1)
print('name' in dict1.keys())
print('name' in dict1.values())

"""
公共方法
"""
# len
str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]
t1 = (10, 20, 30, 40, 50)
s1 = {10, 20, 30, 40, 50}
dict1 = {'name': 'TOM', 'age': 18}
print(len(str1))
print(len(list1))
print(len(t1))
print(len(s1))
print(len(dict1))

# del
# 1. 字符串
str1 = 'abcdefg'
del str1
# print(str1) # 已被删除 name 'str1' is not defined
# 2. 列表
list1 = [10, 20, 30, 40]
del (list1[0])
print(list1)  # [20, 30, 40]

# max
str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]

# max() : 最大值
print(max(str1))  #
print(max(list1))

# min() ： 最小值
print(min(str1))
print(min(list1))

# range(start, end, step) ⽣成从start到end的数字，步长为 step，供for循环使用
# 1. 如果不写开始，默认从0开始
# 2. 如果不写步长，默认为1
print(range(1, 10, 1))
for i in range(1, 10, 1):
    print(i, end="\t")

print()
for i in range(1, 10):
    print(i, end="\t")

print()
for i in range(1, 10, 2):
    print(i, end='\t')

print()
for i in range(10):
    print(i, end='\t')
print()

# enumerate 返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
# 函数用于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i, end='\t')

print()
for i in enumerate(list1, start=1):
    print(i, end="\t")

"""
数据类型转换
"""
list1 = [10, 20, 30, 20, 40, 50]
s1 = {100, 300, 200, 500}
t1 = ('a', 'b', 'c', 'd', 'e')

# tuple(): 转换成元组
print(tuple(list1))
print(tuple(s1))

# list()：转换成列表
print(list(s1))
print(list(t1))

# set()：转换成集合
print(set(list1))
print(set(t1))




