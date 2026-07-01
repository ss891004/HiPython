import openpyxl
#读取“录取表.xlsx”文件
myBook=openpyxl.load_workbook('录取表.xlsx')
mySheet=myBook['录取表']
#按行获取录取表(mySheet)的单元格数据(myRange)
myRange=list(mySheet.values)
#创建空白字典(myDict)
myDict={}
#从录取表(myRange)的第4行开始循环(到最后一行)
for myRow in myRange[3:]:
    #如果在字典(myDict)中存在某录取院校(myRow[0])，
    #则直接在某录取院校(myRow[0])中添加考生([myRow])
    if myRow[0] in myDict.keys():
       myDict[myRow[0]]+=[myRow]
    #否则创建新录取院校
    else:
       myDict[myRow[0]]=[myRow]
#循环字典(myDict)的成员
for myKey,myValue in myDict.items():
    #创建新工作簿(myNewBook)
    myNewBook=openpyxl.Workbook()
    myNewSheet=myNewBook.active
    #在新工作表(myNewSheet)中添加表头(录取院校、专业、考生姓名、总分)
    myNewSheet.append(myRange[2])
    #在新工作表(myNewSheet)中添加键名(录取院校)下的多个键值(考生)
    for myRow in myValue:
        myNewSheet.append(myRow)
    myNewSheet.title=myKey+'录取表'
    #保存拆分之后(各个录取院校)的工作簿(myNewBook)，或者说保存各个Excel文件
    myPath='结果表-'+myKey+'录取表.xlsx'
    myNewBook.save(myPath)
