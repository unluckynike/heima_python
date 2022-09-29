'''
@Project ：PythonDeom 
@File    ：definExcept.py
@Author  ：hailin
@Date    ：2022/9/29 15:29 
@Info    :  自定义异常
'''


# 在Python中，抛出⾃定义异常的语法为 raise 异常类对象 。
# 需求:密码长度不足，则报异常(⽤户输入密码，如果输入的长度不足3位，则报错，即抛出⾃定义异 常，并捕获该异常)。
# 1. 自定义异常类， 继承Exception， 魔法方法有init和str(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self):
        return f'您输入的密码长度是{self.length}, 密码不能少于{self.min_len}'


def main():
    # 2. 抛出异常: 尝试执行：用户输入密码，如果长度小于3，抛出异常
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            # 抛出异常类创建的对象
            raise ShortInputError(len(password), 3)
    # 3. 捕获该异常
    except Exception as result:
        print(result)
    else:
        print('没有异常，密码输入完成')


main()
