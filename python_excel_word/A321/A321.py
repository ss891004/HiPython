import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(myValues)
myValues=list(mySheet.values)
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='员工表'
myNewSheet.append(['工号','部门','姓名','最高学历','专业','出生日期'])
#从myValues的第2行开始逐行循环(到最后一行)
for myRow in myValues[1:]:
    myList=[]
    #拼接行(myRow)的第1列到第5列的单元格数据
    myList+=myRow[0:5]
    myConnector=''
    #将出生年份列、出生月份列、出生日列拼接成出生日期列
    myDate=myConnector.join(myRow[5:8])
    myList+=[myDate]
    myNewSheet.append(myList)
myNewBook.save('结果表-员工表.xlsx')
