import openpyxl
myBook=openpyxl.load_workbook('学员表.xlsx',data_only=True)
mySheet1=myBook['Android学员表']
mySheet2=myBook['Java学员表']
#将Android学员表复制成仅学一门课程的学员表(mySheet3)
mySheet3=myBook.copy_worksheet(mySheet1)
mySheet3.title='仅学一门课程的学员表'
#删除仅学一门课程的学员表(mySheet3)的行(第1行除外)
while mySheet3.max_row>1:
      mySheet3.delete_rows(2)
#根据Android学员表(mySheet1)的行(第1行除外)创建集合(mySet1)
mySet1=set(list(mySheet1.values)[1:])
#根据Java学员表(mySheet2)的行(第1行除外)创建集合(mySet2)
mySet2=set(list(mySheet2.values)[1:])
#计算mySet1和mySet2两个集合的对称差集(mySet3)，即获得两个工作表(集合)不同的行
mySet3=mySet1.symmetric_difference(mySet2)
#循环集合(mySet3)的行(myRow)数据
for myRow in mySet3:
    #将行(myRow)数据添加到仅学一门课程的学员表(mySheet3)中
    mySheet3.append(myRow)
myBook.save('结果表-学员表.xlsx')
