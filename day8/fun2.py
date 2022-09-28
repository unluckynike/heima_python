'''
@Project ：PythonDeom 
@File    ：fun2.py
@Author  ：hailin
@Date    ：2022/9/27 20:43 
@Info    :  函数
'''

"""
变量作用域
"""


def fun1():
    a = 9
    print(a)


fun1()
# print(a) 超出函数范围

"""
声明全局变量：函数体内外都能访问
"""
a = 100

print(a)


def testA():
    print(a)


def testB():
    print(a)


testA()
testB()

"""
全局变量
"""
# B函数想要a的取值是200
c = 500


def fun2():
    global c  # 声明为全局遍历
    c = 200
    print(c)


print(c)  # 100
fun2()
print('globle :', c)

"""
修改全局变量 多函数公用
"""
b = 9


def fun3():
    global b
    b = 3


def fun4():
    print(b)


fun3()
fun4()

"""
返回值
1. return a, b 写法，返回多个数据的时候，默认是元组类型。
2. return后⾯可以连接列表、元组或字典，以返回多个值。
"""


def return_num():
    return 1, 2


result = return_num()
print(result)  # (1, 2)

"""
位置参数
"""


def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20, '男')

"""
关键字参数
"""


def user_info(name, age, gender):
    print(f'您的名字是{name}, 年年龄是{age}, 性别是{gender}')


user_info(name='TOM', gender='女', age=18)  # 参数指定键值对

"""
默认参数
"""


def user_info(name, age, gender='男'):  # 带默认值
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20)
user_info('Rose', 18, '⼥')  # 可改变默认值

"""
不定长参数
"""


# 包裹位置传递
def user_info(*args):  # 接收所有位置参数，返回一个元组
    # 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)， args是元组类型，这就是包裹位置传递。
    print(args)


# ('TOM',)
user_info('TOM')
# ('TOM', 18)
user_info('TOM', 18)


# 包裹关键字
def user_info(**kwargs):  # 收集所有关键字参数，返回一个字典
    print(kwargs)


# {'name': 'TOM', 'age': 18, 'id': 110}
user_info(name='TOM', age=18, id=110)
# ⽆论是包裹位置传递还是包裹关键字传递，都是一个组包的过程。


"""
拆包和交换变量值
"""


# 元组拆包
def fun5():
    return 100, 200, 300


tuple1, tuple2, tuple3 = fun5()
print(f'{tuple1},{tuple2},{tuple3}')

# 字典拆包
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1  # 对字典进行拆包，取出来的是字典的key

print(a)  # name
print(b)  # age
print(dict1[a])  # TOM
print(dict1[b])  # 18

"""
交换变量 有变量 a = 10 和 b = 20 ，交换两个变量的值。
"""
a = 10
b = 20

temp = 0
temp = a
a = b
b = temp

print(f'a:{a} ,b:{b}')

# 在python
a, b = 10, 20
print(f'a:{a} ,b:{b}')

a, b = b, a
print(f'a:{a} ,b:{b}')

"""
引用
在python中，值是靠引用来传递来的。
我们可以用 id() 来判断两个变量是否为同一个值的引⽤用。 我们可以将id值理理解为那块内存的地址标识。
"""

#int
a=1
b=a
print(f'aid: {id(a)} , bid:{id(b)}') #引用地址相同
a=4
print(f'aid: {id(a)} , bid: {id(b)}') #  因为修改了a的数据，内存要开辟另外一份内存取存储2，id检测a和b的地址不同

aa = [10, 20]
bb = aa

print(f'aaid: {id(aa)} , bbid: {id(bb)}')

aa.append(30)

print(f'aaid: {id(aa)} , bbid: {id(bb)}')

"""
"""
def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))
# int:计算前后id值不不同
b = 100
test1(b)
# 列列表:计算前后id值相同
c = [11, 22]
test1(c)







