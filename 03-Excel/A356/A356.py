import openpyxl
myBook=openpyxl.load_workbook('各省简称表.xlsx',data_only=True)
mySheet=myBook.active
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='各省简称表'
myNewSheet.append(['简称','省份'])
#按行获取各省简称表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myDict={}
for myRow in myRows:
    #如果在字典(myDict)中存在某省份，则直接在某省份中添加myRow[1]
    if myRow[0] in myDict.keys():
       myDict[myRow[0]]+=myRow[1]
    #否则创建新省份
    else:
         myDict[myRow[0]]=myRow[1]
#交换键名和键值(即交换省份和简称)
myDictSwap={myValue:myKey for myKey, myValue in myDict.items()}
#循环交换键名和键值之后的字典(myDictSwap)
for myKey,myValue in myDictSwap.items():
    myNewSheet.append([myKey,myValue])
myNewBook.save('结果表-各省简称表.xlsx')
