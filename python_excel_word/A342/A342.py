import openpyxl
myBook=openpyxl.load_workbook('订单表.xlsx',data_only=True)
mySheet1=myBook['全部订单表']
mySheet2=myBook['已出库订单表']
#将全部订单表(mySheet1)复制成未出库订单表(mySheet3)
mySheet3=myBook.copy_worksheet(mySheet1)
mySheet3.title='未出库订单表'
#删除未出库订单表(mySheet3)的行(第1行除外)
while mySheet3.max_row>1:
      mySheet3.delete_rows(2)
myList1=list(mySheet1.values)[1:]
myList2=list(mySheet2.values)[1:]
#循环全部订单表(myList1列表)的行(myRow)
for myRow in myList1:
    #如果行(myRow)不在已出库订单表(myList2列表)中
    if myRow not in myList2:
       #则将行(myRow)添加到未出库订单表(mySheet3)中
       mySheet3.append(myRow)
myBook.save('结果表-订单表.xlsx')
