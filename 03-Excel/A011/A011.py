import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#在收入表(mySheet)的第6行之前插入2个空白行
mySheet.insert_rows(6,2)
myBook.save('结果表-收入表.xlsx')
