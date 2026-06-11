import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myBarChart=openpyxl.chart.BarChart()
myBarChart.add_data(openpyxl.chart.Reference(mySheet,
      min_col=2,max_col=3,min_row=3,max_row=8),titles_from_data=True)
myBarChart.set_categories(openpyxl.chart.Reference(mySheet,
                                      min_col=1,min_row=4,max_row=8))
myBarChart.title="使用柱形图展示华茂集团员工人数"
mySheet.add_chart(myBarChart,"A9")
myBook.save('结果表-员工表.xlsx')
