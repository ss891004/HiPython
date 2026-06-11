import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#指定按列操作单元格的数据范围(B5:D8)
myRange=mySheet.iter_cols(min_row=5,min_col=2)
myMax=['最大值']
#使用列表推导式获取每列的最大值
myMax+=[max([myCell.value for myCell in myCol]) for myCol in myRange]
#直接在收入表的末尾添加最大值(行)
mySheet.append(myMax)
myBook.save('结果表-收入表.xlsx')
