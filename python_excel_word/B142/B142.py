import docx
myDocument=docx.Document('航母简介.docx')
#在Word文件(myDocument)的末尾添加指定宽度和高度的图像
myDocument.add_picture('myimage.jpg',
           width=docx.shared.Cm(12),height=docx.shared.Cm(4))
myDocument.save('我的Word文件-航母简介.docx')
