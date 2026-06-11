import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#创建柱形图(myBarChart)
myBarChart=openpyxl.chart.BarChart()
#设置柱形图(myBarChart)各个柱子的高度(大小)
myBarChart.add_data(openpyxl.chart.Reference(mySheet,
                  min_col=2,min_row=4,max_col=6,max_row=4),from_rows=True)
#设置柱形图(myBarChart)的x轴的公司名称标签
myBarChart.set_categories(openpyxl.chart.Reference(mySheet,
                  min_col=2,max_col=6,min_row=3,max_row=3))
#设置柱形图(myBarChart)的样式
myBarChart.style=26
#自定义柱形图(myBarChart)的各个柱子的颜色
myColumns=[openpyxl.chart.series.DataPoint(idx=i) for i in range(5)]
myBarChart.series[0].data_points=myColumns
myColumns[0].graphicalProperties.solidFill="FAE1D0"
myColumns[1].graphicalProperties.solidFill="BB2244"
myColumns[2].graphicalProperties.solidFill="22DD22"
myColumns[3].graphicalProperties.solidFill="61210B"
myColumns[4].graphicalProperties.solidFill="915102"
#在柱形图(myBarChart)上禁止绘制图例
myBarChart.legend=None
#设置柱形图(myBarChart)的标题
myBarChart.title="使用柱形图展示华茂集团员工人数"
#将柱形图(myBarChart)添加到员工表(mySheet)的A5单元格
mySheet.add_chart(myBarChart,"A5")
myBook.save('结果表-员工表.xlsx')
