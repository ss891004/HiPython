import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
mySheet=myBook.active
mySheet.title='2020年'+mySheet.title
myBook.save('结果表-利润表.xlsx')
