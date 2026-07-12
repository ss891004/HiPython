import openpyxl
myBook=openpyxl.load_workbook('新书订购表.xlsx')
mySheet=myBook.active
#根据指定的图像文件创建myImage1图像
myImage1=openpyxl.drawing.image.Image('images/myImage1.jpg')
#在A5单元格中添加myImage1图像
mySheet.add_image(myImage1,'A5')
myImage2=openpyxl.drawing.image.Image('images/myImage2.jpg')
mySheet.add_image(myImage2,'B5')
myBook.save('结果表-新书订购表.xlsx')


'''
pip install pillow
'''