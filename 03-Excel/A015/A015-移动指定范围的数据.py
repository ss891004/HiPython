import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#把收入表(mySheet)的B4:B8范围的数据向下移动0行，向右移动3列
mySheet.move_range('B4:B8',rows=0,cols=3)
myBook.save('结果表-收入表.xlsx')
