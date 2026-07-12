import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
myList=[['2季度',373445,138815,445],['3季度',496008,168123,1246],
        ['4季度',120234,499028,118896]]
#循环列表(myList)的行(myRow)数据
for myRow in myList:
    #根据行(myRow)数据在收入表(mySheet)的末尾添加新行
    mySheet.append(myRow)
myBook.save('结果表-收入表.xlsx')
