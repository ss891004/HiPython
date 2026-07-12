import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
#循环工作簿(myBook)的工作表(mySheet)
for mySheet in myBook.worksheets:
    #如果工作表(mySheet)的表名包含'华东'，则删除工作表(mySheet)
    if mySheet.title.split('-')[0]=='华东':
       myBook.remove(mySheet)
myBook.save('结果表-利润表.xlsx')
