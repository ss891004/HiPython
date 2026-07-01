import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.worksheets[0]
myRowIndex=0
#按行循环收入表(mySheet)的['B5':'D8']范围的行(myRow)
for myRow in mySheet['B5':'D8']:
    myRowSum=0
    myRowIndex+=1
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #累加各个单元格(myCell)的数据
        myRowSum+=myCell.value
    #在行(myRow)的最后一个单元格中写入合计
    mySheet.cell(myRowIndex+4,5).value=myRowSum
myBook.save('结果表-收入表.xlsx')
