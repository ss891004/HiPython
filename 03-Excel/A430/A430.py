import openpyxl
myBook=openpyxl.load_workbook('房价表.xlsx')
mySheet=myBook.active
myLineChart3D=openpyxl.chart.LineChart3D()
myLineChart3D.add_data(openpyxl.chart.Reference(mySheet,
      min_col=2,max_col=2,min_row=3,max_row=15),titles_from_data=True)
myLineChart3D.set_categories(openpyxl.chart.Reference(mySheet,
                                       min_col=1,min_row=4,max_row=15))
#设置3D折线图(myLineChart3D)的样式(37)
myLineChart3D.style=37
myLineChart3D.legend=None
myLineChart3D.title="使用3D折线图展示2018年度房价走势"
mySheet.add_chart(myLineChart3D,"C1")
myBook.save('结果表-房价表.xlsx')
