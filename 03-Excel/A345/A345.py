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
#根据全部订单表的行(第1行除外)创建集合(mySet1)
mySet1=set(myList1)
#根据已出库订单表的行(第1行除外)创建集合(mySet2)
mySet2=set(myList2)
#计算mySet1和mySet2两个集合的差集，即获得未出库订单表的行
mySet3=mySet1.difference(mySet2)
#循环集合(mySet3)的行(myRow)数据
for myRow in mySet3:
    #将行(myRow)数据添加到未出库订单表(mySheet3)中
    mySheet3.append(myRow)
myBook.save('结果表-订单表.xlsx')
