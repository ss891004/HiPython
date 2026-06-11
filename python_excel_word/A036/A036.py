import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#对收入表(mySheet)的D列的第5、6、7、8行数据求和
myColDSum=sum([myCell.value for myCell in mySheet['D'][4:]])
#对收入表(mySheet)的C列的第5、6、7、8行数据求和
myColCSum=sum([myCell.value for myCell in mySheet['C'][4:]])
#对收入表(mySheet)的B列的第5、6、7、8行数据求和
myColBSum=sum([myCell.value for myCell in mySheet['B'][4:]])
#在收入表(mySheet)的D列、C列、B列的第9行中写入合计金额
mySheet['D9']=myColDSum
mySheet['C9']=myColCSum
mySheet['B9']=myColBSum
mySheet['A9']='合计'
myBook.save('结果表-收入表.xlsx')
