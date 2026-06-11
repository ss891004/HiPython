import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.series[0].dLbls=openpyxl.chart.label.DataLabelList()
myPieChart.series[0].dLbls.showCatName=True
mySlices=[openpyxl.chart.series.DataPoint(idx=i) for i in range(5)]
myPieChart.series[0].data_points=mySlices
#设置第1个切片(mySlices[0])无填充颜色
mySlices[0].graphicalProperties.noFill=True
#设置第1个切片(mySlices[0])的边线颜色为黑色
mySlices[0].graphicalProperties.line.solidFill="000000"
mySlices[1].graphicalProperties.noFill=True
mySlices[1].graphicalProperties.line.solidFill="000000"
mySlices[2].graphicalProperties.noFill=True
mySlices[2].graphicalProperties.line.solidFill="000000"
mySlices[3].graphicalProperties.noFill=True
mySlices[3].graphicalProperties.line.solidFill="000000"
mySlices[4].graphicalProperties.noFill=True
mySlices[4].graphicalProperties.line.solidFill="000000"
myPieChart.title="使用饼图展示华茂集团员工人数"
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
