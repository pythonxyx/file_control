import os
import shutil


#测试遍历文件夹
def FindAll(xpath='.\\程序文件夹'):
    for x in os.listdir(xpath):
        next_file = os.path.join(xpath,x)
        if os.path.isfile(next_file):
            n=os.path.relpath(next_file)
            tmplist = n.split('\\')
            print(tmplist)
            newname = tmplist[2]

        else:
            FindAll(next_file)

FindAll()