import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#根据指定的范围创建表格myTable
myTable=openpyxl.worksheet.table.Table(displayName="myTable", ref="A1:F12")
#根据预置的样式以行交错风格创建表格样式myStyle
myStyle=openpyxl.worksheet.table.TableStyleInfo(name="TableStyleMedium13",
                                                showRowStripes=True)
#在表格中应用新建的表格样式myStyle
myTable.tableStyleInfo=myStyle
#在员工表(mySheet)中应用新建表格(样式) myTable
mySheet.add_table(myTable)
myBook.save('结果表-员工表.xlsx')
