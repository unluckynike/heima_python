'''
@Project ：PythonDeom 
@File    ：if.py.py
@Author  ：hailin
@Date    ：2022/9/26 09:35 
@Info    : 
'''
import random

"""
  if 条件:
     code1
     code2
"""

if True:
    print("在缩进内")
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')
# 注意：在这个下方的没有加缩进的代码，不属于if语句块，即和条件成立与否无关

age = 22
if age < 18:
    print("未成年")
else:
    print("成年")

"""
上网实践 else
"""
age_enforement = int(input("输入年龄"))  # 输入接收到到是str
if age_enforement >= 18:
    print(f"年龄为{age_enforement}，可以上网")
else:
    print(f"未成年，不允许")

"""
工龄实践 elif  
"""
age1 = int(input("输入年龄"))
if age1 < 18:
    print(f"年龄{age1},童工")
elif age1 >= 18 and age1 < 60:  # elif 18 <= age <= 60:
    print(f"年龄{age1},劳工年龄")
elif age1 >= 60:
    print(f"年龄{age1}，退休")

"""
公交车实践 if嵌套
"""
money=1
set=1

if money==1:
    print("上车")
    if set==1:
       print("上车有座")
    else:
       print("无座")
else:
    print("没带钱，不上车，跑快点")

"""
随机数
"""
a=random.randint(0,2) # 0 1 2
b=random.randint(5,90)
print(a,b)

"""
三目运算
"""
"""
语法
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""
a = 1
b = 2

c = a if a > b else b
print(c)

# 需求： 有两个变量，比较大小 如果变量1 大于 变量2 执行 变量 1 - 变量2； 否则 变量2 - 变量1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)





