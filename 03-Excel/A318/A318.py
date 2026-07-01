import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#由于每执行一次mySheet.delete_rows(myRow)，
#mySheet.max_row会发生变化，因此采用倒循环，
#mySheet.max_row表示起始行号，1表示结束行号，-1表示步长(即倒数)
for myRow in range(mySheet.max_row,1,-1):
    #如果在(家庭地址)单元格中未包含‘江北县’，
    if '江北县' not in mySheet[myRow][2].value:
       #则删除该员工(行)，剩下的员工(行)则是筛选结果
       mySheet.delete_rows(myRow)
myBook.save('结果表-员工表.xlsx')
