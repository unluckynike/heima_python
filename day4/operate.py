'''
@Project ：PythonDeom 
@File    ：operate.py
@Author  ：hailin
@Date    ：2022/9/26 22:34 
@Info    : 字符串常用操作方法 查找 修改 判断 三大类
'''

str = "hello world and itcast and itheima and Python"
"""
查找
"""
print("str len:", len(str))
# 字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
print(str.find("and"))  # 下标12开始 字串 and
print(str.find("and", 15, 45))
print(str.find("and", 26, 45))
print(str.find("ands"))  # 没有找到 返回-1

# 字符串序列.index(⼦串, 开始位置下标, 结束位置下标)
print(str.index("and"))
print(str.index("world", 5, 45))
# print(str.index("worlds", 5, 45))  # 如果在返回这个⼦串开始的位置下标，否则则 报异常。
# rfind(): 和find()功能相同，但查找⽅方向为右侧开始。
# rindex():和index()功能相同，但查找⽅方向为右侧开始。

print(str.rfind('and'))
print(str.rfind('ands'))

print(str.rindex('and'))
# print(str.rindex('ands')) # 如果在返回这个⼦串开始的位置下标，否则则 报异常。

# 字符串序列.count(子串, 开始位置下标, 结束位置下标)
print(str.count("and"))  # 有三个 and 子串
print(str.count("ands"))  # 没有子串

"""
修改
"""
# 字符串序列.replace(旧⼦串, 新子串串, 替换次数)
print(str.replace('and', 'AND', 1))  # 第一个and 换成了大写
# 数据按照是否能直接修改分为可变类型和不可变类型两种。字符串类型的数据修改的时候 不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型。
print(f'🤔origin str: {str}')
new_str = str.replace('and', 'AND', 1)
print(f'🤔new str: {new_str}')

# 字符串序列.split(分割字符, num)
print(str.split('and', 1))  # 去掉了第一个 and 子串 ,不写num则所有都分割 会丢失分割符
print(str.split('and'))  # 不写num则所有都分割 会丢失分割符
print(type(str.split('and', 1)))  # 列表 list 类型

# 字符或⼦串.join(多字符串组成的序列)
join_list = ['aa', 'bb', 'cc']
print(".....".join(join_list))
print(str)
print(str.join(join_list))

# capitalize():将字符串第一个字符转换成大写。
# title():将字符串每个单词首字母转换成⼤写。
# lower():将字符串中大写转⼩写。
# upper():将字符串中小写转大写。
print(str)
print(str.capitalize())
print(str.title())
print(str.lower())
print(str.upper())

mystr = "   hello world and itcast and itheima and Python   "
print(mystr, len(mystr))
# 1. lstrip(): 删除左侧空白字符
new_str = mystr.lstrip()
print(new_str)
# 2. rstrip(): 删除右侧空白字符
new_str = mystr.rstrip()  # 鼠标点击查看末尾空百
print(new_str, len(new_str))
# 3.strip()：删除两侧空白字符
new_str = mystr.strip()
print(new_str)

# ljust rjust center


"""
判断
"""
mystr = "hello world and itcast and itheima and Python"

# 1. startswith(): 判断字符串是否以某个子串开头
# 字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标)
print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('hels'))

# 2. endswith(): 判断字符串是否以某个子串结尾
# 字符串序列.endswith(⼦串, 开始位置下标, 结束位置下标)
print(mystr.endswith('Python'))
print(mystr.endswith('Pythons'))

# 3. isalpha(): 字母
print('isalpha: ',mystr.isalpha())

# 4. isdigit(): 数字
print(mystr.isdigit())
mystr1 = '12345'
print(mystr1.isdigit())

# 5. isalnum() : 数字或字母或组合
print(mystr1.isalnum())
print(mystr.isalnum())
mystr2 = 'abc123'
print(mystr2.isalnum())

# 6.isspace(): 空白
print(mystr.isspace())
mystr3 = '   '
print(mystr3.isspace())

