import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#根据指定参数(horizontal='right')自定义水平对齐样式(myAlignment)
myAlignment=openpyxl.styles.Alignment(horizontal='right')
#使用自定义水平对齐样式(myAlignment)设置A1单元格的alignment属性
mySheet['A1'].alignment=myAlignment
myBook.save('结果表-收入表.xlsx')
