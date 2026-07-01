import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myPieChart=openpyxl.chart.PieChart()
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
myPieChart.title="使用饼图展示华茂集团员工人数"
#在饼图底部绘制图例
myPieChart.legend.position='b'
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
