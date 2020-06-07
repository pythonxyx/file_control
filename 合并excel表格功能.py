import os
import xlrd
import xlwt
import xlwings as xw


os.chdir(r'C:\Users\Administrator\Desktop\新建文件夹')

filename = '干部年报.xls'

wb = xw.Book(filename)
sheet = xw.Sheet('1总名册')

print(sheet)

last_row_index = xw.Range('A6').expand('table').last_cell.row

print(last_row_index)

rn = 'A6:S'+str(last_row_index-1)

work_deail = xw.Range(rn).value

print(work_deail)

wb.close()

filename2='测试汇总表格.xlsx'

wb2 = xw.Book(filename2)
ws = xw.Sheet('sheet1')
last_row_index1 = xw.Range('A6').expand('table').last_cell.row
last_row_index1 += 1
xw.Range('A'+str(last_row_index1)).expand('table').value = work_deail
wb.save()
wb.close()








