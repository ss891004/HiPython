import openpyxl
import random
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)所有单元格的数据(第1行除外)
myValues=list(mySheet.values)[1:]
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='员工表'
myNewSheet.append(['工号','部门','姓名','最高学历',
                   '专业','出生年份','出生月份','出生日'])
#随机排列行
random.shuffle(myValues)
#在新员工表(myNewSheet)中添加经过随机排列的行
for myRow in myValues:
    myNewSheet.append(myRow)
myNewBook.save('结果表-员工表.xlsx')
