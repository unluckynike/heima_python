'''
@Project ：PythonDeom 
@File    ：forAndWhile.py.py
@Author  ：hailin
@Date    ：2022/9/26 16:04 
@Info    : 循环
'''

"""
while 条件:
    条件成立要重复执行的代码
    ......
"""
i = 1
while i <= 5:
    i += 1
    print(f"i={i}")
print("while end")

"""
1-100数字累加和 -- 1 + 2 + 3 + 4...+ 100 = 结果，打印结果
"""
i = 0
result = 0
while i <= 100:
    result += i
    i += 1
print(f"result value:{result}")

"""
1-100偶数累加和 -- 2 + 4 + 6 + 。。。+ 100 = 结果 -- 输出结果
"""
i = 0
result = 0
while i <= 100:
    if not i % 2:  # i%2==0
        result += i
    i += 1
print(f"result value:{result}")

"""
1-100偶数累加和 -- 2 + 4 + 6 + 。。。+ 100 = 结果 -- 输出结果 计数器实现
"""
i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print(f"result value:{result}")

"""
break：当某些条件成立，退出整个循环
循环吃5个苹果，吃完第3个吃饱了，第4 和 5 不吃了（不执行） -- == 4 或 >3
"""
eatApple = 0
while eatApple <= 5:
    print(f"eat apple 🍎 num:{eatApple}")
    if eatApple == 3:
        print(f"num:{eatApple},full can not eat")
        break
    eatApple += 1

"""
continue : 当条件成立，退出当前一次循环，继而执行下一次循环
吃5个苹果 -- 循环； 吃到第3个吃出一个虫子，第三个不吃了，没吃饱，继续吃4和5个苹果 -- 只有第三个不吃
"""
eatApple = 0
while eatApple <= 5:
    print(f"eat apple num:{eatApple}")
    if eatApple == 3:
        print(f"num:{eatApple} worm 🐛 ")
        # 如果使用continue，在continue之前一定要修改计数器，否则进入死循环
        eatApple += 1
        continue
    eatApple += 1

"""
1. 循环打印3次媳妇儿，我错了
2. 今天刷晚饭的碗
3. 上面是一套惩罚，这一套惩罚要重复执行3天 -- 一套惩罚要重复执行 -- 放到一个while循环里面
"""
i=0
j=0
while i<=3:
    while j<=3:
        print("punish")
        j+=1
    print("my fault")
    i+=1

"""
1. 打印1个星星
2. 一行5个： 循环 -- 5个星星在一行显示
3. 打印5行星星： 循环 -- 一行5个
"""
i=1
while i<=5:
    j=0
    while j<=4:
        print("*",end=" ")
        j+=1
    print()
    i+=1

"""
三角形： 每行星星的个数和行号数相等
"""
i=0
while i<=5:
    # 一行星星开始
    j=0
    while j<=i:
        print("*" ,end=" ")
        j+=1
    # 一行星星结束：换行显示下一行
    print()
    i+=1

"""
多行多个乘法表达式 x * x = x*x
1. 打印一个乘法表达式：x * x = x*x
2. 一行打印多个表达式 -- 一行表达式的个数和行号数相等 -- 循环： 一个表达式 -- 不换行
3. 打印多行表达式 -- 循环 ： 一行表达式 -- 换行
**** 一行表达式的个数和行号数相等
"""
i=1
while i<=9:
    j=1
    while j<=i: # 主要这个条件
        print(f"{i} * {j} = {i*j}",end="\t")
        j+=1
    print()
    i+=1



