'''
@Project ：PythonDeom 
@File    ：mulitExtend.py
@Author  ：hailin
@Date    ：2022/9/29 09:40 
@Info    : 多继承
'''


# class Master:
#     def __init__(self):
#         self.name = 'master'
#
#     def print_master(self):
#         print(f'this is {self.name}')
#
#
# class School:
#     def __init__(self):
#         self.name = 'school'
#
#     def print_school(self):
#         print(f'this is {self.name}')
#
#
# # 多继承
# class Prentice(School, Master):
#     pass
#
#
# tudi = Prentice()
#
# tudi.print_school()
# tudi.print_master()


# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义徒弟类，继承师父类 和 学校类
class Prentice(School, Master):
    pass


# 3. 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()


# 结论：如果一个类继承多个父类，优先继承第一个父类的同名属性和方法
