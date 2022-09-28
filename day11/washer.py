'''
@Project ：PythonDeom 
@File    ：washer.py
@Author  ：hailin
@Date    ：2022/9/28 22:35 
@Info    : 
'''


# 1. 定义类：带参数的init：宽度和高度； 实例方法：调用实例属性
class Washer():
    # 定义初始化功能的函数  添加实例例属性
    """
    __init__() ⽅法，在创建一个对象时默认被调用，不需要手动调用
   __init__(self) 中的self参数，不需要开发者传递，python解释器会自动把当前的对象引⽤传递过去。
    """

    def __init__(self, width, height):  # 在Python中， __xx__() 的函数叫做魔法方法，指的是具有特殊功能的函数。
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}, 洗衣机的高度是{self.height}')

    # 当使⽤print输出对象的时候，默认打印对象的内存地址。如果类定义了了 __str__ 方法，那么就会打印从 在这个方法中 return 的数据。
    def __str__(self):
        return '解释说明：类的说明或对象状态的说明'

   # 当删除对象时，python解释器也会默认调用 __del__() 方法。
    def __del__(self):
        print(f'{self}对象已经被删除')



# 2. 创建对象，创建多个对象且属性值不同；调用实例方法
haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(100, 200)
haier2.print_info()


# str
haier = Washer(300,900)
print(haier)

del haier
