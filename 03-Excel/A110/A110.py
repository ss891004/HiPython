import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#自定义红色字体(myFont)
myFont=openpyxl.styles.Font(color='FF0000')
#循环收入表(mySheet)的['B5:D8']范围的单元格(myCell)
for myRow in mySheet['B5:D8']:
    for myCell in myRow:
        #使用自定义红色字体(myFont)设置单元格(myCell)的font属性
        myCell.font=myFont
myBook.save('结果表-收入表.xlsx')
