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


