import os
import shutil
import re

#关键字查找文件，不重新命名
def FindAndCopyMoveOne(path,str1):
    if not os.path.exists('.\\查找结果文件夹'):
        os.mkdir('.\\查找结果文件夹')
    global filecountforname
    global file_nothing_list
    filecountindir =0  #定义一个变量来统计找到的文件个数
    searchdir = os.path.relpath(path)  #定义一个变量显示查找的文件夹
    filefindedlist = []  #定义一个空列表来存储文件夹中找到的文件
    for x in os.listdir(path):
        next_file = os.path.join(path,x)
        if os.path.isfile(next_file):
            for keyword in str1:
                if keyword in x:
                    filecountforname += 1  #该变量用来重命名文件，防止重名！
                    filenamelist = x.split('.')  # 用来分解找到的文件名及其后缀名
                    newfilename = filenamelist[0]+str(filecountforname)+'.'+filenamelist[1]
                    shutil.copy(next_file,os.path.join('.\\查找结果文件夹',newfilename))
                    filefindedlist.append(newfilename)
                    filecountindir += 1
        else:
            FindAndCopyMoveOne(next_file,str1)
    if filecountindir == 0:
        file_nothing_list.append(searchdir)
    else:
        print('【{}】文件夹找到{}个文件'.format(searchdir, filecountindir))
        with open(r'.\查找结果文件夹\查找结果日志.txt','a+') as file:
            file.write('【{}】文件夹找到{}个文件：\n{}\n\n'.format(searchdir, filecountindir,filefindedlist))

def MainProgram():
    while True:
        if not os.path.exists('.\\查找目标源文件夹'):
            os.mkdir('.\\查找目标源文件夹')
        if os.path.exists('.\\查找结果文件夹'):
            shutil.rmtree('.\\查找结果文件夹')
        i=os.system('cls')
        print('*'*10+'欢迎使用本程序'+'*'*10)
        print('\n')
        print('【说明】：本程序可以通过文件名字的关键词用来查找1个或多个文件夹中你需要的文件！\n')
        print('''【使用方法】：
    1.将需要的查找的1个或多个文件夹复制到本程序所在位置的【查找目标源文件夹】（首次运行本程序时会自动创建该文件夹），
    2.选择查找要实现的功能
    3.输入查找的文件名称中的关键词
    4.在【查找结果文件夹】中获得相应的结果
    5.可以在【查找结果文件夹】中点击《查找结果日志.txt》文件来查看查询的情况
        \n''')
        print('【提示】：重复使用时，请注意清空【查找结果文件夹】！！')
        print('-'*27+'\n')
        print('''请选择相应的功能：
    1.仅查找文件，不重新命名（遇重名时自动编号）
    2.查找文件，并用文件所在的文件夹名字命名''')
        print('*'*27)
        chosed = input('请选择相应功能（直接回车键退出程序）：')
        if chosed == '1':
            while True:
                i = os.system('cls')
                print('*'*10+'目前正在使用【仅查找文件，不重新命名（遇重名时自动编号）】功能'+'*'*10)
                chosed=input('''\n【提示】：请将需要查找的文件夹或文件拷贝到【查找目标源文件夹】，拷贝完成后：
                1-继续查找
                --直接回车键返回主界面\n【注意：上述任一步都会删除之前的查找结果！！！】\n请选择下一步操作：''')
                if chosed == '1':
                    if os.path.exists('.\\查找结果文件夹'):
                        shutil.rmtree('.\\查找结果文件夹')
                    DirNums,FileNums = CountFileAndDir()
                    if DirNums == 0 and FileNums == 0:
                        i=os.system('cls')
                        print('没有在【查找目标源文件夹】中找到任何文件夹或文件，请确认已经将需要查找的'
                              '文件拷入到该文件夹')
                    else:
                        i=os.system('cls')
                        print('已经在【查找目标源文件夹】中找到{}个文件夹，{}个文件！'
                              '如果文件夹数量与拷入的不一致，说明文件夹中还有文件夹，是否影响'
                              '查找请自行判断！！！'.format(DirNums,FileNums))
                        chosed = input('\n是否开始查找？（0-返回功能界面，直接回车键开始查找！）')
                        if chosed == '0':
                            pass
                        else:
                            keyword = input('请输入文件名的关键词(多个关键词，请用逗号<不区分中英文>隔开):')
                            keywordlist = re.split('[,，]',keyword)
                            print('正在查找并拷贝文件，请稍后…')
                            global filecountforname
                            global file_nothing_list
                            filecountforname = 0  # 定义一个全局变量，来统计找到的文件数量，并用来区别重名文件的命名
                            file_nothing_list = [] # 定义一个全局变量，来统计未找到文件的文件夹
                            FindAndCopyMoveOne('.\\查找目标源文件夹', keywordlist)
                            with open(r'.\查找结果文件夹\查找结果日志.txt','a+') as file:
                                file.write('-'*30+'\n')
                                file.write('\n总共查找到{}个文件！'.format(filecountforname))
                            print('-'*30)
                            print('没有找到文件的文件夹有：\n')
                            for i in file_nothing_list:
                                print(i)
                            input('\n查找结束,查找情况可在查找结果文件夹中【查找结果日志.txt】文件中查阅，回车键继续…')
                else:
                    break

        elif chosed == '2':
            pass
        else:
            break


#  定义一个函数，来统计【查找目标源文件夹】中文件夹和文件的数量
def CountFileAndDir(path='.\\查找目标源文件夹'):
    DirNums = 0
    FileNums = 0
    for root,dirs,files in os.walk(path):
        for each in dirs:
            DirNums += 1
        for each in files:
            FileNums += 1
    return DirNums,FileNums


MainProgram()

# x,y= CountFileAndDir()
# print(x,y)
