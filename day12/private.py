
'''
@Project ：PythonDeom 
@File    ：private.py
@Author  ：hailin
@Date    ：2022/9/29 10:40 
@Info    : 私有属性
'''

# 设置私有权限的⽅法:在属性名和⽅法名前面 加上两个下划线 __。

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
        # self.money = 2000000
        # 定义私有属性
        self.__money = 2000000

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


xiaoqiu = Tusun()

# print(xiaoqiu.money) # 'Tusun' object has no attribute 'money'
# print(xiaoqiu.__money) # 'Tusun' object has no attribute '__money'

# xiaoqiu.__info_print() # 私有方法


p= Prentice()
