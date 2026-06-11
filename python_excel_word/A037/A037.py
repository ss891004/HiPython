import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#对第5行的B、C、D列(即2、3、4列)的单元格数据求和，并在合计列的单元格中写入合计
mySheet['E5']=sum([myCell.value for myCell in mySheet[5][1:4]])
mySheet['E6']=sum([myCell.value for myCell in mySheet[6][1:4]])
mySheet['E7']=sum([myCell.value for myCell in mySheet[7][1:4]])
mySheet['E8']=sum([myCell.value for myCell in mySheet[8][1:4]])
myBook.save('结果表-收入表.xlsx')
