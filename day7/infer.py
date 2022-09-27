'''
@Project ：PythonDeom 
@File    ：infer.py
@Author  ：hailin
@Date    ：2022/9/27 17:40 
@Info    :  推导式 生产式  更加复合python代码风格 化简代码量
  列表推导式
  字典推导式
  集合推导式
'''
# 需求:创建一个0-10的列表。
# while
list = []
i = 0
while i <= 10:
    list.append(i)
    i += 1
print(list)

# for
list = []
for i in range(0, 11, 1):
    list.append(i)
print(list)

# 列表推导式实现
list1 = [i for i in range(11)]
print(list1)

# 带if的列表推导式
# 需求：0-10偶数数据的列表
list2 = [i for i in range(0, 11, 2)]
print('range : ', list2)

# if 实现
list3 = [i for i in range(11) if i % 2 == 0]
print('if : ',list3)

# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 数据1 ： 1 和 2  range(1,3)
# 数据2 ：0 1 2  range(3)
list4=[]
for i in  range(1,3):
    for j in range(5):
        list4.append((i,j))
print(list4)

# 推导式
list5=[(i, j) for i in range(1, 3) for j in range(3)]
print(list5)






