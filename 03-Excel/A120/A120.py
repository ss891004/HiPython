import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#自定义收入表(mySheet)的第6行的高度
mySheet.row_dimensions[6].height=30
myBook.save('结果表-收入表.xlsx')
