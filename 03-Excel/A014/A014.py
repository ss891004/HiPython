import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#从收入表(mySheet)的第2列开始，连续删除3列数据
mySheet.delete_cols(2,3)
myBook.save('结果表-收入表.xlsx')
