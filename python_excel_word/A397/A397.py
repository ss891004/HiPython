import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myBarChart=openpyxl.chart.BarChart()
myBarChart.add_data(openpyxl.chart.Reference(mySheet,
                                min_col=2,min_row=4,max_row=8))
myBarChart.set_categories(openpyxl.chart.Reference(mySheet,
                                 min_col=1,min_row=4,max_row=8))
myBarChart.title="使用柱形图展示华茂集团员工人数"
myDataPoint=openpyxl.chart.series.DataPoint(idx=0)
myBarChart.series[0].data_points=[myDataPoint]
mySheet.add_chart(myBarChart,"C1")
myBook.save('结果表-员工表.xlsx')
