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
#根据已出库订单表的行创建集合(mySet1)
mySet1=set(list(mySheet1.values)[1:])
#根据未出库订单表的行创建集合(mySet2)
mySet2=set(list(mySheet2.values)[1:])
#将mySet1和mySet2拼接成mySet3，即生成全部订单表
mySet3=mySet1.union(mySet2)
for myRow in mySet3:
    mySheet3.append(myRow)
myBook.save('结果表-订单表.xlsx')
