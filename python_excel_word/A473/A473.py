import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#在员工表(mySheet)中设置过滤范围(A1:D12)
mySheet.auto_filter.ref="A1:D12"
#表示在员工表(mySheet)的第4列中默认过滤“博士”
mySheet.auto_filter.add_filter_column(3,["博士"])
myBook.save('结果表-员工表.xlsx')
