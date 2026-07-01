import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
#累加工作簿(myBook)的所有工作表的B5单元格数据
mySum=sum([mySheet['B5'].value for mySheet in myBook])
#在工作簿(myBook)中新增一个全年利润表(mySheet2)
mySheet2=myBook.copy_worksheet(myBook.worksheets[0])
mySheet2.title='全年利润表'
#在全年利润表(mySheet2)的对应单元格设置累加数(合计)
mySheet2['B5'].value=mySum
mySheet2['B6'].value=mySum
myBook.save('结果表-利润表.xlsx')
