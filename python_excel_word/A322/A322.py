import openpyxl
myBook=openpyxl.load_workbook('高校汇总表.xlsx',data_only=True)
mySheet=myBook.active
myList=[0]
#从高校汇总表(mySheet)的第2行开始逐行循环(到最后一行)
for myRow in list(mySheet.rows)[1:]:
    #在列表(myList)中添加高校列的单元格的字符串长度
    myList.append(len(myRow[1].value))
#在列表(myList)中获取最大的字符串长度，即最大列宽
myMaxWidth=max(myList)
#根据最大列宽设置高校汇总表(mySheet)的高校列(B列)的宽度
mySheet.column_dimensions['B'].width=myMaxWidth*2
myBook.save('结果表-高校汇总表.xlsx')
