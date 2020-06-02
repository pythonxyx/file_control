import os
import shutil

#测试遍历文件夹
def FindAndCopyMove(xplace='.\\程序文件夹'):
    for x in os.listdir(xplace):
        next_file = os.path.join(xplace,x)
        if os.path.isfile(next_file):
            if 'test' in x:
                if not os.path.exists('.\\目标目录'):
                    os.mkdir('.\\目标目录')
                newfile = os.path.join('.\\目标目录',x)
                filenamelist = x.split('.')
                tmplist = os.path.relpath(next_file).split('\\')
                newfilename = tmplist[2]+'.'+filenamelist[1]
                newname = os.path.join('.\\目标目录',newfilename)
                shutil.copy(next_file,newfile)
                try:
                    os.rename(newfile,newname)
                except:
                    print('【{}】文件夹中找到多个符合的文件，已经存在，不再重复复制'.format(tmplist[2]))
                print(x,'已经被复制且改名！')
        else:
            FindAndCopyMove(next_file)

FindAndCopyMove()

