import openpyxl
myBook=openpyxl.load_workbook('城市排名表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取城市排名表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
#使用集合推导式在myRows中筛选包含'广州'的行(mySet)
mySet={myRow for myRow in myRows if '广州' in myRow[1]}
#在城市排名表(mySheet)中删除所有行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
#将筛选结果(mySet)重新写入城市排名表(mySheet)
for myRow in mySet:
    mySheet.append(myRow)
myBook.save('结果表-城市排名表.xlsx')
