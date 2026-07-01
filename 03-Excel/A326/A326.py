import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(myValues)
myValues=list(mySheet.values)
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='员工表'
myNewSheet.append(['工号','姓名','最高学历','专业','出生年份'])
#从myValues的第2行开始逐行循环(到最后一行)
for myRow in myValues[1:]:
    myList=[]
    #拼接行(myRow)的第1列的单元格数据
    myList+=[myRow[0]]
    #根据字符('-')将第2列的单元格数据拆分为包含三个成员的列表(myParts)
    myParts=list(myRow[1].partition('-'))
    #在列表(myParts)的指定位置插入行(myRow)的第3列的单元格数据
    myParts.insert(2,myRow[2]+'-')
    #将列表(myParts)的所有成员组合成一个新字符串(myNewParts)
    myNewParts=''.join(myParts)
    #将新字符串(myNewParts)添加到列表(myList)中
    myList+=[myNewParts]
    #拼接行(myRow)的第4列及后面的所有单元格数据
    myList+=myRow[3:]
    myNewSheet.append(myList)
myNewBook.save('结果表-员工表.xlsx')
