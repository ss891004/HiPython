import openpyxl
myBook=openpyxl.load_workbook('销量排行表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取销量排行表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
#在销量排行表(mySheet)中删除所有行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
for myRow in myRows:
    #如果售价大于100,且出版社含有‘清华大学出版社’
    if myRow[2]>100 and '清华大学出版社' in myRow[3]:
       #则在销量排行表(mySheet)中添加此图书(myRow)
       mySheet.append(myRow)
myBook.save('结果表-销量排行表.xlsx')
