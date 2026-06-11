import openpyxl
myBook=openpyxl.load_workbook('房价表.xlsx')
mySheet=myBook.active
#创建折线图(myLineChart)
myLineChart=openpyxl.chart.LineChart()
#设置折线图(myLineChart)的数据点(在y轴上的位置)
myLineChart.add_data(openpyxl.chart.Reference(mySheet,
      min_col=2,max_col=2,min_row=3,max_row=15),titles_from_data=True)
#设置折线图(myLineChart)的x轴的月份标签
myLineChart.set_categories(openpyxl.chart.Reference(mySheet,
                                      min_col=1,min_row=4,max_row=15))
#设置折线图(myLineChart)的标题
myLineChart.title="使用折线图展示2018年度房价走势"
#将折线图(myLineChart)添加到房价表(mySheet)的C1单元格
mySheet.add_chart(myLineChart,"C1")
myBook.save('结果表-房价表.xlsx')
