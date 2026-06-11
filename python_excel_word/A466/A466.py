import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#根据参数创建圆环图(myDoughnutChart)
myDoughnutChart=openpyxl.chart.DoughnutChart(holeSize=50)
myDoughnutChart.add_data(openpyxl.chart.Reference(mySheet,
                                     min_col=2,min_row=4,max_row=8))
myDoughnutChart.set_categories(openpyxl.chart.Reference(mySheet,
                                     min_col=1,min_row=4,max_row=8))
myDoughnutChart.style=26
myDoughnutChart.series[0].dLbls=openpyxl.chart.label.DataLabelList()
#在圆环图(myDoughnutChart)的各个切片上显示百分比
myDoughnutChart.series[0].dLbls.showPercent=True
myDoughnutChart.title="使用圆环图展示华茂集团员工人数"
mySheet.add_chart(myDoughnutChart,"C1")
myBook.save('结果表-员工表.xlsx')
