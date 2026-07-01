import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#从收入表(mySheet)的第6行开始，连续删除2行数据
mySheet.delete_rows(6,2)
myBook.save('结果表-收入表.xlsx')
