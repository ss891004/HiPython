import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=5))
mySlices=[openpyxl.chart.series.DataPoint(idx=i) for i in range(2)]
#使用蓝色(0000FF)填充女性人数切片(mySlices[0])
mySlices[0].graphicalProperties.solidFill="0000FF"
#禁止使用颜色填充男性人数切片(mySlices[1])
mySlices[1].graphicalProperties.noFill=True
myPieChart.series[0].data_points=mySlices
#设置禁止绘制饼图(myPieChart)的图例
myPieChart.legend=None
myPieChart.title="使用扇形图展示华茂集团女工人数"
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
