'''
@Project ：PythonDeom 
@File    ：file1.py
@Author  ：hailin
@Date    ：2022/9/28 21:05 
@Info    : 
'''

f = open('test1.txt')

print(f.read())

# 改变读取数据开始位置 ⽂件对象.seek(偏移量量, 起始位置)
# 0:文件开头 1:当前位置 2:文件结尾

f.seek(0, 0)  # 上面一行已经将光标移动到了末尾 需要加上seek 不然会读出空

con = f.readline()
print('1 line: ', con)
content = f.readline()
print(f'第一行:{content}')
content = f.readline()
print(f'第二行:{content}')
print(f.readlines())
# 关闭⽂文件
f.close()
