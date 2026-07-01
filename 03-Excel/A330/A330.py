import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='员工表'
myNewSheet.append(['工号','部门','姓名','最高学历','专业','出生日期'])
#在myRows中倒序排列所有的行
myRows.reverse()
for myRow in myRows:
    #在新员工表(myNewSheet)中添加经过倒序排列的行
    myNewSheet.append(myRow)
myNewBook.save('结果表-员工表.xlsx')
