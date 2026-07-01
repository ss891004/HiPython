import openpyxl
myBook=openpyxl.load_workbook('房价表.xlsx')
mySheet=myBook.active
myLineChart=openpyxl.chart.LineChart()
myLineChart.add_data(openpyxl.chart.Reference(mySheet,
      min_col=2,max_col=4,min_row=3,max_row=15),titles_from_data=True)
myLineChart.set_categories(openpyxl.chart.Reference(mySheet,
                                      min_col=1,min_row=4,max_row=15))
myLineChart.title="使用折线图展示2018年度房价走势"
myLineChart.style=34
mySheet.add_chart(myLineChart,"E1")
myBook.save('结果表-房价表.xlsx')
