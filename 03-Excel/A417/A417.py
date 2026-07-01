import openpyxl
myBook=openpyxl.load_workbook('房价表.xlsx')
mySheet=myBook.active
myLineChart=openpyxl.chart.LineChart()
myLineChart.add_data(openpyxl.chart.Reference(mySheet,
                       min_col=2,max_col=2,min_row=4,max_row=15))
myLineChart.set_categories(openpyxl.chart.Reference(mySheet,
                                 min_col=1,min_row=4,max_row=15))
#使用红色绘制折线
myLineChart.series[0].graphicalProperties.line.solidFill="FF0000"
#设置折线的宽度为50000
myLineChart.series[0].graphicalProperties.line.width=50000
#设置折线的样式为虚线
myLineChart.series[0].graphicalProperties.line.dashStyle="sysDot"
myLineChart.legend=None
myLineChart.title="使用折线图展示2018年度房价走势"
mySheet.add_chart(myLineChart,"C1")
myBook.save('结果表-房价表.xlsx')
