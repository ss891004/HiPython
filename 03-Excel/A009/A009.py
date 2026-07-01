import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
myNames=myBook.sheetnames
i=0;myLength=len(myNames)
while i<myLength:
      #如果工作表表名的月份数为奇数，则删除之
      if i%2==0:
          myBook.remove(myBook[myNames[i]])
      i+=1
myBook.save('结果表-利润表.xlsx')
