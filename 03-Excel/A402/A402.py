import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myBarChart3D=openpyxl.chart.BarChart3D()
myBarChart3D.add_data(openpyxl.chart.Reference(mySheet,
                       min_col=2,min_row=3,max_row=8),titles_from_data=True)
myBarChart3D.set_categories(openpyxl.chart.Reference(mySheet,
                       min_col=1,min_row=4,max_row=8))
myBarChart3D.title="使用3D柱形图展示华茂集团员工人数"
#设置3D柱形图(myBarChart3D)的样式
#myBarChart3D.style=5
myBarChart3D.style=14
mySheet.add_chart(myBarChart3D,"A9")
myBook.save('结果表-员工表.xlsx')
