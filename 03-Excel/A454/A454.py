import openpyxl
myBook=openpyxl.load_workbook('房价表.xlsx')
mySheet=myBook.active
myLineChart=openpyxl.chart.LineChart()
myLineChart.add_data(openpyxl.chart.Reference(mySheet,
                        min_col=2,max_col=2,min_row=4,max_row=15))
myLineChart.set_categories(openpyxl.chart.Reference(mySheet,
                                  min_col=1,min_row=4,max_row=15))
#在折线图(myLineChart)上按照从大到小的顺序绘制x轴的刻度
myLineChart.x_axis.scaling.orientation="maxMin"
# #在折线图(myLineChart)上按照从小到大的顺序绘制x轴的刻度(默认方式)
#myLineChart.x_axis.scaling.orientation="minMax"
myLineChart.series[0].graphicalProperties.line.solidFill="FF0000"
myLineChart.series[0].graphicalProperties.line.width=15000
myLineChart.series[0].graphicalProperties.line.dashStyle="sysDash"
myLineChart.legend=None
myLineChart.title="使用折线图展示2018年度房价走势"
mySheet.add_chart(myLineChart,"C1")
myBook.save('结果表-房价表.xlsx')
