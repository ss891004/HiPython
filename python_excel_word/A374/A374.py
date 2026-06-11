import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#隐藏员工表(mySheet)的D列、E列、F列
mySheet.column_dimensions.group('D','F', hidden=True)
myBook.save('结果表-员工表.xlsx')
