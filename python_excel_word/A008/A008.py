import openpyxl
myBook=openpyxl.load_workbook('利润表.xlsx')
myNames=['1月份利润表','2月份利润表','3月份利润表','4月份利润表',
         '5月份利润表','6月份利润表','7月份利润表','8月份利润表',
         '9月份利润表','10月份利润表','11月份利润表','12月份利润表']
#循环列表(myNames)的表名(myName)，如'1月份利润表'等
for myName in myNames:
    #在工作簿(myBook)中根据利润表(myBook.worksheets[0])复制工作表(mySheet)
    mySheet=myBook.copy_worksheet(myBook.worksheets[0])
    #重新设置复制工作表的表名
    mySheet.title=myName
myPath='结果表-利润表.xlsx'
myBook.save(myPath)
