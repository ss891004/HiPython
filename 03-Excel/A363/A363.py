#自定义函数解析身份证号码的出生日期
def myFunc(myID):
    myList=[myID[x:y] for x,y in((6,10),(10,12),(12,14))]
    myDate='-'.join(myList)
    return myDate
import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#获取员工表(mySheet)的行(第1行除外)
myRows=list(mySheet.rows)[1:]
for myRow in myRows:
    #在行(myRow)中获取身份证号码(myID)
    myID=myRow[5].value
    #解析在身份证号码(myID)中的出生日期，
    #并将结果设置为出生日期列的单元格数据(myRow[6].value)
    myRow[6].value=myFunc(myID)
myBook.save('结果表-员工表.xlsx')
