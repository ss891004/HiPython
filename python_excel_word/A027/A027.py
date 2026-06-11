import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.worksheets[0]
#设置收入表(mySheet)的数据范围(myRange)
myRange=mySheet['A1':'D8']
#使用列表推导式对myRange的行数据求和
myValues=[sum([myCell.value for myCell in myRow[1:]]) for myRow in myRange[4:]]
myRowIndex=5
for myValue in myValues:
    #在合计列的单元格中写入求和数据(即每个季度的收入合计)
    mySheet.cell(myRowIndex,5).value=myValue
    myRowIndex+=1
myBook.save('结果表-收入表.xlsx')
