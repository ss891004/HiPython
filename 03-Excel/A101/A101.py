import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#根据指定参数(vertical='center')创建垂直对齐样式(myAlignment)
myAlignment=openpyxl.styles.Alignment(vertical='center')
#使用垂直对齐样式(myAlignment)设置A1单元格的alignment属性
mySheet['A1'].alignment=myAlignment
myBook.save('结果表-收入表.xlsx')
