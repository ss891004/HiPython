import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx',data_only=True)
mySheet=myBook.active
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='收入表'
myNewSheet.append(['月份','公司名称','合计金额'])
#按行获取收入表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myDict={}
for myRow in myRows:
    #如果在字典(myDict)中存在某公司，则直接在某公司中累加金额
    if myRow[1] in myDict.keys():
       myDict[myRow[1]]+=myRow[2]
    #否则创建新公司
    else:
       myDict[myRow[1]]=myRow[2]
#循环字典(myDict)的成员(公司)
for myName,myAmount in myDict.items():
    myNewSheet.append(['12月份',myName,myAmount])
myNewBook.save('结果表-收入表.xlsx')
