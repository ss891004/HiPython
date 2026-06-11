import openpyxl
myBook=openpyxl.load_workbook('高校汇总表.xlsx')
mySheet=myBook.active
#从高校汇总表(mySheet)的第2行开始逐行循环(到最后一行)
for myRow in list(mySheet.rows)[1:]:
    #获取每行(myRow)的高校列的单元格数据(myOldValue)
    myOldValue=str(myRow[1].value)
    #在单元格数据(myOldValue)中使用回车符'\r\n'替换字符'、'
    myRow[1].value=myOldValue.replace('、','\r\n')
myBook.save('结果表-高校汇总表.xlsx')
