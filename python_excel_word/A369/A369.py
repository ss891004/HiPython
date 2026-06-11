import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#冻结员工表(mySheet)的D列和2行之前的所有行和列
mySheet.freeze_panes='D2'
myBook.save('结果表-员工表.xlsx')
