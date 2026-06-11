import openpyxl
#初始化列表(myData)的数据
myData=[['公司名称','员工人数'],['南京分公司',8600],
          ['广州分公司',6200],['武汉分公司',4800],
          ['郑州分公司',7300],['重庆分公司',9600]]
#创建工作簿(myBook)及工作表(mySheet)
myBook=openpyxl.Workbook()
mySheet=myBook.active
mySheet.title="员工表"
for myRow in myData:
    mySheet.append(myRow)
#创建饼图(myPieChart)
myPieChart=openpyxl.chart.PieChart()
#根据员工表(mySheet)的B2:B6范围的单元格数据设置饼图(myPieChart)的切片大小
myPieChart.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                             min_row=2,max_row=6))
#根据员工表(mySheet)的A2:A6范围的单元格数据设置饼图(myPieChart)的图例数据
myPieChart.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                   min_row=2,max_row=6))
#设置饼图(myPieChart)的标题
myPieChart.title="使用饼图展示华茂集团员工人数"
#将饼图(myPieChart)添加到员工表(mySheet)的C1单元格
mySheet.add_chart(myPieChart, "C1")
myBook.save("员工表.xlsx")
