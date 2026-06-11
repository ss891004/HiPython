import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#创建3D饼图(myPieChart3D)
myPieChart3D=openpyxl.chart.PieChart3D()
#根据员工表(mySheet)的B4:B8范围的单元格数据设置3D饼图的各个切片大小
myPieChart3D.add_data(openpyxl.chart.Reference(mySheet,min_col=2,
                                               min_row=4,max_row=8))
#根据员工表(mySheet)的A4:A8范围的单元格数据设置3D饼图的图例数据
myPieChart3D.set_categories(openpyxl.chart.Reference(mySheet,min_col=1,
                                                     min_row=4,max_row=8))
#设置3D饼图(myPieChart3D)的标题
myPieChart3D.title="使用3D饼图展示华茂集团员工人数"
#在3D饼图(myPieChart3D)上设置凸出显示的切片
mySlice1=openpyxl.chart.series.DataPoint(idx=1, explosion=20)
mySlice2=openpyxl.chart.series.DataPoint(idx=2, explosion=20)
myPieChart3D.series[0].data_points=[mySlice1,mySlice2]
#将3D饼图(myPieChart3D)添加到员工表(mySheet)的C1单元格
mySheet.add_chart(myPieChart3D,"C1")
myBook.save('结果表-员工表.xlsx')
