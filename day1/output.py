'''
@Project ：PythonDeom 
@File    ：output.py
@Author  ：hailin
@Date    ：2022/9/26 08:00 
@Info    : 输出输入
'''

"""
%s 字符串
%d 有符号的⼗进制整数 
%f 浮点数
其他不常用
%c %u %o %x %X %e %E %g %G
"""

age = 10
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 10102

# 填充数据
print('我的年龄是%d岁' % age)
print('我的名字是%s' % name)
# %.2f，表示⼩小数点后显示的⼩小数位数。
print("体重为%.2f公斤" % weight)
# %06d，表示输出的整数显示位数，不不⾜足以0补全，超出当前位数则原样输出
print('学号为%06d' % stu_id)
print('另一个学生的学号%06d' % stu_id2)
# 5. 我的名字是x，今年x岁了
print('我的名字是%s，今年%d岁了' % (name, age))

# 5.1 我的名字是x，明年x岁了
print('我的名字是%s，明年%d岁了' % (name, age + 1))
# 格式化多值输出
print("我的学号是%06d，姓名%s，今年%d，体重为%.2f公斤" % (stu_id, name, age, weight))

name1 = 'helen'
age = 20
weight = 60
stu_id1 = 4
# %统一用 %s 输出
print('我的学号是%s，姓名%s，今年%s，体重为%s公斤' % (stu_id1, name1, age, weight))

# f格式化输出 语法 f'{表达式}'  f-格式化字符串是Python3.6中新增的格式化方法，该方法更更简易易读。
print(f'我的学号是{stu_id1}，姓名{name}，今年{age}，体重为{weight}公斤')

"""
转义字符 
\n :换⾏行行。
\t :制表符，⼀一个tab键(4个空格)的距离。
在Python中，print()， 默认⾃带 end="\n" 这个换行结束符，所以导致每两个 print 直接会换行展示，⽤户可以按需求更改结束符。
"""

# 没有转义
print('hello')
print('python')
print('abc')
# 转义字符
print('hello\npython')
print('a\tb\tc\t')

# 结束符
print('输出的内容')
print('hello', end='\n')
print('world', end='\t')
print('hello', end='...')  # 自定义
print('python')

"""
输入 input("提示信息")
当程序执⾏行到 input ，等待⽤户输⼊入，输入完成之后才继续向下执行。 
在Python中， input 接收⽤户输⼊入后，⼀一般存储到变量，⽅便使用。 
在Python中， input 会把接收到的任意用户输⼊的数据都当做字符串处理。
"""
temp_input = input('please input')
print(f'你输入了:{temp_input}')
