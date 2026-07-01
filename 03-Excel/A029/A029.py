import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
#获取收入表(myBook.active)的行(myRows)
myRows=myBook.active.rows
#循环myRows的5、6、7、8行(myRow)
for myRow in list(myRows)[4:8]:
    #循环行(myRow)的B、C、D列的单元格(myCell)
    for myCell in myRow[1:4]:
        #如果单元格(myCell)不为空
        if myCell.value is not None:
           #则将单元格(myCell)的数据乘以10000
           myCell.value*=10000
myBook.save('结果表-收入表.xlsx')
