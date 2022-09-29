'''
@Project ：PythonDeom 
@File    ：overwride.py
@Author  ：hailin
@Date    ：2022/9/29 09:50 
@Info    : 重写
'''


class Master:
    def __init__(self):
        self.name = 'master'

    def print_info(self):
        print(f'this is {self.name}')


class School:
    def __init__(self):
        self.name = 'school'

    def print_info(self):
        print(f'this is {self.name}')


class Prentice(School, Master):
    def __init__(self):
        self.name = 'prentice'

    # ⼦类重写父类同名方法和属性
    def print_info(self):
        print(f'this is {self.name}')

    def print_master_info(self):
        Master.__init__(self)
        Master.print_info(self)

    def print_school_info(self):
        School.__init__(self)
        School.print_info(self)


p = Prentice()

p.print_info()  # 打印自己的方法

print(Prentice.__mro__)  # 打印继承层级顺序


p.print_school_info()
p.print_master_info()

print('='*10+'多继承'+'='*10)
# 多继承
class Tusun(Prentice):
    pass
t = Tusun()
t.print_info()
t.print_master_info()
t.print_school_info()

