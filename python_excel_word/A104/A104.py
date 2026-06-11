import openpyxl
myBook=openpyxl.load_workbook('排名表.xlsx')
mySheet=myBook.active
#创建在内容超长时自动换行的自定义样式(myAlignment)
myAlignment=openpyxl.styles.Alignment(wrap_text=True)
#循环排名表(mySheet)的['A4:D6']范围的行(myRow)
for myRow in mySheet['A4:D6']:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #使用自定义样式(myAlignment)设置单元格(myCell)的alignment属性
        myCell.alignment=myAlignment
myBook.save('结果表-排名表.xlsx')
