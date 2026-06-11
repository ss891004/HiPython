import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#根据员工表(mySheet)的单元格数据(第1行除外)创建集合(mySet)
mySet=set(list(mySheet.values)[1:])
#删除员工表(mySheet)的行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
#在员工表(mySheet)中随机筛选6行数据
for myRow in range(6):
    mySheet.append(mySet.pop())
myBook.save('结果表-员工表.xlsx')
