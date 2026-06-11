import openpyxl
myBook=openpyxl.load_workbook('订单表.xlsx',data_only=True)
mySheet1=myBook['已出库订单表']
mySheet2=myBook['未出库订单表']
#将已出库订单表复制成全部订单表
mySheet3=myBook.copy_worksheet(mySheet1)
mySheet3.title='全部订单表'
#删除全部订单表的行(第1行除外)
while mySheet3.max_row>1:
      mySheet3.delete_rows(2)
myList3=list(mySheet1.values)[1:]
myList2=list(mySheet2.values)[1:]
#拼接已出库订单表(即列表myList3)和未出库订单表(即列表myList2)的所有行
#myList3.extend(myList2)
myList3=myList3+myList2
#根据订单编号升序排列全部订单表(即拼接之后的列表myList3)的行
myList3=sorted(myList3,key=lambda x:x[1])
#将全部订单表(即拼接之后的列表myList3)的行添加到mySheet3
for myRow in myList3:
    mySheet3.append(myRow)
myBook.save('结果表-订单表.xlsx')
