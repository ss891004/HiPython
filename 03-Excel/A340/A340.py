import openpyxl
myBook=openpyxl.load_workbook('管理费用表.xlsx',data_only=True)
mySheet=myBook.active
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='管理费用表'
myNewSheet.append(['月份','费用类别','金额合计'])
#按行获取管理费用表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myDict={}
for myRow in myRows:
    #如果在字典(myDict)中存在某费用类别，则直接在某费用类别中添加[myRow]
    if myRow[2] in myDict.keys():
       myDict[myRow[2]]+=[myRow]
    #否则创建新费用类别
    else:
       myDict[myRow[2]]=[myRow]
#在字典(myDict)中循环每个成员(费用类别)
for myType in myDict.keys():
    #对某费用类别的所有金额求和，并添加到金额合计表中
    mySum=sum([myRow[3] for myRow in myDict[myType]])
    myNewSheet.append(['12月份',myType,mySum])
myNewBook.save('结果表-管理费用表.xlsx')
