import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
#获取收入表(myBook.active)的所有列(myColumns)
myColumns=myBook.active.columns
myColIndex=2
#循环收入表(myColumns)的B、C、D列(myCol)
for myCol in list(myColumns)[1:4]:
    myColSum=0
    #循环列(myCol)的5、6、7、8行的4个单元格
    for myCell in myCol[4:8]:
        #对4个单元格数据求和
        myColSum+=myCell.value
    #将求和数据(myColSum)写入合计单元格
    myBook.active.cell(9,myColIndex).value=myColSum;
    myColIndex+=1
myBook.save('结果表-收入表.xlsx')
