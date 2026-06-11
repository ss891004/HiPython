import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myBarChart=openpyxl.chart.BarChart()
myBarChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                              min_row=3,max_row=8),titles_from_data=True)
myBarChart.set_categories(openpyxl.chart.Reference(mySheet,
                                           min_col=1,min_row=4,max_row=8))
myBarChart.legend=None
myBarChart.title="使用柱形图展示华茂集团员工人数"
myBarChart.style=26
#自定义柱形图(myBarChart)各个柱子的填充颜色
myColumns=[openpyxl.chart.series.DataPoint(idx=i) for i in range(5)]
myBarChart.series[0].data_points=myColumns
myColumns[0].graphicalProperties.solidFill="FAE1D0"
myColumns[1].graphicalProperties.solidFill="BB2244"
myColumns[2].graphicalProperties.solidFill="22DD22"
myColumns[3].graphicalProperties.solidFill="61210B"
myColumns[4].graphicalProperties.solidFill="915102"
mySheet.add_chart(myBarChart,"C1")
myBook.save('结果表-员工表.xlsx')
