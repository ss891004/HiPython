import openpyxl
myBook=openpyxl.load_workbook('运动员表.xlsx',data_only=True)
mySheet1=myBook['篮球赛']
mySheet2=myBook['足球赛']
mySheet3=myBook['乒乓球赛']
#根据篮球赛工作表的行(第1行除外)创建集合(mySet1)
mySet1=set(list(mySheet1.values)[1:])
#根据足球赛工作表的行(第1行除外)创建集合(mySet2)
mySet2=set(list(mySheet2.values)[1:])
#根据乒乓球赛工作表的行(第1行除外)创建集合(mySet3)
mySet3=set(list(mySheet3.values)[1:])
#获取三个集合(mySet1、mySet2、mySet3)的交集(mySet4)，即筛选参加三种比赛的运动员
mySet4=mySet1.intersection(mySet2,mySet3)
#根据交集(mySet4)创建参加三种比赛的工作表(mySheet4=)
mySheet4=myBook.copy_worksheet(mySheet1)
mySheet4.title='三种比赛'
while mySheet4.max_row>1:
      mySheet4.delete_rows(2)
for myRow in mySet4:
    mySheet4.append(myRow)
myBook.save('结果表-运动员表.xlsx')
