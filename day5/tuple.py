'''
@Project ：PythonDeom 
@File    ：tuple.py
@Author  ：hailin
@Date    ：2022/9/27 16:06 
@Info    : 元组
'''

"""
一个元组可以存储多个数据，元组内的数据是不能修改的。
元组特点:定义元组使⽤⼩括号，且逗号隔开各个数据，数据可以是不同的数据类型。
"""
tuple = (10, 20, 30)
print(tuple)
print(type(tuple))

# 多个数据元组
t1 = (1, 2, 3, 4, 5)
print(t1)

# 单个数据元组
# 如果定义的元组只有⼀个数据，那么这个数据后⾯添加逗号，否则数据类型为唯一的这个数据的数据类型
t2 = (1,)
print(t2, type(t2))

t3 = (2)  # 不加逗号
print(t3, type(t3))

t4 = ('aaaa')
print(t4, type(t4))

"""
常见操作 由于不能修改 只支持查找
"""
# 下标
tuple = ('aa', 'bb', 'cc', 'bb')
print(tuple[0])  # aa
# 直接修改则报错
# tuple[0]='dd' # 'tuple' object does not support item assignment

# index():查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index 方法相同。
print(tuple.index('bb'))
# count():统计某个数据在当前元组出现的次数。
print(tuple.count('bb'))
# len():统计元组中数据的个数。
print(len(tuple))

# 但是如果元组⾥⾯有列表，修改列列表里面的数据则是⽀支持的
tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
print(tuple2[2])  # 访问到列表
print(tuple2) # (10, 20, ['aa', 'bb', 'cc'], 50, 30)

tuple2[2][0]='qaqa'
print(tuple2) # (10, 20, ['qaqa', 'bb', 'cc'], 50, 30)
