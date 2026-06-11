import openpyxl
myBook=openpyxl.load_workbook('股价表.xlsx',data_only=True)
mySheet=myBook.active
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='股价表'
myNewSheet.append(['股票名称','成交均价'])
#按行获取股价表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myDict={}
for myRow in myRows:
    #如果在字典中存在某股票(myRow[1])，则直接在某股票中添加[myRow]
    if myRow[1] in myDict.keys():
       myDict[myRow[1]]+=[myRow]
    #否则创建新股票
    else:
       myDict[myRow[1]]=[myRow]
#循环字典(myDict)的成员(股票)
for myStock in myDict.keys():
   #计算股票的日成交均价，并添加到新表中
   myPrice=sum([myRow[2] for myRow in myDict[myStock]])/len(myDict[myStock])
   myNewSheet.append([myStock,myPrice])
myNewBook.save('结果表-股价表.xlsx')
