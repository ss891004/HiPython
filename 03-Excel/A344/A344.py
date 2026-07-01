import openpyxl
myBook=openpyxl.load_workbook('城市排名表.xlsx')
mySheet=myBook.active
#获取城市排名表(mySheet)的行(第1行除外)
myRows=list(mySheet.rows)[1:]
for myRow in myRows:
    #根据'、'符号将城市列(myRow[1])的城市名字拆分为列表(myList)
    myList=myRow[1].value.split('、')
    #根据列表(myList)列表创建集合(mySet)，此时自动删除重复的城市名字
    mySet=set(myList)
    #使用'、'符号将集合(mySet)的所有成员连接成字符串，
    #并设置为城市列的单元格数据(即无重复的城市名字)
    myRow[1].value='、'.join(mySet)
myBook.save('结果表-城市排名表.xlsx')
