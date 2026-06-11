import openpyxl
myBook=openpyxl.load_workbook('交易表.xlsx')
mySheet=myBook.active
#创建股票图(myStockChart)
myStockChart=openpyxl.chart.StockChart()
#获取交易表(mySheet)的A4:A8范围的单元格数据
myLabels=openpyxl.chart.Reference(mySheet,min_col=1,min_row=4,max_row=8)
#获取交易表(mySheet)的C4:F8范围的单元格数据
myData=openpyxl.chart.Reference(mySheet,min_col=3,
                                max_col=6,min_row=3,max_row=8)
#设置股票图(myStockChart)的数据点(开盘价、最高价、最低价和收盘价)
myStockChart.add_data(myData,titles_from_data=True)
#设置股票图(myStockChart)的x轴的标签
myStockChart.set_categories(myLabels)
#在股票图(myStockChart)上禁止绘制默认的开盘价、最高价、最低价和收盘价折线
for mySeries in myStockChart.series:
    mySeries.graphicalProperties.line.noFill=True
#在股票图(myStockChart)上绘制开盘价和收盘价的数据点之间的柱子
myStockChart.upDownBars=openpyxl.chart.updown_bars.UpDownBars()
#在股票图(myStockChart)上绘制最高价和最低价的数据点之间的连线
myStockChart.hiLowLines=openpyxl.chart.updown_bars.ChartLines()
from openpyxl.chart.data_source import NumData, NumVal
myPoints=[NumVal(idx=i) for i in range(len(myData)-1)]
myCache=NumData(pt=myPoints)
myStockChart.series[-1].val.numRef.numCache=myCache
#设置在股票图(myStockChart)上禁止绘制y轴主网格线
myStockChart.y_axis.majorGridlines=None
#创建成交量柱形图(myBarChart)
myBarChart=openpyxl.chart.BarChart()
myBarChart.add_data(openpyxl.chart.Reference(mySheet,
                    min_col=2,min_row=3,max_row=8),titles_from_data=True)
myBarChart.set_categories(myLabels)
#在成交量柱形图(myBarChart)上设置禁止绘制y轴主网格线
myBarChart.y_axis.majorGridlines=None
myBarChart.title="使用股票图展示交易价和交易量"
#在成交量柱形图(myBarChart)上叠加股票图
#myBarChart.y_axis.axId=10
myBarChart.y_axis.axId=11
myBarChart.y_axis.crosses="max"
myBarChart+=myStockChart
#将股票图(myStockChart)和成交量图(myBarChart)添加到交易表(mySheet)的A9单元格
mySheet.add_chart(myBarChart,"A9")
myBook.save('结果表-交易表.xlsx')
