import openpyxl
myBook=openpyxl.load_workbook('新书订购表.xlsx')
mySheet=myBook['新书订购表']
#按行获取新书订购表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myList=[]
for myRow in myRows:
    myList+=[myRow[0]]
#根据书名的长度进行降序排列
myList.sort(key=len,reverse=True)
#在新书订购表(mySheet)中删除所有的行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
#在新书订购表(mySheet)中添加倒序排列的书名
for myRow in myList:
    mySheet.append([myRow])
myBook.save('结果表-新书订购表.xlsx')
