import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#获取收入表(mySheet)第5行到第8行之间的行(myRows)
myRows=mySheet['5':'8']
myRowIndex=5
for myRow in myRows:
    #对行(myRow)的B列、C列、D列的单元格数据求和(myRowSum)
    myRowSum=sum(myCell.value for myCell in myRow[1:4])
    #在行(myRow)的第5列单元格写入求和数据(myRowSum)
    mySheet.cell(myRowIndex,5).value=myRowSum
    myRowIndex+=1
myBook.save('结果表-收入表.xlsx')
