import openpyxl
myBook=openpyxl.load_workbook('五百强企业表.xlsx',data_only=True)
mySheet=myBook['五百强企业表']
#按行获取五百强企业表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
#创建空集合(mySet)
mySet=set()
#循环五百强企业表(myRows)的行(myRow)
for myRow in myRows:
    #循环行(myRow)的公司名称(第1列单元格除外)
    for myName in myRow[1:]:
        #在集合(mySet)中添加所有的公司名称(自动删除重复的公司)
        mySet.add(myName)
#在工作簿(myBook)中创建新工作表(myNewSheet)
myNewSheet=myBook.create_sheet('所有公司表')
for myName in mySet:
    #在新工作表(myNewSheet)中添加不重复的公司名称(myName)
    myNewSheet.append([myName])
myBook.save('结果表-五百强企业表.xlsx')
