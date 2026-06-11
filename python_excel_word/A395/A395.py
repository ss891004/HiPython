import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.title="使用饼图展示华茂集团员工人数"
#创建凸出显示的切片(mySlice)
mySlice=openpyxl.chart.series.DataPoint(idx=1,explosion=10)
myPieChart.series[0].data_points=[mySlice]
#将饼图(myPieChart)添加到员工表的C1单元格
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
