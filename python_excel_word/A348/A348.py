import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(第1行除外)
myValues=list(mySheet.values)[1:]
#根据myValues创建mySet集合，此时自动随机排列所有行
mySet=set(myValues)
#删除员工表(mySheet)的行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
#在员工表(mySheet)中添加经过随机排列的行(mySet)
for myRow in mySet:
    mySheet.append(myRow)
myBook.save('结果表-员工表.xlsx')
