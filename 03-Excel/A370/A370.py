import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook['收入表']
#表示从第2列(B列)开始
myIndex=2
#循环收入表(mySheet)的B、C、D列(A列除外)
for myColumn in list(mySheet.columns)[1:]:
    #累加列(myColumn)的第5、6、7、8行的单元格数据
    mySum=sum([myCell.value for myCell in myColumn[4:8]])
    #在单元格cell(9,myIndex)中写入合计(mySum)
    mySheet.cell(9,myIndex).value=mySum
    myIndex+=1
myBook.save('结果表-收入表.xlsx')
