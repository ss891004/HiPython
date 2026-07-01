import openpyxl
myBook=openpyxl.load_workbook('成员表.xlsx')
mySheet=myBook.active
#循环成员表(mySheet)的['B5:C8']范围的行(myRow)
for myRow in mySheet['B5:C8']:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #设置单元格(myCell)的日期格式
        myCell.number_format='YYYY年MM月DD日'
myBook.save('结果表-成员表.xlsx')
