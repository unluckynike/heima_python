'''
@Project ：PythonDeom 
@File    ：fun.py.py
@Author  ：hailin
@Date    ：2022/9/27 20:25 
@Info    : 函数
'''

"""
定义函数
def 函数名(参数): 
    代码1
    代码2 
    ......

调用函数
函数名(参数)
"""


# 定义函数
def info_print():
    print('hello world')


# 调用函数
info_print()


# 需求:复现ATM取钱功能。
def ATM():
    print('查询余额')
    print('存款')
    print('取款')


ATM()

# 参数
"""
def 函数名(参数):
    代码
    ......
"""


def add(a, b):
    return a + b;


num = add(3, 9)
print(num)
print(add(8, 8))


# 函数嵌套
def funA():
    print('funA')


def funB():
    funA()  # 函数调用函数
    print('funB')


funB()


# 打印一条横线
def line(num):
    print('--' * num)


line(10)


# 打印多条横线
def mulitLine(num1, num2):
    for i in range(num1):
        print('-' * i)
        for j in range(num2):
            print('——' * num2)


mulitLine(2,3)


#  1. 任意三个数之和

def sum(a,b,c):
    return a+b+c

print('sum: ',sum(1,9,3))


# 2. 任意三个数求平均值
def avg(a,b,c):
    return sum(a,b,c)/3

print('avg: ',avg(6,9,3))