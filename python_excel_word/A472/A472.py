import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#根据指定的范围(A1:F12)创建myTable
myTable=openpyxl.worksheet.table.Table(displayName="myTable", ref="A1:F12")
#以交错列背景颜色的预置样式创建myStyle
myStyle=openpyxl.worksheet.table.TableStyleInfo(name="TableStyleMedium13",
                                                showColumnStripes=True)
#在新建表格(myTable)中应用新建的样式(myStyle)
myTable.tableStyleInfo=myStyle
#在员工表(mySheet)中应用新建表格(myTable)
mySheet.add_table(myTable)
myBook.save('结果表-员工表.xlsx')
