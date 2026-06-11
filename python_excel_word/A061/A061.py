import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
mySheet['B9']='=Average(B5:B8)'
mySheet['C9']='=Average(C5:C8)'
mySheet['D9']='=Average(D5:D8)'
myBook.save('结果表-收入表.xlsx')
