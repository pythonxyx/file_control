import os
import shutil


# #测试遍历文件夹
# def FindAll(xpath='.\\程序文件夹'):
#     for x in os.listdir(xpath):
#         next_file = os.path.join(xpath,x)
#         if os.path.isfile(next_file):
#             n=os.path.relpath(next_file)
#             tmplist = n.split('\\')
#             print(tmplist)
#             newname = tmplist[2]
#
#         else:
#             FindAll(next_file)
#
# FindAll()
# count =0
# countfiles = 0
# x = os.walk('.\\查找目标源文件夹')
# for root,dirs,files in x:
#     for each in dirs:
#         count += 1
#     for each in files:
#         countfiles +=1
# print('文件夹的数量为：{}'.format(count))
# print('文件的数量为：{}'.format(countfiles))
#

# print(x)
# print(y)
# print(z)

#测试显示查找到的文件数量,测试成功
# count = 0
# count1 = 0
# def FindAll(path):
#     global count
#     global count1
#     for x in os.listdir(path):
#         next_file = os.path.join(path,x)
#         if os.path.isfile(next_file):
#             count += 1
#         else:
#             count1 += 1
#             FindAll(next_file)
#     return count,count1
#
# x,y= FindAll('.\\查找目标源文件夹')
# print(x,y)
