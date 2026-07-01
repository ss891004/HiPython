import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
myCol=openpyxl.utils.column_index_from_string('B')
#print(myCol)
#删除收入表(mySheet)的第2列
mySheet.delete_cols(myCol,1)
myBook.save('结果表-收入表.xlsx')
