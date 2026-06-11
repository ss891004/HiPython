import openpyxl
myBook=openpyxl.load_workbook('交易表.xlsx')
mySheet=myBook.active
#创建股票图(myStockChart)
myStockChart=openpyxl.chart.StockChart()
#获取交易表(mySheet)的A4:A8范围的单元格数据
myLabels=openpyxl.chart.Reference(mySheet,min_col=1,min_row=4,max_row=8)
#获取交易表(mySheet)的C4:D8范围的单元格数据
myData=openpyxl.chart.Reference(mySheet,min_col=3,
                                max_col=4,min_row=3,max_row=8)
#设置股票图(myStockChart)的数据点(开盘价和收盘价)
myStockChart.add_data(myData,titles_from_data=True)
#设置股票图(myStockChart)的x轴的标签
myStockChart.set_categories(myLabels)
#禁止绘制开盘价和收盘价默认的折线
for mySeries in myStockChart.series:
    mySeries.graphicalProperties.line.noFill=True
#根据开盘价和收盘价绘制柱形图
myStockChart.upDownBars=openpyxl.chart.updown_bars.UpDownBars()
#设置股票图(myStockChart)的标题
myStockChart.title="使用股票图展示开盘价和收盘价"
#将股票图(myStockChart)添加到交易表(mySheet)的A9单元格
mySheet.add_chart(myStockChart,"A9")
myBook.save('结果表-交易表.xlsx')
