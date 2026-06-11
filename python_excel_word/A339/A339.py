import openpyxl
myBook=openpyxl.load_workbook('销量排行表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取销量排行表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
myDict={}
#在销量排行表(mySheet)中删除所有行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
for myRow in myRows:
    #如果在字典(myDict)中存在某出版社(myRow[3])，则直接在某出版社中添加[myRow]
    if myRow[3] in myDict.keys():
       myDict[myRow[3]]+=[myRow]
    #否则创建新出版社
    else:
       myDict[myRow[3]]=[myRow]
#循环字典(myDict)的出版社(myPress)
for myPress in myDict.keys():
    #根据售价对某出版社(myPress)的图书进行降序排序
    myRows=sorted(myDict[myPress],key=lambda x: x[2],reverse=True)
    #获取售价最低的图书(即经过降序排序之后的最后一本图书)
    mySheet.append(myRows[-1])
myBook.save('结果表-销量排行表.xlsx')
