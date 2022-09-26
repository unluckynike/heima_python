'''
@Project ：PythonDeom 
@File    ：str.py.py
@Author  ：hailin
@Date    ：2022/9/26 17:56 
@Info    : 字符串
'''

str1 = "hello " \
       "python"
str2 = 'abcd'
str3 = '''三引号字符串'''
str4 = """sss """
print(type(str1), type(str2), type(str3), type(str4))
print(str1)  # 单引换行

str5 = """ I 
am halen"""
print(str5)  # 三引换行

str6 = 'I \'m halen'  # 斜杠转义
print(str6)

"""
格式化输出
"""
print("hello world")
name = 'ROSE'
# 我的名字是TOM
print('我的名字是%s' % name)
print(f'我的名字是{name}')

"""
字符串输入
"""
# 输入密码
password = input('请输入您的密码：')
print(f'您输入的密码是:{password}')
print(type(password))

"""
下标 索引
 数据在程序运行过程中存储在内存
 得到数据a字符， 得到数据b字符 --   使用字符串中某个特定的数据
 这些字符数据从0开始顺序分配一个编号 -- 使用这个编号精确找到某个字符数据 -- 下标或索引或索引值
 str1[下标]
"""
str6 = "abcdefg"
print(str6[0])  # a
print(str6[3])  # d

"""
切片
  序列[开始位置下标:结束位置下标:步长]
  1. 不包含结束位置下标对应的数据， 正负整数均可; 
  2. 步长是选取间隔，正负整数均可，默认步长为1。
"""
str7 = "abcdefg"
print(str7[1:3])  # bc
print("====切片====")
name = "abcdefg"
print(name[2:5:1])  # cde
print(name[2:5])  # cde
print(name[:5])  # abcde
print(name[1:])  # bcdefg
print(name[:])  # abcdefg
print(name[::2])  # aceg
print(name[:-1])  # abcdef  负1表示倒数第一个数据 print(name[-4:-1]) # def
print(name[::-1])  # gfedcba 倒序

str1 = '012345678'
print(str1[2:5:1])  # 234
print(str1[2:5:2])  # 24
print(str1[2:5])  # 234
print(str1[:5])  # 01234 -- 如果不写开始，默认从0开始选取
print(str1[2:])  # 2345678 -- 如果不写结束，表示选取到最后
print(str1[:])  # 012345678 -- 如果不写开始和结束，表示选取所有

# 负数测试
print(str1[::-1])  # 876543210 -- 如果步长为负数，表示倒叙选取
print(str1[-4:-1])  # 567 -- 下标-1表示最后一个数据，依次向前类推

# 终极测试
print(str1[-4:-1:1])  # 567
print(str1[-4:-1:-1])  # 不能选取出数据：从-4开始到-1结束，选取方向为从左到右，但是-1步长：从右向左选取
#  如果选取方向(下标开始到结束的方向) 和 步长的方向冲突，则无法选取数据
print(str1[-1:-4:-1])  # 876
