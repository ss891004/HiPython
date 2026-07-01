import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
#创建3D柱形图(myBarChart3D)
myBarChart3D=openpyxl.chart.BarChart3D()
#设置3D柱形图(myBarChart3D)的各个柱子的大小
myBarChart3D.add_data(openpyxl.chart.Reference(mySheet,
      min_col=2,max_col=3,min_row=3,max_row=8),titles_from_data=True)
#设置3D柱形图(myBarChart3D)的公司名称标签
myBarChart3D.set_categories(openpyxl.chart.Reference(mySheet,
                                       min_col=1,min_row=4,max_row=8))
#表示使用3D条形图风格显示3D柱形图(myBarChart3D)
myBarChart3D.type="bar"
#设置3D柱形图(myBarChart3D)的标题
myBarChart3D.title="使用3D条形图展示华茂集团员工人数"
#将3D柱形图添加到员工表(mySheet)的A9单元格
mySheet.add_chart(myBarChart3D,"A9")
myBook.save('结果表-员工表.xlsx')
