import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#指定在收入表(mySheet)中按列操作单元格的数据范围(myRange)
myRange=mySheet.iter_cols(min_row=5,min_col=2,max_row=8,max_col=4)
myNewRow=['合计']
#循环收入表(myRange)的B、C、D列(myCol)
for myCol in myRange:
    #按列(myCol)对单元格数据求和
    myColSum=sum([myCell.value for myCell in myCol])
    myNewRow.append(myColSum)
#直接在收入表(mySheet)的末尾添加一行(分类收入)合计
mySheet.append(myNewRow)
myBook.save('结果表-收入表.xlsx')
