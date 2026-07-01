import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#设置收入表(mySheet)的C列的宽度为10
mySheet.column_dimensions['C'].width=10
myBook.save('结果表-收入表.xlsx')
