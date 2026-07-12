import openpyxl
from PIL import Image
myBook=openpyxl.load_workbook('新书订购表.xlsx')
mySheet=myBook.active
myImage1=openpyxl.drawing.image.Image('images/myImage1.jpg')
mySheet.add_image(myImage1,'A5')
#根据指定的图像文件创建图像(myImage2)
myImage2=Image.open('images/myImage2.jpg')
#根据指定参数通过裁剪和粘贴操作拼接图像(myImage2)，并将结果保存在temp目录中
myCropedImage=myImage2.crop((39,11,167,188))
myCropWidth,myCropHeight=myCropedImage.size
#创建空白的新图像(myNewImage)

myNewImage=Image.new('RGB',(256,354),'white')
myNewWidth,myNewHeight=myNewImage.size
for myLeft in range(0,myNewWidth,myCropWidth-50):
    for myTop in range(0,myNewHeight,myCropHeight-50):
        myNewImage.paste(myCropedImage,(myLeft,myTop))
myNewImage.save('temp/myImage4.jpg')
#根据temp/myImage2.jpg这个拼接之后的图像(文件)创建图像(myNewImage2)
myNewImage2=openpyxl.drawing.image.Image('temp/myImage4.jpg')
#在新书订购表(mySheet)的B5单元格中添加拼接之后的图像(myNewImage2)
mySheet.column_dimensions['B'].width=32    #修改B列的宽度
mySheet.row_dimensions[5].height=268       #修改5行的高度
mySheet.add_image(myNewImage2,'B5')
myBook.save('结果表-新书订购表.xlsx')
