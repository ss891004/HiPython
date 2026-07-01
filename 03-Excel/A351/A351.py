import openpyxl
myBook=openpyxl.load_workbook('世界五百强表.xlsx',data_only=True)
mySheet=myBook.active
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='世界五百强表'
myNewSheet.append(['公司名称','夺冠次数'])
#按行获取世界五百强表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myList=[]
for myRow in myRows:
    myList.append(myRow[1])
#根据列表(myList)创建集合(mySet)，即通过集合(mySet)删除列表(myList)重复的公司名称
mySet=set(myList)
for myName in mySet:
    #统计myName(每个公司)在列表(myList)中的出现次数
    myNewSheet.append([myName,myList.count(myName)])
myNewBook.save('结果表-世界五百强表.xlsx')
