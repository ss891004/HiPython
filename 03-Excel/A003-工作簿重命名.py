import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
# 修改活动工作簿的名称
mySheet=myBook.active
mySheet.title='2020年'+mySheet.title
myBook.save('结果表-利润表.xlsx')

import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
#循环工作簿(myBook.worksheets)的工作表(mySheet)
for mySheet in myBook.worksheets:
    #根据工作表(mySheet)的表名设置新的表名
    mySheet.title='2020年' + mySheet.title
myBook.save('结果表-利润表.xlsx')

