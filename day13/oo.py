'''
@Project ：PythonDeom 
@File    ：oo.py.py
@Author  ：hailin
@Date    ：2022/9/29 12:26 
@Info    : 面向对象
'''
"""
面向对象的三大特性
封装
     将属性和⽅法书写到类的里面的操作即为封装
     封装可以为属性和方法添加私有权限
  继承
     ⼦类默认继承父类的所有属性和方法
     子类可以重写⽗类属性和方法
  多态
     传⼊不同的对象，产生不同的结果
"""

"""
多态指的是一类事物有多种形态，(一个抽象类有多个子类，因而多态的概念依赖于继承)。
  定义:多态是⼀种用对象的方式，子类重写父类方法，调⽤不同子类对象的相同⽗类方法，可以产⽣不同的执行结果
  好处:调⽤灵活，有了多态，更容易编写出通用的代码，做出通⽤的编程，以适应需求的不断变化!
实现步骤:
     定义类，并提供公共方法
     定义子类，并重写父类方法
     传递子类对象给调用者，可以看到不同子类执行效果不同
"""


# 需求：警务人员和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作


# 1. 定义父类，提供公共方法： 警犬 和 人
class Dog(object):
    def work(self):
        pass


# 2. 定义子类，子类重写父类方法：定义2个类表示不同的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人...')


class DrugDog(Dog):
    def work(self):
        print('追查毒品...')


# 定义人类
class Person(object):
    def work_with_dog(self, dog):
        dog.work()


# 3. 创建对象，调用不同的功能，传入不同的对象，观察执行的结果
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)


"""
设置和访问类属性
"""

# 1. 定义类，定义类属性
class Dog(object):
    tooth = 10


# 2. 创建对象
wangcai = Dog()
xiaohei = Dog()

# 3. 访问类属性： 类和对象
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
# 类的实例 记录的某项数据 始终保持一致时，则定义类属性。
# 实例属性 要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有 ，仅占用一份内存，更加节省内存空间。

# 修改类属性
# 2. 测试通过对象修改类属性
wangcai.tooth = 200

print(Dog.tooth)  # 10
print(wangcai.tooth)  # 200
print(xiaohei.tooth)  # 10


# 类方法
# 1. 定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 1000

    # 定义类方法 第一个形参是类对象的⽅法
    # 需要用装饰器 @classmethod 来标识其为类方法，对于类方法，第⼀个参数必须是类对象一般以 cls 作为第⼀个参数。
    @classmethod
    def get_tooth(cls):
        return cls.__tooth


# 2. 创建对象，调用类方法
wangcai = Dog()
result = wangcai.get_tooth()
print(result)


"""
静态方法
"""

# 1. 定义类，定义静态方法
class Dog(object):
    #需要通过装饰器 @staticmethod 来进⾏修饰，静态⽅法既不需要传递类对象也不需要传递实例对象 (形参没有self/cls)。
    # 静态方法 也能够通过 实例对象 和 类对象 去访问。
    @staticmethod
    def info_print():
        print('这是一个静态方法')


# 2. 创建对象
wangcai = Dog()

# 3. 调用静态方法：类 和 对象
# 静态方法既可以使用对象访问⼜可以使用类访问
wangcai.info_print()
Dog.info_print()



