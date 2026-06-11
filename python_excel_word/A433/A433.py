import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.series[0].dLbls=openpyxl.chart.label.DataLabelList()
#在饼图(myPieChart)的切片上显示标签
myPieChart.series[0].dLbls.showCatName=True
#在饼图(myPieChart)的切片上显示百分比
myPieChart.series[0].dLbls.showPercent=True
myPieChart.title="使用饼图展示华茂集团员工人数"
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
