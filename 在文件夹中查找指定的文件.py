import os
import shutil
import re

#关键字查找文件，不重新命名
def FindAndCopyMoveOne(path,str1):
    global filecount
    for x in os.listdir(path):
        next_file = os.path.join(path,x)
        if os.path.isfile(next_file):
            for keyword in str1:
                if keyword in x:
                    filecount += 1
                    filenamelist = x.split('.')
                    newfilename = filenamelist[0]+str(filecount)+'.'+filenamelist[1]
                    os.renames(next_file,os.path.join('.\\查找结果文件夹',newfilename))
        else:
            FindAndCopyMoveOne(next_file,str1)

def MainProgram():
    while not os.path.exists('.\\查找目标源文件夹'):
        os.mkdir('.\\查找目标源文件夹')
        sourcedir = '.\\查找目标源文件夹'
    while not os.path.exists('.\\查找结果文件夹'):
        os.mkdir('.\\查找结果文件夹')
        resultdir = '.\\查找结果文件夹'
    while True:
        i=os.system('cls')
        print('*'*10+'欢迎使用本程序'+'*'*10)
        print('\n')
        print('【说明】：本程序可以通过文件名字的关键词用来查找1个或多个文件夹中你需要的文件！\n')
        print('''【使用方法】：
    1.将需要的查找的1个或多个文件夹复制到本程序所在位置的【查找目标源文件夹】（首次运行本程序时会自动创建该文件夹），
    2.选择查找要实现的功能
    3.输入查找的文件名称中的关键词
    4.在【查找结果文件夹】中获得相应的结果
    5.可以在【查找结果文件夹】中点击《查找结果.txt》文件来查看查询的情况
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
                input('\n请将需要查找的文件夹或文件拷贝到【查找目标源文件夹】，拷贝完成后回车键继续…')
                DirNums,FileNums = CountFileAndDir()
                if DirNums == 0 and FileNums == 0:
                    print('没有在【查找目标源文件夹】中找到任何文件夹或文件，请确认已经将需要查找的'
                          '文件拷入到该文件夹')
                else:
                    print('已经在【查找目标源文件夹】中找到{}个文件夹，{}个文件！'.format(DirNums,FileNums))
                chosed = input('\n是否开始查找？（0-返回主界面，直接回车键开始查找！）')
                if chosed == '0':
                    break
                else:
                    keyword = input('请输入文件名的关键词(多个关键词，请用逗号<不区分中英文>隔开):')
                    keywordlist = re.split('[,，]',keyword)
                    print('正在查找并拷贝文件，请稍后…')
                    FindAndCopyMoveOne('.\\查找目标源文件夹', keywordlist)
                    print('查找结束')




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

filecount = 0  # 定义一个全局变量，来统计找到的文件数量，并用来区别重名文件的命名
MainProgram()

# x,y= CountFileAndDir()
# print(x,y)
