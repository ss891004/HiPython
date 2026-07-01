import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
#删除员工表(mySheet)的行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
myList=[]
for myRow in myRows:
    #如果在列表(myList)中不存在行(myRow)
    if myRow not in myList:
        #则在列表(myList)中添加行(myRow)
        myList.append(myRow)
#在员工表(mySheet)中添加不重复的行(myRow)
for myRow in myList:
    mySheet.append(myRow)
myBook.save('结果表-员工表.xlsx')
