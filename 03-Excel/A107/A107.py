import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#自定义删除线字体(myFont)
myFont=openpyxl.styles.Font(strike=True)
#循环收入表(mySheet)的['D5:D8']范围的单元格(myCell)
for myCell in mySheet['D'][4:8]:
    #使用删除线字体(myFont)设置单元格(myCell)的font属性
    myCell.font=myFont
myBook.save('结果表-收入表.xlsx')
