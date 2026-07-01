import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
#myRows=list(myBook['收入表'].values)
#获取收入表(myBook.worksheets[0])的单元格数据(myRows)
myRows=list(myBook.worksheets[0].values)
myRowIndex=4
#从myRows的第5行开始循环(到最后一行)
while myRowIndex<len(myRows):
      #对每行的[1:4]范围(第2、3、4列)的单元格数据求和
      myRowSum=sum(myRows[myRowIndex][1:4])
      #将求和结果写入合计列
      myBook.worksheets[0].cell(myRowIndex+1,5).value=myRowSum
      myRowIndex+=1
myBook.save('结果表-收入表.xlsx')
