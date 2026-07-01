import openpyxl
myBook=openpyxl.load_workbook('房价表.xlsx')
mySheet=myBook.active
myLineChart=openpyxl.chart.LineChart()
myLineChart.add_data(openpyxl.chart.Reference(mySheet,
      min_col=2,max_col=2,min_row=3,max_row=15),titles_from_data=True)
myLineChart.set_categories(openpyxl.chart.Reference(mySheet,
                                       min_col=1,min_row=4,max_row=15))
myLineChart.title="使用折线图展示2018年度房价走势"
#设置折线图(myLineChart)的样式(取值范围：1-48)
#myLineChart.style=39
myLineChart.style=44
mySheet.add_chart(myLineChart,"C1")
myBook.save('结果表-房价表.xlsx')
