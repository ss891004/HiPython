import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#循环收入表(mySheet)的['B5:D8']范围的行(myRow)
for myRow in mySheet['B5:D8']:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #设置单元格(myCell)的数据格式为人民币格式
        myCell.number_format='￥#,##0.00'
myBook.save('结果表-收入表.xlsx')
