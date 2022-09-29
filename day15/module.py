'''
@Project ：PythonDeom 
@File    ：module.py.py
@Author  ：hailin
@Date    ：2022/9/29 15:46 
@Info    : 
'''

# Python 模块(Module)，是一个 Python文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
# 模块能定义函数，类和变量，模块里也能包含可执行的代码。

"""
import 模块名
from 模块名 import 功能名
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名


# 1. 导⼊入模块
import 模块名
import 模块名1, 模块名2...
# 2. 调⽤用功能 模块名.功能名()

"""

import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(9))

# 模块别名
import time as  tt
tt.sleep(3)
print('sleep(3)')
# 功能别名
from time import sleep as sl
sl(1)
print('sl(1)')


from math import *
print(abs(-9.8))

# 自定义模块
import module1
# 调用自定义模块
module1.testA(2,6)

# 方法一
"""
1. 导入
import 包名.模块名
2. 调用功能
包名.模块名.功能()
"""
# 导入mypackage包下的模块1，使用这个模块内的info_print1函数
# import mypackage.my_module1
# mypackage.my_module1.info_print1()


# 方法二：注意 设置__init__.py文件里面的all列表，添加的是允许导入的模块
"""
from 包名 import *
模块名.目标
"""
from module2 import *
testA()

# 因为testB函数没有添加到all列表，只有all列表里面的功能才能导入
# testB()









