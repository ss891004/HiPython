import openpyxl
myBook=openpyxl.load_workbook('城市排名表.xlsx')
mySheet=myBook.active
#获取城市排名表(mySheet)的行(第1行除外)
myRows=list(mySheet.rows)[1:]
#循环城市排名表(myRows)的行(myRow)
for myRow in myRows:
    myList=[]
    #根据'、'符号将每行的城市列(myRow[1])的城市名字拆分为列表(myNames)
    myNames=myRow[1].value.split('、')
    #循环列表(myNames)的城市名字(myName)
    for myName in myNames:
        #如果在列表(myList)中没有城市名字(myName)
        if myName not in myList:
           #则在列表(myList)中添加城市名字(myName)
           myList.append(myName)
    #使用'、'符号将列表(myList)的成员(城市名字)连接成字符串，
    #并设置为城市列的单元格数据(即无重复的城市名字)

    myRow[1].value='、'.join(myList)
myBook.save('结果表-城市排名表.xlsx')
