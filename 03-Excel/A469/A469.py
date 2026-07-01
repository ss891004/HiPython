import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#mySheet.protection.sheet=True
#设置修改工作表的保护密码
mySheet.protection.password='123456'
myBook.save('结果表-员工表.xlsx')
