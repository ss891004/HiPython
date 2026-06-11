import openpyxl
myBook=openpyxl.load_workbook('新书表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取新书表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myDict={}
for myRow in myRows:
    #根据每行(myRow)的书名(myRow[0])和售价(myRow[1])创建字典
    myDict[myRow[0]]=myRow[1]
#获取在字典(myDict)中售价(myDict.values())最高的图书
myMax=max(zip(myDict.values(),myDict.keys()))
mySheet.append(['【最高售价图书】'+myMax[1],myMax[0]])
myBook.save('结果表-新书表.xlsx')
