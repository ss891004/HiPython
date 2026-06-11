import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myDoughnutChart=openpyxl.chart.DoughnutChart(holeSize=50,firstSliceAng=270)
myDoughnutChart.add_data(openpyxl.chart.Reference(mySheet,
                                     min_col=2,min_row=4,max_row=9))
myDoughnutChart.set_categories(openpyxl.chart.Reference(mySheet,
                                     min_col=1,min_row=4,max_row=9))
#设置圆环图(myDoughnutChart)各个切片的填充颜色
mySlices=[openpyxl.chart.series.DataPoint(idx=i) for i in range(6)]
mySlices[0].graphicalProperties.solidFill="FF0000"
mySlices[1].graphicalProperties.solidFill="00FF00"
mySlices[2].graphicalProperties.solidFill="0000FF"
mySlices[3].graphicalProperties.solidFill="00FFFF"
mySlices[4].graphicalProperties.solidFill="FFFF00"
mySlices[5].graphicalProperties.noFill=True
myDoughnutChart.series[0].data_points=mySlices
#自定义圆环图(myDoughnutChart)的大小和位置
myDoughnutChart.layout=openpyxl.chart.layout.Layout(
        openpyxl.chart.layout.ManualLayout(h=0.6, w=0.6,x=0.1,y=0.3))
myDoughnutChart.title="使用圆环图展示华茂集团员工人数"
mySheet.add_chart(myDoughnutChart,"C1")
myBook.save('结果表-员工表.xlsx')
