import openpyxl
from PIL import Image
myBook=openpyxl.load_workbook('新书订购表.xlsx')
mySheet=myBook.active
myImage1=openpyxl.drawing.image.Image('images/myImage1.jpg')
mySheet.add_image(myImage1,'A5')
#根据指定的图像文件创建图像(myImage2)
myImage2=Image.open('images/myImage2.jpg')
#将图像(myImage2)旋转90度并保存在temp目录中
myImage2.rotate(90).save('temp/myImage2.jpg')
#根据temp/myImage2.jpg这个旋转之后的图像(文件)创建图像(myImage2Rotate)
myImage2Rotate=openpyxl.drawing.image.Image('temp/myImage2.jpg')
#在新书订购表(mySheet)的B5单元格中添加旋转90度的图像(myImage2Rotate)
mySheet.add_image(myImage2Rotate,'B5')
myBook.save('结果表-新书订购表.xlsx')
