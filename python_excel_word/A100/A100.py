import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#根据指定参数创建自定义字体(myFont)
myFont=openpyxl.styles.Font(name='隶书',size=18,
                            bold=True,italic=True,color='0000FF')
#使用自定义字体(myFont)设置A1单元格的font属性
mySheet['A1'].font=myFont
myBook.save('结果表-收入表.xlsx')
