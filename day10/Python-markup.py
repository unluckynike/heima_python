'''
@Project ：PythonDeom 
@File    ：markup.py
@Author  ：hailin
@Date    ：2022/9/28 21:23 
@Info    : 文件备份
'''

# 1.接收⽤户输⼊的文件名
# 2. 规划备份文件名
# 3. 备份文件写⼊数据

old_name = input("markup old file name: ")  # 输入 text1.txt

index = old_name.rfind('.')

print('.的下标：', index)  # 后缀中.的下标
print(old_name[:index])  # 源文件名

print('前缀文件名：', old_name[:index])
print('后缀文件类型：', old_name[index:])

if index > 0:
    postfix = old_name[index:]
else:
    print(f'无效文件: {old_name}')

# # 2.2 组织新⽂文件名 旧⽂文件名 + [备份] + 后缀
new_name = old_name[:index] + '备份' + postfix
print('新文件名：', new_name)

# 3.1 打开⽂文件
old_f = open(old_name, 'rb')  # rb以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
new_f = open(new_name, 'wb')  # 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。

#
while True:
    con = old_f.read(1024)  # 读到源文件内容
    if len(con) == 0:
        break
    new_f.write(con)  # 写入内容

# 3.3 关闭⽂文件
old_f.close()
new_f.close()
