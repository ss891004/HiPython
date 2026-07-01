import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#获取收入表(mySheet)的B、C、D列
myRange=mySheet['B':'D']
myColIndex=2
#循环收入表(myRange)的B、C、D列(myCol)
for myCol in myRange:
    #计算列(myCol)的第5、6、7、8行的单元格数据合计
    myColSum=sum(myCell.value for myCell in myCol[4:8])
    #在列(myCol)的第9行的单元格中写入合计数据(myColSum)
    mySheet.cell(9, myColIndex).value=myColSum
    myColIndex+=1
mySheet['A9']='合计'
myBook.save('结果表-收入表.xlsx')
