'''
@Project ：PythonDeom 
@File    ：std.py.py
@Author  ：hailin
@Date    ：2022/9/28 08:59 
@Info    : 
'''


def print_info():
    print('-' * 20)
    print('欢迎登录学员管理理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


# 等待存储所有学员的信息
info = []


# print(type(info))

# 添加学员信息的函数
def add_info():
    # 1. 用户输入：学号、姓名、手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 2. 判断是否添加这个学员：如果学员姓名已经存在报错提示；如果姓名不存在添加数据
    global info
    # 2.1 不允许姓名重复：判断用户输入的姓名 和 列表里面字典的name对应的值 相等 提示
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            # return作用：退出当前函数，后面添加信息的代码不执行
            return

    # 2.2 如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)

    # 列表追加字典
    info.append(info_dict)
    print(info)


# 删除学员
def del_info():
    # 1. 用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员的姓名：')

    # 2. 判断学员是否存在：存在则删除；不存在提示
    # 2.1 声明info是全局变量
    global info
    # 2.2 遍历列表
    for i in info:
        # 2.3 判断学员是否存在：存在执行删除(列表里面的字典)，break：这个系统不允许重名，删除了一个后面的不需要再遍历；不存在提示
        if del_name == i['name']:
            # 列表删除数据 -- 按数据删除remove
            info.remove(i)
            break
    else:
        print('该学员不存在')

    print(info)


# 修改函数
def modify_info():
    # 1. 用户输入想要修改的学员您的姓名
    modify_name = input('请输入要修改的学员的姓名：')

    # 2. 判断学员是否存在：存在修改手机号；不存在，提示
    # 2.1 声明info是全局
    global info
    # 2.2 遍历列表，判断输入的姓名==字典['name']
    for i in info:
        if modify_name == i['name']:
            # 将tel这个key修改值，并终止此循环
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')

    # 3. 打印info
    print(info)


# 查询学员信息函数
def search_info():
    # 1. 用户输入目标学员姓名
    search_name = input('请输入要查询的学员的姓名：')

    # 2. 检查学员是否存在：存在打印这个学员的信息；不存在则提示
    # 2.1 声明info为全局
    global info
    # 2.2 遍历info，判断输入的学员是否存在
    for i in info:
        if search_name == i['name']:
            # 学员存在：打印信息并终止循环
            print('查询到的学员信息如下---------------')
            print(f"学员的学号是:{i['id']}, 姓名是:{i['name']}, 手机号是:{i['tel']}")
            break
    else:
        # 学员不存在的提示
        print('查无此人...')


# 显示所有学员信息
def print_all():
    """显示所有学员信息"""
    # 1. 打印提示字
    print('学号\t姓名\t手机号')
    # 2. 打印所有学员的数据
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


while True:
    print_info()
    user_num = input('请选择您需要的功能序号:')
    if user_num == '1':
        print('添加学员')
        add_info()
    elif user_num == '2':
        print('删除学员')
        del_info()
    elif user_num == '3':
        print('修改学员信息')
        modify_info()
    elif user_num == '4':
        print('查询学员信息')
        search_info()
    elif user_num == '5':
        print('显示所有学员信息')
        print_all()
    elif user_num == '6':
        # 程序要想结束，退出终止while True -- break
        exit_flag = input('确定要退出吗？yes or no')
        if exit_flag == 'yes':
            print('exist')
            break
    else:
        print('输⼊错误，请重新输入!!!')
