import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
myNames=['2月份','4月份','6月份','8月份','10月份','12月份']
i=0;myLength=len(myBook.worksheets)
while i<myLength:
      #在工作簿(myBook)的指定位置(i*2+1)创建空白的工作表
      myBook.create_sheet(myNames[i],i*2+1)
      i+=1
myBook.save('结果表-利润表.xlsx')
