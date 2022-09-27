'''
@Project ：PythonDeom 
@File    ：dict.py.py
@Author  ：hailin
@Date    ：2022/9/27 16:22 
@Info    : 字典
'''

# 字典，字典⾥面的数据是以键值对形式出现，字典数据和数据顺序没有关系，即字典不支持下标，
# 后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。
"""
字典特点:
符号为大括号
数据为键值对形式出现 
各个键值对之间⽤用逗号隔开
"""
# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(type(dict1))
# 空字典
dict2 = {}
print(type(dict2))
dict3 = dict()
print(type(dict3))
print(dict1, dict2, dict3)

"""
常见操作
"""
# 增 写法:字典序列列[key] = 值
dict = {'name': 'TOM', 'age': 20, 'gender': '男'}
dict['id'] = 111
print(dict)

# 删 del() / del:删除字典或删除字典中指定键值对。
del dict['age']
print(dict)

dict.clear()  # 清空字典
print(dict)

dict = {'name': 'TOM', 'age': 20, 'gender': '男', 'id': 110}
# 修改 字典序列列[key] = 值
dict['name'] = 'Alice'
print(dict)

# 查找 按照键查找
print(dict['age'], dict['gender'])  # 如果当前查找的key存在，则返回对应的值;否则则报错。
# get  字典序列.get(key, 默认值)
print(dict.get('name'))

print('keys : ', dict.keys())
print('values : ', dict.values())
print('items : ', dict.items())

"""
遍历
"""
dict = {'name': 'TOM', 'age': 20, 'gender': '男'}
for k in dict.keys():
    print(k, end="\t")

print()
for v in dict.values():
    print(v, end="\t")

print()
for item in dict.items():
    print(item)

print()
for k, v in dict.items():
    print(f'key: {k}, value: {v}。')
