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
#设置股票图股票图(myStockChart)的数据点
myStockChart.add_data(myData,titles_from_data=True)
#设置股票图股票图(myStockChart)的x轴的标签
myStockChart.set_categories(myLabels)
#使用横线(图形符号)绘制数据点(最高价和最低价)
for mySeries in myStockChart.series:
    mySeries.graphicalProperties.line.noFill=True
    mySeries.marker.symbol="dash"
    mySeries.marker.size=15
#使用竖线绘制两个数据点(最高价和最低价)之间的连线
myStockChart.hiLowLines=openpyxl.chart.updown_bars.ChartLines()
from openpyxl.chart.data_source import NumData, NumVal
myPoints=[NumVal(idx=i) for i in range(len(myData)-1)]
myCache=NumData(pt=myPoints)
myStockChart.series[-2].val.numRef.numCache=myCache
#设置股票图(myStockChart)的标题
myStockChart.title="使用股票图展示最高价和最低价"
#将股票图(myStockChart)添加到交易表(mySheet)的A9单元格
mySheet.add_chart(myStockChart,"A9")
myBook.save('结果表-交易表.xlsx')
