import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
#按行获取收入表(myBook.worksheets[0])的单元格数据
myRows=list(myBook.worksheets[0].values)
#实现行列数据交换，即行转换成列，列转换成行
myCols=list(zip(*list(myRows[4:8])))[1:4]
myIndex=2
for myCol in myCols:
    #对行数据求和，即是对列数据求和
    myColSum=sum(myCol)
    myBook.worksheets[0].cell(9, myIndex).value=myColSum
    myIndex+=1
myBook.save('结果表-收入表.xlsx')
