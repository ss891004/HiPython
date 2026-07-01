import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
myList=[]
for myCells in mySheet.merged_cells:
    myList.append(str(myCells))
for myCells in myList:
    mySheet.unmerge_cells(myCells)
myBook.save('结果表-收入表.xlsx')
