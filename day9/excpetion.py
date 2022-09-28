'''
@Project ：PythonDeom 
@File    ：excpetion.py
@Author  ：hailin
@Date    ：2022/9/28 09:23 
@Info    :  递归 lambda 表达式 ⾼高阶函数

'''
import functools

"""
递归
"""


# 数字累加和
def sum(a):
    if a == 1:  # 递归出口 如果没有出口，报错：超出最大递归深度
        return 1
    return a + sum(a - 1)  # 1. 当前数字 + 当前数字-1的累加和


print(sum(3))


# 数字累乘
def mulit(num):
    if num == 1:
        return 1
    return num * mulit(num - 1)


print(mulit(4))

"""
lambda 
如果⼀个函数有一个返回值，并且只有⼀句代码，可以使⽤ lambda简化。
lambda表达式的参数可有可⽆，函数的参数在lambda表达式中完全适⽤。 
lambda函数能接收任何数量的参数但只能返回⼀个表达式的值

"""


# lambda 参数列表 : 表达式

def fun1():
    return 100


print(fun1)
print(fun1())

# lambda表达式
fn2 = lambda: 100
print(fn2)
print(fn2())

# lambda 实现 a+b
print((lambda a, b: a + b)(1, 2))
# 乘法
mulitab = (lambda a, b: a * b)(2, 3)
print(mulitab)

"参数"
# 1. 无参数
fn1 = lambda: 100
print(fn1())

# 2. 一个参数
fn2 = lambda a: a
print(fn2('hello world'))

# 3. 默认参数/缺省参数
fn3 = lambda a, b, c=100: a + b + c
print(fn3(10, 20))
print(fn3(10, 20, 200))

# 4. 可变参数：*args
fn4 = lambda *args: args
print(fn4(10, 20))
print(fn4(10, 20, 30, 40))
print(fn4(10))

# 5. 可变参数：**kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='Python'))
print(fn5(name='Python', age=30))

"判断"
# lambda 两个数字比大小，谁大返回谁
max = (lambda a, b: a if a > b else b)(2, 5)
print(max)

students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)
# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# 3. age key对应的值进行升序排序
students.sort(key=lambda x: x['age'])  # 默认升序
print(students)

"""
高阶函数
"""
# abs(): 绝对值
print(abs(-10))

# round()： 四舍五入
print(round(1.2))
print(round(1.9))


# 需求：任意两个数字，先进行数字处理(绝对值或四舍五入)再求和计算


# 1. 写法一
# def add_num(a, b):
#     # 绝对值
#     return abs(a) + abs(b)
#
#
# result = add_num(-1.1, 1.9)
# print(result)

# 2. 写法二：高阶函数:f是第三个参数，用来接收将来传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)


result1 = sum_num(-1, 5, abs)  # 注意第三个参数
print(result1)

result2 = sum_num(1.1, 1.3, round)
print(result2)

# map(func, lst)，将传⼊入的函数变量量func作用到lst变量量的每个元素中，并将结果组成新的列表(Python2)/ 迭代器器(Python3)返回。
# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5]


# 2. 准备2次方计算的函数
def func(x):
    return x ** 2


# 3. 调用map
result = map(func, list1)

# 4. 验收成果
print(result)
print(list(result))

# reduce(func(x,y)，lst)，其中func必须有两个参数。每次func计算的结果继和序列的下一个元素做累积计算。
list1 = [1, 2, 3, 4, 5]


# 1. 导入模块


# 2. 定义功能函数
def func(a, b):
    return a + b


# 3. 调用reduce，作用：功能函数计算的结果和序列的下一个数据做累计计算
result = functools.reduce(func, list1)
print(result)


#filter(func, lst)函数⽤于过滤序列列, 过滤掉不符合条件的元素, 返回⼀个 filter 对象,。如果要转换为列表, 可以使用 list() 来转换。
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. 定义功能函数：过滤序列中的偶数
def func(x):
    return x % 2 == 0


# 2. 调用filter
result = filter(func, list1)
print(result)

print(list(result))

