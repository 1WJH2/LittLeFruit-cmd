import os
import subprocess
from time import sleep
import random
import shutil

echo_or = 'on'
random_mod_or = 'off'
exit_or = 'off'
cu = str(os.path.dirname(__file__))
print('''
LittLeFruit cmd''')

while True:
    a = input('> ')
    if '' != a:
        if 'add' == a.split()[0]:
            try:
                b = a.split()[1]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                open(b,'x')
                print('\033[32m命令执行成功\033[0m')
        elif 'help' == a or '帮助' == a:
            print('''
<>为 单选项,[]为 多选项,|为 或,::为 Python数据源(如:[], {}, ())
help|帮助 可获取命令帮助
ver|版本 显示版本信息
add|添加文件 <绝对路径> 
del|删除文件 <绝对路径>
sleep|等待 <时间>
open|打开 <类型> [<file>, <website>, <folder>] 
cd|切换目录 [操作] <路径>
    操作:
        show:显示当前目录
        /d:切换到绝对目录
        /:切换到相对目录
        /s:切换到上级目录
        /h:切换到根目录
show|显示 <内容>
random|随机数模块 <功能> [参数]
    随机数模块说明:
              randint|生成一个随机整数 <最小值> <最大值>
              choice|从列表中随机选取一个元素 <元素1> <元素2> ...

data|LittLeFruit cmd数据管理 <操作> <数据名> <值>
                          [set, show]
    数据值对照表:
            数据:
              tiles:窗口标题
            关联:
              @echo:是否显示命令输出
              @random_mod:是否启用随机数功能
              @exit:是否退出
cmd|打开新的LittLeFruit cmd窗口
command|执行系统命令 <命令>
copy|复制 <路径> <目标路径夹>
exit|退出程序
              
''')
        elif 'cmd' == a.split()[0]:
            subprocess.Popen('start cmd /k python main.py', shell=True)
        elif 'copy' == a.split()[0]:
            try:
                b = a.split()[1]
                c = a.split()[1]
            except:
                print('\033[31m参数错误\033[0m')  
            else:
                if os.path.isfile(b):
                    try:
                        shutil.copy(b,c)
                    except:
                        print('\033[31m没有此文件夹\033[0m')
                    else:
                        print('\033[92m操作成功\033[0m')
                else:
                    print('\033[31m没有此文件\033[0m')
        elif 'del' in a.split()[0]:
            try:
                b = a.split()[1] 
            except:
                print('\033[31m参数错误\033[0m')
            else:
                c = input('确定要删除吗? y/n:')
                if c == 'y' or c == 'Y':
                    os.remove(b)
                    print('\033[92m操作成功\033[0m')
        elif 'sleep' in a.split()[0]:
            try:
                b = a.split()[1]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                sleep(int(b))
        elif 'show' in a.split()[0]:
            try:
                b = a.split()[1]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                print(b)
        elif 'data' in a.split()[0]:
            try:
                b = a.split()[1]
                c = a.split()[2]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                if a.split()[1] == 'show':
                    if a.split()[2] == 'tiles':
                        print(str(os.path.basename(__file__)))
                    elif a.split()[2] == '@echo':
                        print(echo_or)
                    elif a.split()[2] == '@random_mod':
                        print(random_mod_or)
                    elif a.split()[2] == '@exit':
                        print(exit_or)
                elif a.split()[1] == 'set':
                    try:
                        b = a.split()[2]
                        c = a.split()[3]
                    except:
                        print('\033[31m参数错误\033[0m')
                    else:
                        if a.split()[2] == 'tiles':
                            print('不可设置窗口标题')
                        elif a.split()[2] == '@echo':
                            if a.split()[3] == 'on':
                                echo_or = 'on'
                                print('\033[92m操作成功\033[0m')
                            elif a.split()[3] == 'off':
                                echo_or = 'off'
                                print('\033[92m操作成功\033[0m')
                            else:
                                print('\033[31m没有此选项\033[0m')
                        elif a.split()[2] == '@random_mod':
                            if a.split()[3] == 'on':
                                random_mod_or = 'on'
                                print('\033[92m操作成功\033[0m')
                            elif a.split()[3] == 'off':
                                random_mod_or = 'off'
                                print('\033[92m操作成功\033[0m')
                            else:
                                print('\033[31m没有此选项\033[0m')
                        elif a.split()[2] == '@exit':
                            if a.split()[3] == 'on':
                                exit_or = 'on'
                                print('\033[92m操作成功\033[0m')
                                exit()
                            elif a.split()[3] == 'off':
                                exit_or = 'off'
                                print('\033[92m操作成功\033[0m')
                            else:
                                print('\033[31m没有此选项\033[0m')
        elif 'ver' == a :
            print('''
LittLeFruit cmd 
V1.2.1

版本日志:
              1.0.0:初始版本
              1.1.0:BUG修复
              1.1.4:添加了echo命令
              1.1.6:添加了随机数功能
              1.1.8:添加了数据管理功能
              1.2.0:添加了cmd命令,版本日志,exit功能,random功能
              1.2.1:修复了若干BUG, 添加open, cd, command, copy命令,把相对路径改为绝对路径,优化了代码结构
''')
        elif 'exit' == a:
            if exit_or == 'on':
                break
            else:
                print('\033[31mexit未启用此功能\033[0m')
        elif 'random' == a.split()[0]:
            try:
                b = a.split()[1]
                c = a.split()[2]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                if random_mod_or == 'on':
                    if a.split()[1] == 'randint':
                        try:
                            b = a.split()[2]
                            c = a.split()[3]
                        except:
                            print('\033[31m参数错误\033[0m')
                        else:
                            print(random.randint(int(b), int(c)))
                    elif a.split()[1] == 'choice':
                        try:
                            b = a.split()[2:]
                        except:
                            print('\033[31m参数错误\033[0m')
                        else:
                            print(random.choice(b))
                    else:
                        print('\033[31m未启用此功能\033[0m')
        elif 'open' in a.split()[0]:
            try:
                b = a.split()[1] 
                c = a.split()[2]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                if b == 'file':
                    if os.path.isfile(c):
                        os.startfile(c)
                        print('\033[92m操作成功\033[0m')
                    else:
                        print('\033[31m没有此文件\033[0m')
                elif b == 'url':
                    os.startfile(c)
                    print('\033[92m操作成功\033[0m')
                elif b == 'folder':
                    if os.path.isdir(c):
                        os.startfile(c)
                        print('\033[92m操作成功\033[0m')
                    else:
                        print('\033[31m没有此目录\033[0m')
        elif 'cd' in a.split()[0]:
            try:
                b = a.split()[1]
                c = a.split()[2]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                if a.split()[1] == 'show':
                    print(cu)
                elif a.split()[1] == '/d':
                    if os.path.isdir(c):
                        cu = c
                        print('\033[92m操作成功\033[0m')
                    else:
                        print('\033[31m没有此目录\033[0m')
                elif a.split()[1] == '/':
                    if os.path.isdir(os.path.join(cu, c)):
                        cu = os.path.join(cu, c)
                        print('\033[92m操作成功\033[0m')
                    else:
                        print('\033[31m没有此目录\033[0m')
                elif a.split()[1] == '/s':
                    if os.path.isdir(os.path.dirname(cu)):
                        cu = os.path.dirname(cu)
                        print('\033[92m操作成功\033[0m')
                    else:
                        print('\033[31m没有上级目录\033[0m')
                elif a.split()[1] == '/h':
                    if os.path.isdir(os.path.splitdrive(cu)[0] + '\\'):
                        cu = os.path.splitdrive(cu)[0] + '\\'
                        print('\033[92m操作成功\033[0m')
                    else:
                        print('\033[31m没有此目录\033[0m')
        elif 'command' in a.split()[0]:
            try:
                b = a.split()[1:]
            except:
                print('\033[31m参数错误\033[0m')
            else:
                os.system(' '.join(b))
        else:   
            print('\033[31m没有此命令\033[0m')
    else:
        pass
