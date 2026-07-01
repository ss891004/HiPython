import openpyxl
myBook=openpyxl.load_workbook('成交表.xlsx')
mySheet=myBook.active
myLineChart=openpyxl.chart.LineChart()
myLineChart.add_data(openpyxl.chart.Reference(mySheet,
                         min_col=2,max_col=2,min_row=4,max_row=15))
myLineChart.set_categories(openpyxl.chart.Reference(mySheet,
                                  min_col=1,min_row=4,max_row=15))
#自定义折线图(myLineChart)的x轴的日期格式(根据标签)
#myLineChart.x_axis.number_format='yyyy年mm月dd日'
myLineChart.x_axis.number_format='d日'
myLineChart.series[0].graphicalProperties.line.solidFill="FF0000"
myLineChart.series[0].graphicalProperties.line.width=15000
myLineChart.legend=None
myLineChart.title="使用折线图展示2020年7月成交记录"
mySheet.add_chart(myLineChart,"C1")
myBook.save('结果表-成交表.xlsx')
