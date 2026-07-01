import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
i=0;myLength=len(myBook.worksheets)
while i<myLength:
      #如果工作表的表名月份数为奇数，则设置工作表的表名标签背景为红色
      if i%2==0:
         myBook.worksheets[i].sheet_properties.tabColor='FF0000'
      i+=1
myBook.save('结果表-利润表.xlsx')
