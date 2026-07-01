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
#设置折线的宽度为15000
myLineChart.series[0].graphicalProperties.line.width=15000
# #设置虚线绘制折线
#myLineChart.series[0].graphicalProperties.line.dashStyle="sysDot"
#设置数据点的图形符号(正方形)
myLineChart.series[0].marker.symbol="square"
##设置数据点的图形符号(三角形)
#myLineChart.series[0].marker.symbol="triangle"
#设置数据点的图形符号的填充颜色(红色)
myLineChart.series[0].marker.graphicalProperties.solidFill="FF0000"
#设置数据点的图形符号的边线颜色(红色)
myLineChart.series[0].marker.graphicalProperties.line.solidFill="FF0000"
myLineChart.legend=None
myLineChart.title="使用折线图展示2018年度房价走势"
mySheet.add_chart(myLineChart,"C1")
myBook.save('结果表-房价表.xlsx')
