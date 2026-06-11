import openpyxl
#根据“录取表.xlsx”文件创建工作簿(myBook)
myBook=openpyxl.load_workbook('录取表.xlsx')
mySheet=myBook['录取表']
#按行获取录取表(mySheet)的单元格数据(myRange)
myRange=list(mySheet.values)
#创建空白字典(myDict)
myDict={}
#从myRange的第4行开始循环(到最后一行)
for myRow in myRange[3:]:
    #如果在字典(myDict)中存在某录取院校(myRow[0])，
    #则直接在某录取院校(myRow[0])中添加[myRow]
    if myRow[0] in myDict.keys():
       myDict[myRow[0]]+=[myRow]
    #否则创建新录取院校
    else:
       myDict[myRow[0]]=[myRow]
#循环字典(myDict)的成员
for myKey,myValue in myDict.items():
    #根据myKey(录取院校)创建新工作表(myNewSheet)
    myNewSheet=myBook.create_sheet(myKey+'录取表')
    #在新工作表(myNewSheet)中添加表头(录取院校、专业、考生姓名、总分)
    myNewSheet.append(myRange[2])
    #在新工作表(myNewSheet)中添加录取院校(myKey)的多个考生(myValue)
    for myRow in myValue:
        myNewSheet.append(myRow)
#保存工作簿，即将拆分结果保存在'结果表-录取表.xlsx'文件中
myBook.save('结果表-录取表.xlsx')
