import openpyxl
from PIL import Image
myBook=openpyxl.load_workbook('新书订购表.xlsx')
mySheet=myBook.active
myImage1=openpyxl.drawing.image.Image('images/myImage1.jpg')
mySheet.add_image(myImage1,'A5')
#根据指定的图像文件创建图像(myImage2)
myImage2=Image.open('images/myImage2.jpg')
#根据指定的参数裁剪图像(myImage2)，并将裁剪结果保存在temp目录中
myImage2.crop((39,11,167,188)).save('temp/myImage2.jpg')
#根据temp/myImage2.jpg这个裁剪之后的图像(文件)创建图像(myNewImage2)
myNewImage2=openpyxl.drawing.image.Image('temp/myImage2.jpg')
#在新书订购表(mySheet)的B5单元格中添加裁剪之后的图像(myNewImage2)
mySheet.add_image(myNewImage2,'B5')
myBook.save('结果表-新书订购表.xlsx')
