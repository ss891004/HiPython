import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#创建饼图(myPieChart)
myPieChart=openpyxl.chart.PieChart()
#根据员工表(mySheet)的B4:B8范围的单元格数据设置饼图(myPieChart)的切片大小
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=4,max_row=8))
#根据员工表(mySheet)的A4:A8范围的单元格数据设置饼图(myPieChart)的图例数据
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=4,max_row=8))
#设置饼图(myPieChart)的标题
myPieChart.title="使用饼图展示华茂集团员工人数"
#将饼图(myPieChart)添加到员工表(mySheet)的C1单元格
mySheet.add_chart(myPieChart,"C1")
myBook.save('结果表-员工表.xlsx')
