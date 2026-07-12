import openpyxl
myBook=openpyxl.load_workbook('新书订购表.xlsx')
mySheet=myBook.active
#根据指定的图像文件创建图像(myImage1)
myImage1=openpyxl.drawing.image.Image('images/myImage1.jpg')
#自定义图像(myImage1)的宽度和高度
myImage1.width=100
myImage1.height=100
#在新书订购书(mySheet)的A5单元格中添加图像(myImage1)
mySheet.add_image(myImage1,'A5')
myImage2=openpyxl.drawing.image.Image('images/myImage2.jpg')
mySheet.add_image(myImage2,'B5')
myBook.save('结果表-新书订购表.xlsx')
