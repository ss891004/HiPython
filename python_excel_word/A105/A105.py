import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#设置自定义边框线(mySide)为红色的粗线
mySide=openpyxl.styles.Side(style='thick',color='FF0000')
#在自定义边框(myBorder)的上、下、左、右四条边上应用自定义边框线
myBorder=openpyxl.styles.Border(left=mySide,right=mySide,
                                 top=mySide,bottom=mySide)
#循环收入表(mySheet)的['A5:D8']范围的行(myRow)
for myRow in mySheet['A5:D8']:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #使用自定义边框(myBorder)设置单元格(myCell)的border属性
        myCell.border=myBorder
myBook.save('结果表-收入表.xlsx')
