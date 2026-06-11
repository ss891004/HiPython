import openpyxl
myBook=openpyxl.load_workbook('成绩表.xlsx')
mySheet=myBook.active
#根据成绩表(mySheet)的单元格数据(第1行除外)创建集合(mySet)
mySet=set(list(mySheet.values)[1:])
#从集合(mySet)中随机删除一个成员(此例为行)
mySet.pop()
#删除成绩表(mySheet)的行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
#根据随机删除成员(行)之后的集合(mySet)重新添加成绩表(mySheet)的数据
for myRow in mySet:
    mySheet.append(myRow)
myBook.save('结果表-成绩表.xlsx')
