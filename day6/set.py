'''
@Project ：PythonDeom 
@File    ：set.py
@Author  ：hailin
@Date    ：2022/9/27 16:53 
@Info    :  集合
'''

"""
特点:
1. 集合可以去掉重复数据;
2. 集合数据是⽆序的，故不支持下标
创建集合使⽤用 {} 或 set() ， 但是如果要创建空集合只能使用 set() ，因为 {} 用来创建空字典。
"""
s = {10, 20, 30, 22, 123, 22, 10, 20}
print(s)  # {10, 20, 22, 123, 30} 已经去重复了

s2 = {10, 30, 20, 10, 30, 40, 30, 50}
print(s2)

s3 = set('abcdefgaa')
print(s3)

s4 = set()
print(type(s))
print(type(s4))  # set

s5 = {}
print(type(s5))  # dic

"""
常见操作
"""
# 增加数据 add()
s = {10, 20, 30, 22, 123, 22, 10, 20}
s.add('aaa')
s.add(10)  # 重复不会添加 因为集合有去重功能，所以，当向集合内追加的数据是当前集合已有数据的话，则不进行任何操作。
print(s)

# update(), 追加的数据是序列。
s.update('a', 'p', 'l')
print(s)
s.update('abc')
print(s)

# remove()，删除集合中的指定数据，如果数据不存在则报错。
s.remove('a')
print(s)
s.remove('aaa')
print(s)

# discard()，删除集合中的指定数据，如果数据不存在也不会报错。
s.discard(123)
print(s)

# pop()，随机删除集合中的某个数据，并返回这个数据。
print(s.pop())
print(s)
print(s.pop())
print(s)

# 查找 in、not in
s1 = {10, 20, 30, 40, 50}

# in 或not in 判断数据10是否存在
print(10 in s1)

print(10 not in s1)
