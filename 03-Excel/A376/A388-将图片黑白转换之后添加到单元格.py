import openpyxl
from PIL import Image
from PIL import ImageEnhance
myBook=openpyxl.load_workbook('生鲜订购表.xlsx')
mySheet=myBook.active
myImage1=openpyxl.drawing.image.Image('images/myImage1.jpg')
mySheet.add_image(myImage1,'A5')
#根据指定的图像文件创建图像(myImage2)
myImage2=Image.open('images/myImage2.jpg')
#将彩色图像转换成黑白图像，并将结果保存在temp目录中
myImage2.convert('L').save('temp/myImage6.jpg')
#根据temp/myImage2.jpg这个黑白图像(文件)创建图像(myNewImage2)
myNewImage2=openpyxl.drawing.image.Image('temp/myImage6.jpg')
#在生鲜订购表(mySheet)的B5单元格中添加黑白图像(myNewImage2)
mySheet.add_image(myNewImage2,'B5')
myBook.save('结果表-生鲜订购表.xlsx')
