'''
@Project ：PythonDeom 
@File    ：file.py.py
@Author  ：hailin
@Date    ：2022/9/28 10:20 
@Info    : 文件
'''

# open(name,mode)
# name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
# mode:设置打开文件的模式(访问模式):只读、写入、追加等。

# 1. 打开 open()
f = open('test.txt', 'w') # 没有则创建文件

# 2. 读写操作 write() read()
# 对象.write('内容')
f.write('aaasss')

# 3. 关闭 close()
f.close()


"""
测试目标
1. 访问模式对文件的影响
2. 访问模式对write()的影响
3. 访问模式是否可以省略
"""

"""
w和a模式:如果文件不存在则创建该文件;如果⽂件存在，w模式先清空再写入，a模式 直接末尾追加。
r模式:如果文件不存在则报错。
"""
# r: 如果文件不存在，报错；不支持写入操作，表示只读
# f = open('test1.txt', 'r')
# f = open('test.txt', 'r')
# f.write('aa')
# f.close()

# w：只写, 如果文件不存在，新建文件；执行写入，会覆盖原有内容
f = open('1.txt', 'w')
f.write('bbb')
f.close()

# a：追加，如果文件不存在，新建文件；在原有内容基础上，追加新内容
f = open('2.txt', 'a')
f.write('xyz') # 再次执行会追加内容
f.close()

# 访问模式参数可以省略, 如果省略表示访问模式为r
f = open('1.txt')
f.close()


f = open('test.txt', 'r')

# 文件内容如果换行，底层有\n，会有字节占位，导致read书写参数读取出来的看到的个数和参数值不匹配
# read不写参数表示读取所有；
print('read:',f.read())
print('read(10)',f.read(10))

f.close()

# readlines可以按照行的⽅式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
f = open('test.txt', 'r')
con = f.readlines()
print(con)

f.close()






