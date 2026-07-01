import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(myValues)
myValues=list(mySheet.values)
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='员工表'
myNewSheet.append(['工号','部门','姓名','最高学历','专业','出生年份'])
#从myValues的第2行开始逐行循环(到最后一行)
for myRow in myValues[1:]:
    #创建列表(myList)，用于拼接每行各个列的单元格数据
    myList=[]
    #拼接每行(myRow)的第1列的数据
    myList+=[myRow[0]]
    #根据'-'字符将每行(myRow)的第2列的数据拆分为包含三个成员的列表(myParts)
    myParts=list(myRow[1].partition('-'))
    #删除列表(myParts)的第二个成员，即删除'-'字符
    del myParts[1]
    #拼接拆分之后的部门和姓名(即列表(myParts)剩下的两个成员)
    myList+=myParts
    #拼接每行(myRow)的第3列及后面列的所有数据
    myList+=myRow[2:]
    myNewSheet.append(myList)
myNewBook.save('结果表-员工表.xlsx')
