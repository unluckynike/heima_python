'''
@Project ：PythonDeom 
@File    ：renameFiles.py
@Author  ：hailin
@Date    ：2022/9/28 22:14 
@Info    :  批量重命名文件
'''

import os

# 设置重命名标识:如果为1则添加指定字符，flag取值为2则除指定字符
flag = 1
# 获取指定目录
dir_name = './'
# 获取指定⽬录的文件列列表
file_list = os.listdir(dir_name)
print('old file name : ', file_list)

for name in file_list:
    # 添加指定字符
    if flag == 1:
        new_name = 'Python-' + name
        # 除指定字符
    elif flag == 2:
        num = len('Python-')
        new_name = name[num:]
    # 打印新⽂文件名，测试程序正确性
    print('new file name : ', new_name)
    # 重命名
    os.rename(dir_name + name, dir_name + new_name)
