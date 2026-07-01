import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#自定义渐变色填充样式(myGradientFill)
myGradientFill=openpyxl.styles.GradientFill(stop=('FF0000','00FF00'))
#循环收入表(mySheet)的['A5:D8']范围的行(myRow)
for myRow in mySheet['A5:D8']:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #使用渐变色填充样式(myGradientFill)设置单元格(myCell)的fill属性
        myCell.fill=myGradientFill
myBook.save('结果表-收入表.xlsx')
