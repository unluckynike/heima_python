'''
@Project ：PythonDeom 
@File    ：if.py.py
@Author  ：hailin
@Date    ：2022/9/25 18:46 
@Info    : python基础第一天
'''

# 上传服务器切勿中文命名文件

# 单行输出
print("output")

# 简单注释

"""
多行注释
另一行注释
other
"""

print("hello python")
'''
注释一
注释二
'''

"""
1. 定义变量
    语法：变量名 = 值
  由数字、字⺟母、下划线组成
  不能数字开头
  不能使⽤用内置关键字
  严格区分⼤小写
 见名知义。
 大驼峰:即每个单词⾸首字⺟母都⼤大写，例如: MyName 。
 小驼峰:第二个(含)以后的单词首字母大写，例如: myName 。 
 下划线:例如: my_name 。
2. 使用变量
3. 看变量的特点
"""

# 定义变量：存储数据TOM
my_name = 'TOM'
print(my_name)

# 定义变量：存储数据 黑马程序员
schoolName = '我是黑马程序员，我爱Python'
print(schoolName)

# 认识数据类型 验证数据类型 --type（） 数值 布尔 字符串 列表 字典  集合 元组

#int
numbers1=1
#float
numbers2=1.1
print(type(numbers1))
print(type(numbers2))

#str
str="study python"
print(type(str))

#bool
flag=False
print(type(flag))

#list
list=[10,20,30]
print(type(list))

#tuple
tuple=(10,20,30)
print(type(tuple))

#set
set={10,20,30}
print(type(set))

#dict
dict={'name':'halen','age':'18'}
print(dict)
print(type(dict))
