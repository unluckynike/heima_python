'''
@Project ：PythonDeom 
@File    ：excp.py.py
@Author  ：hailin
@Date    ：2022/9/29 15:09 
@Info    : 异常
'''
import time

"""
异常语法
try: 
    可能发⽣生异常的代码
except:
     如果出现异常执⾏行行的代码
else: 
     没有异常执⾏行行的代码
finally: 
     ⽆无论是否异常都要执⾏行行的代码


异常捕捉
except 异常类型: 
       代码
except 异常类型 as xx: 
       代码     


自定义异常
# 1. ⾃自定义异常类
class 异常类类名(Exception):
        代码
# 设置抛出异常的描述信息 
        def __str__(self):
          return ...
# 2. 抛出异常 
raise 异常类名()

# 捕获异常
except Exception...     

"""

# 当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的"异常"。
# 例如:以 r 方式打开一个不存在的文件。
# 需求：尝试打开test.txt（r），如果文件不存在，只写方式打开w
"""
try:
    可能发生错误的代码
except:
    发生错误的时候执行的代码
"""

try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')

# ZeroDivisionError: division by zero
# print(1 / 0)

try:
    print(num)
except NameError:
    print('有错误')

# 需求：尝试执行打印num，捕获异常类型NameError，如果捕获到这个异常类型，执行打印：有错误
try:
    # print(num)
    print(1 / 0)
except ZeroDivisionError:  # except接错误类型
    print('有错误')
# 1. 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
# 2. ⼀般try下⽅只放⼀⾏尝试执⾏的代码。


# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except 后，并使⽤元组的方式进行书写。
try:
    print(1 / 0)
except (NameError, ZeroDivisionError):
    print('有错误')

# 捕获异常描述信息
try:
    print(aaa)  # result ：name 'aaa' is not defined
    # print(1/0) # result ：division by zero
except (NameError, ZeroDivisionError) as result:
    print(result)  #

# 捕获所有异常 尝试执行打印num，捕获Exception 打印异常描述信息
try:
    print(num)
except Exception as result:
    print(result)

# 异常的else
# else表示的是如果没有异常要执行的代码。
try:
    print('no erro')
except Exception as result:
    print(result)
else:
    print('我是else，当没有异常的时候执行的代码')

# finally表示的是⽆论是否异常都要执行的代码，例如关闭文件。
# 需求：尝试以r打开文件，如果有异常以w打开这个文件，最终关闭文件
try:
    f = open('test100.txt', 'r')
except Exception as e:
    print(e)
    f = open('test100.txt', 'w')
finally:
    f.close()

# 需求1： 尝试只读打开test.txt 文件存在读取内容，不存在提示用户
# 需求2：读取内容：循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经被意外终止

try:
    f = open('test.txt')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成退出循环
            if len(con) == 0:
                break

            time.sleep(3)
            print(con)
    except:
        # 在命令提示符中如果按下ctrl+C结束终止的键
        print('程序被意外终止')
except:
    print('该文件不存在')

