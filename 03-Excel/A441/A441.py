import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.style=26
#自定义饼图各个切片的填充颜色
mySlices=[openpyxl.chart.series.DataPoint(idx=i) for i in range(5)]
myPieChart.series[0].data_points=mySlices
mySlices[0].graphicalProperties.solidFill="FF0000" #红色
mySlices[1].graphicalProperties.solidFill="00FF00" #绿色
mySlices[2].graphicalProperties.solidFill="0000FF" #蓝色
mySlices[3].graphicalProperties.solidFill="000000" #黑色
mySlices[4].graphicalProperties.solidFill="00FFFF" #青色
myPieChart.title="使用饼图展示华茂集团员工人数"
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
