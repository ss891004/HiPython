import openpyxl
myBook=openpyxl.load_workbook('销售表.xlsx')
mySheet=myBook.active
#创建气泡图(myBubbleChart)
myBubbleChart=openpyxl.chart.BubbleChart()
#获取销售表(mySheet)的气温数据
myTemperature=openpyxl.chart.Reference(mySheet,min_col=1,min_row=4,max_row=8)
#获取销售表(mySheet)的价格数据
myPrice=openpyxl.chart.Reference(mySheet,min_col=2,min_row=4,max_row=8)
#获取销售表(mySheet)的销量数据
myAmount=openpyxl.chart.Reference(mySheet,min_col=3,min_row=4,max_row=8)
#根据气温、价格、销量数据创建气泡图系列(mySeries)
mySeries=openpyxl.chart.Series(values=myPrice, xvalues=myTemperature,
        zvalues=myAmount,title="维冠纯净水试销统计气泡图")
#在气泡图(myBubbleChart)中添加新建的系列(mySeries)
myBubbleChart.series.append(mySeries)
#设置气泡图(myBubbleChart)的样式
myBubbleChart.style=26
#在气泡图(myBubbleChart)的底部绘制图例
myBubbleChart.legend.position='b'
#设置气泡图(myBubbleChart)的标题
myBubbleChart.title="使用气泡图展示气温、价格和销量的关系"
#将气泡图(myBubbleChart)添加到销售表(mySheet)的D1单元格
mySheet.add_chart(myBubbleChart,"D1")
myBook.save('结果表-销售表.xlsx')
