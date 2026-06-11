import openpyxl
myBook=openpyxl.load_workbook('成绩表.xlsx')
mySheet=myBook.active
#由于每执行一次mySheet.delete_rows(myRow)，
#mySheet.max_row会发生变化，因此采用倒循环，
#mySheet.max_row表示起始行号，1表示结束行号，-1表示步长(即倒循环)
for myRow in range(mySheet.max_row,1,-1):
    #print(mySheet.max_row)
    #对每行的B、C、D、E、F列求和
    myRowSum=sum([myCell.value for myCell in mySheet[myRow][1:6]])
    #如果合计小于400，则删除行
    if myRowSum<400:
       mySheet.delete_rows(myRow)
myBook.save('结果表-成绩表.xlsx')
