import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
#设置饼图的样式
myPieChart.style=26
myPieChart.title="华茂集团员工分布图"
#自定义饼图的大小
myPieChart.layout=openpyxl.chart.layout.Layout(
               openpyxl.chart.layout.ManualLayout(h=0.99,w=0.99))
#myPieChart.layout=openpyxl.chart.layout.Layout(
#                openpyxl.chart.layout.ManualLayout(h=0.49,w=0.49))
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
