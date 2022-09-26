'''
@Project ：PythonDeom 
@File    ：dataTypeTrans.py
@Author  ：hailin
@Date    ：2022/9/26 08:41 
@Info    : 数据类型转换 运算符
'''

"""
int(x [,base ]) 将x转换为一个整数
float(x ) 将x转换为一个浮点数
eval(str ) 用来计算在字符串中的有效Python表达式,并返回⼀个对象
"""

# num = input('输入数字:')
# print('未转换', num, type(num))  # str
# print('转换', int(num), type(int(num)))

# 1. float() -- 将数据转换成浮点型
num1 = 1
str1 = '10'
print(type(float(num1)))  # float
print(float(num1))  # 1.0

print(float(str1))  # 10.0

# 2. str() -- 将数据转换成字符串型
print(type(str(num1)))  # str

# 3. tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))

# 4. list() -- 将一个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))

# 5. eval() -- 计算在字符串中的有效Python表达式,并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

"""
  算数运算符 // 整除  **指数  混合运算优先级顺序：()⾼于 ** 高于 * / // % 高于 + -
  赋值运算符
  复合赋值运算符 
  ⽐较运算符
  逻辑运算符
"""
# 单变量赋值
temp = 50
print(temp)

# 多变量赋值
num_1, flaot_1, str_1 = 1, 2.0, 'abc'
print(f'{num_1, flaot_1, str_1}')

# 多变量赋相同值
a = b = c = 20
print(f'{a, b, c}')

"""
复合赋值运算符
"""
print("复合赋值运算符")
a = 10
a += 1  # a = a + 1
print(a)

b = 10
b -= 1  # b = b - 1
print(b)

# 注意： 先算复合赋值运算符右面的表达式； 算复合赋值运算
c = 10
# c = 10 + 1 + 2
# c += 3 -- c = c + 3
c += 1 + 2
print(c)

d = 10
d *= 1 + 2
print(d)

"""
比较运算符
"""
print("比较运算符")
a = 7
b = 5
print(a == b)  # False
print(a != b)  # True
print(a < b)  # False
print(a > b)  # True
print(a <= b)  # False
print(a >= b)  # True

"""
逻辑运算符
"""
print("逻辑运算符")
a = 0
b = 1
c = 2

# 1. and: 与: 都真才真
print((a < b) and (c > b))
print(a > b and c > b)

# 2. or：或 : 一真则真，都假才假
print(a < b or c > b)
print(a > b or c > b)

# 3. not： 非: 取反
print(not False)
print(not c > b)

a, b, c = 1, 2, 3
# and运算符，只要有⼀一个值为0，则结果为0，否则结果为最后⼀一个⾮非0数字 print(a and b) # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1
# or运算符，只有所有值为0结果才为0，否则结果为第⼀一个⾮非0数字 print(a or b) # 1
print(a or c)  # 2
print(b or c)  # 1
