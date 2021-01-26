# -*- coding:utf-8 -*- 
__author__ = 'czk'
__date__ = '2021/1/26 8:47 上午'

# from CZKTool import *
# 导入xls第三方库
import xlsxwriter
# 指定年月
nian=2021
yue=1
import calendar
monthRange = calendar.monthrange(nian,yue)
print(monthRange)
# 获取该月有多少天
days = monthRange[1]
sheet_names = []
# 生成该月的年月日名称数组a
for a in range(days):
    aname = str(nian)+"-"+str(yue)+"-"+str(a+1)
    sheet_names.append(aname)
# 创建xls
# Create an new Excel file and add a worksheet.
xls_full_name=str(nian)+"年"+str(yue)+"月"+".xlsx"
workbook = xlsxwriter.Workbook(xls_full_name)

# 对a进行遍历，每个元素作为sheet的名称，
for asheet_name in sheet_names:
    # 创建sheet
    worksheet = workbook.add_worksheet(name=asheet_name)
# 保存
workbook.close()