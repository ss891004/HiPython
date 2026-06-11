import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#隐藏员工表(mySheet)的第7至12行
mySheet.row_dimensions.group(7,12,hidden=True)
myBook.save('结果表-员工表.xlsx')
