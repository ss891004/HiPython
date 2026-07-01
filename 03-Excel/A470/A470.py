import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#根据指定的范围[A1:F12]创建(myTable)
myTable=openpyxl.worksheet.table.Table(displayName="myTable", ref="A1:F12")
#根据预置的样式(TableStyleMedium8)创建表格样式(myStyle)
myStyle=openpyxl.worksheet.table.TableStyleInfo(name="TableStyleMedium8")
#myStyle=openpyxl.worksheet.table.TableStyleInfo(name="TableStyleMedium13")
#在表格(myTable)中应用新建的表格样式(myStyle)
myTable.tableStyleInfo=myStyle
#在工作表(mySheet)中应用自定义的表格(myTable)
mySheet.add_table(myTable)
myBook.save('结果表-员工表.xlsx')
