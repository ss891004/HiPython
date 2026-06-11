import openpyxl
myBook=openpyxl.load_workbook('竞猜表.xlsx',data_only=True)
mySheet=myBook.active
#获取竞猜表(myBook.active)的行(第1行除外)
myRows=list(myBook.active.rows)[1:]
for myRow in myRows:
    #获取该行的发送的选手编号列的单元格数据(myRow[1].value)
    myStr=myRow[1].value
    #如果发送的选手编号在{'20号','25号','27号','33号','38号'}集合中
    if set(myStr.split('、'))=={'20号','25号','27号','33号','38号'}:
       #则在全部猜对列中标注'√'
       myRow[2].value='√'
    else:
       #否则在全部猜对列中标注'×'
       myRow[2].value='×'
myBook.save('结果表-竞猜表.xlsx')
