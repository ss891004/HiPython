import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
mySheet.merged_cells.ranges.clear()
myBook.save('结果表-收入表.xlsx')
