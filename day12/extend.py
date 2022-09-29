'''
@Project ：PythonDeom 
@File    ：extend.py.py
@Author  ：hailin
@Date    ：2022/9/28 22:51 
@Info    : 继承
'''

"""
在Python中，所有类默认继承object类，object类是顶级类或基类;其他子类叫做派生类。

class 类名: 代码
       ......
      
继承的类       
class 类名(object): 
      代码
"""


# 1. 定义父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)
        print('父类方法')


# 2. 定义子类 继承父类
class B(A):  # B继承自A
    pass
    # def info_print(self):
    #     print('子类方法')


# 3. 创建对象，验证结论
result = B()
result.info_print()


# 单继承
class Master(object):
    def __init__(self):
        self.kongfu = 'tradition kongfu'

    def mack_cake(self):
        print(f'{self.kongfu}')


class Prentice(Master):
    pass


tudi=Prentice()
# print(tudi.kongfu)
tudi.mack_cake()
#
# tudi.practice