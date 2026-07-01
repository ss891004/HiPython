import openpyxl
myBook=openpyxl.load_workbook('录取表.xlsx',data_only=True)
mySheet1=myBook['北京大学录取表']
mySheet2=myBook['清华大学录取表']
mySheet3=myBook['浙江大学录取表']
mySheet4=myBook['武汉大学录取表']
#将北京大学录取表(mySheet1)复制成(全部院校)录取表(mySheet5)
mySheet5=myBook.copy_worksheet(mySheet1)
mySheet5.title='录取表'
#删除录取表(mySheet5)的行(第1行除外)
while mySheet5.max_row>1:
      mySheet5.delete_rows(2)
#根据北京大学录取表(mySheet1)的行创建集合(mySet1)
mySet1=set(list(mySheet1.values)[1:])
#根据清华大学录取表(mySheet2)的行创建集合(mySet2)
mySet2=set(list(mySheet2.values)[1:])
#根据浙江大学录取表(mySheet3)的行创建集合(mySet3)
mySet3=set(list(mySheet3.values)[1:])
#根据武汉大学录取表(mySheet4)的行创建集合(mySet4)
mySet4=set(list(mySheet4.values)[1:])
#将mySet1、mySet2、mySet3、mySet4集合拼接(合并)成集合(mySet5)
mySet5=mySet1.union(mySet2,mySet3,mySet4)
#根据集合(mySet5)在(全部院校)录取表(mySheet5)中添加考生数据
for myRow in mySet5:
    mySheet5.append(myRow)
myBook.save('结果表-录取表.xlsx')
