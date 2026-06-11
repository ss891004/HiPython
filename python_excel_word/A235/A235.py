import openpyxl
myBook=openpyxl.load_workbook('成绩表.xlsx')
mySheet=myBook.active
myRange=mySheet.iter_rows(min_row=5,min_col=1)
for myRow in myRange:
    #对每个学生(myRow)的B、C、D、E、F列数据求和
    myRowSum=sum([myCell.value for myCell in myRow][1:6])
    #myRow[-1]表示该行的最后一个单元格，myRow[-2]表示该行倒数第二个单元格
    if myRowSum>400:
         myRow[-1].value='一等奖学金'
    elif myRowSum>350:
         myRow[-1].value='二等奖学金'
    else:
         myRow[-1].value='三等奖学金'
myBook.save('结果表-成绩表.xlsx')
