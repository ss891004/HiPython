import random
import openpyxl
myBook=openpyxl.Workbook()
mySheet=myBook.active
mySheet.append(['序号','随机数'])
#生成20个在0-50000范围的随机数
for myIndex in range(1,21):
    mySheet.append([myIndex,random.randint(0,50000)])
#创建散点图(myScatterChart)
myScatterChart=openpyxl.chart.ScatterChart()
myScatterChart.title="使用散点图展示随机数"
myScatterChart.x_axis.title='序号'
myScatterChart.y_axis.title='随机数'
myScatterChart.legend=None
x=openpyxl.chart.Reference(mySheet,min_col=1,min_row=2,max_row=21)
y=openpyxl.chart.Reference(mySheet,min_col=2,min_row=2,max_row=21)
#根据随机数创建系列(mySeries)
mySeries=openpyxl.chart.Series(y,xvalues=x)
#在散点图(myScatterChart)中添加随机数系列(mySeries)
myScatterChart.append(mySeries)
#使用圆点表示散点图(myScatterChart)的随机数
myScatterChart.series[0].marker.symbol="circle"
#隐藏散点图(myScatterChart)默认添加的折线
myScatterChart.series[0].graphicalProperties.line.noFill=True
#将散点图(myScatterChart)添加到工作表(mySheet)的C3单元格
mySheet.add_chart(myScatterChart, "C3")
myBook.save("结果表-随机数表.xlsx")
