import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.style=26
myPieChart.title="华茂集团员工分布图"
myPieChart.legend.position='b'
#自定义饼图的大小和位置
myPieChart.layout=openpyxl.chart.layout.Layout(
               openpyxl.chart.layout.ManualLayout(h=0.5,w=0.5,x=-0.8,y=0.01))
#myPieChart.layout=openpyxl.chart.layout.Layout(
#              openpyxl.chart.layout.ManualLayout(h=0.5,w=0.5,x=0.8,y=0.01))
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
