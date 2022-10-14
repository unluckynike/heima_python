
'''
@Project ：PythonDeom 
@File    ：files.py
@Author  ：hailin
@Date    ：2022/9/28 22:03 
@Info    : ⽂件和文件夹的操作
'''

# 导⼊os模块
import os

# os.函数名()
# os.mkdir('mkdir') # 新建文件夹

# os.rename('mkdir.txt','mkdirss')

# os.rmdir('mkdirss') # 删除文件夹
# f=open('temp.txt','w')
# os.remove('temp.txt') # 删除文件

print(os.getcwd()) # 获取当前目录
print(os.listdir('mkdir')) # 获取文件目录