import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#在收入表(mySheet)的第4列之前插入2个空白列
mySheet.insert_cols(4,2)
myBook.save('结果表-收入表.xlsx')
