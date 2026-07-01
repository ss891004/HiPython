import openpyxl
myBook=openpyxl.load_workbook('考试时间表.xlsx')
mySheet=myBook.active
#循环考试时间表(mySheet)的['B5:C8']范围的行(myRow)
for myRow in mySheet['B5:C8']:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow:
        #设置单元格(myCell)的时间格式
        myCell.number_format='HH时MM分SS秒'
myBook.save('结果表-考试时间表.xlsx')
