import openpyxl
myBook=openpyxl.load_workbook('城市排名表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取城市排名表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myList=[]
for myRow in myRows:
    myList+=str(myRow[1]).split('、')
myDict={}
for myName in myList:
    #如果在字典(myDict)的键名中已经存在某城市(myName)，则对应的键值增加1
    if myName in myDict.keys():
       myDict[myName]+=1
    #否则在字典(myDict)中直接设置myDict[myName]=1
    else:
       myDict[myName]=1
#创建列表(myNewList)
myNewList=[]
for myName,myIndex in zip(myDict.keys(),myDict.values()):
    #将字典(myDict)的键名设置为子列表的myName，键值设置为子列表的myIndex
    myNewList+=[[myName,myIndex]]
#print(myNewList)
#根据myNewList的子列表(成员)的myIndex进行降序排列myNewList
mySortList=sorted(myNewList,key=lambda x:x[1],reverse=True)
#print(mySortList)
myCellValue=''
#将列表(myNewList)的成员拼接为字符串
for myName in mySortList:
    myCellValue+=str(myName[0])+'('+str(myName[1])+'次)'+'、'
#在城市排名表(mySheet)的最后一行添加结果[出现次数最多的城市]
mySheet.append(['出现次数最多的城市',myCellValue])
myBook.save('结果表-城市排名表.xlsx')
