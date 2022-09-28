'''
@Project ：PythonDeom 
@File    ：oo.py.py
@Author  ：hailin
@Date    ：2022/9/28 22:19 
@Info    : 面向对象
'''
# 需求：洗衣机，功能：能洗衣服
# 1. 定义洗衣机类
"""
class 类名():
    代码
"""


class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)  # 由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象


# 2. 创建对象
# 对象名 =  类名()
haier = Washer()

# 3. 验证成果
# 打印haier对象
print(haier)  # 引用地址

# 使用wash功能 -- 实例方法/对象方法 -- 对象名.Wash()
haier.wash()

# 1. 一个类可以创建多个对象； 2. 多个对象都调用函数的时候，self地址是否相同
print("=" * 10, 'hair1', "=" * 10)
haier1 = Washer()
haier1.wash()

print("=" * 10, 'hair2', "=" * 10)
haier2 = Washer()
haier2.wash()

"类外⾯面获取对象属性"
# 添加属性  对象名.属性名 = 值
haier1.width = 400
haier1.height = 500

# 获取属性 对象名.属性名
print(f'洗衣机的宽度是{haier1.width}')
print(f'洗衣机的高度是{haier1.height}')


"""
1. 定义类
    init魔法方法： width 和 height
    添加实例方法：访问实例属性

2. 创建对象
3. 验证成果
    调用实例方法
"""
print("=" * 10, 'AirConditioner', "=" * 10)
class AirConditioner():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'空调的宽度是{self.width}')
        print(f'空调的高度是{self.height}')


air = AirConditioner()

air.print_info()

