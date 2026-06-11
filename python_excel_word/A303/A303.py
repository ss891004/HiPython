import openpyxl
myBook=openpyxl.load_workbook('工资表.xlsx',data_only=True)
mySheet=myBook['工资表']
#采用倒循环方式循环每行，mySheet.max_row表示最后一行，2表示终止行是第2行
for myRow in range(mySheet.max_row,2,-1):
    #添加空白行，以便于为每位员工的工资条添加表头
    mySheet.insert_rows(myRow)
    for myCol in range(1,8):
        #在空白行中写入表头，myRow和myCol分别表示行号和列号
        mySheet.cell(myRow,myCol,mySheet.cell(1,myCol).value)
    #添加空白行，以便于裁剪工资条
    mySheet.insert_rows(myRow)
myBook.save('结果表-工资表.xlsx')
