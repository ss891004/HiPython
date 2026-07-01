import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.title="华茂集团员工分布图"
#设置饼图的宽度
myPieChart.width=8
#myPieChart.width=12
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
