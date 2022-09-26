'''
@Project ：PythonDeom 
@File    ：exp1.py
@Author  ：hailin
@Date    ：2022/9/26 14:51 
@Info    :  猜拳实践
'''

import random

"""
0--石头；1--剪刀；2--布
"""
computer = random.randint(0, 2)  # comp num
print(computer)
gamer = int(input("gamer input ："))

#gamer win
if (gamer==0 and computer==1)|(gamer==1 and computer==2)|(gamer==2 and computer==0):
    print("gamer win")
elif computer==gamer:
    print("mean")
else:
    print("computer win")
